from django.contrib import auth
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from user_content.forms import UserForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from user_content.models import UserProfile
from content import db
from django.http import Http404
from user_content.models import *
from content.models import *


# View for displaying the home page
def home(request):
	"""Function displays the home page"""

	###GETTING THE LATEST PRODUCTS###
	booklist = Book.objects.order_by("-id")[0:10]# Product selection based on product age
	tvlist = Television.objects.order_by("-id")[0:10]# Product selection based on product age
	laplist = Laptop.objects.order_by("-id")[0:10]# Product selection based on product age
	moblist = Mobile.objects.order_by("-id")[0:10]# Product selection based on product age
	camlist = Camera.objects.order_by("-id")[0:10]# Product selection based on product age

	###IDENTIFYING THE USER###
	if request.user.is_authenticated():
		request.session['user']=request.user
	else:
		request.session['user']='Guest'
	###RETURNING THE RESPECTIVE PAGE###
	return render_to_response('home.html',{'user': request.user,'book':booklist,'tv':tvlist,'lap':laplist,'mob':moblist,'cam':camlist})


# View for the user login
@csrf_exempt
def login(request):
    """Function manages user login"""
    ###USER AUTHENTICATION###
    # if redierects if user is already logged in
    if request.user.is_authenticated():
	return render_to_response('loggedin.html')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
	request.session['user']=request.user
        # Redirect to a success page.
        return HttpResponseRedirect("/home/")
    else:
        ###ERROR HANDLING###
	error=""
	if request.method=='POST':
		error="Invalid Username or Password"
		return render_to_response('login.html',{'error':error})
	else:
		return render_to_response('login.html',{'error':error})

       

# View for user registration/signup
@csrf_exempt
def register(request):
    """Function for user signup"""
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
	    cd=form.cleaned_data
	    ###CREATING USER ###
            new_user = User(username=cd['username'],first_name=cd['first_name'],last_name=cd['last_name'],email=cd['email'])
	    new_user.save()
	    ###SETTING USER PASSWORD ###
	    user = User.objects.get(username=cd['username'])
	    user.set_password(cd['password1'])
	    user.save()
	    ###SETTING UP USER PROFILE ###
	    new_profile=UserProfile(user=new_user,address=cd['address'],nationality=cd['nationality'])
	    new_profile.save()
            return HttpResponseRedirect("/home/")
    else:
        form = UserForm()
    return render_to_response("signup.html", {
        'form': form,
    })

# View for successful logout
def logout_view(request):
    """Function for user logout"""
    auth.logout(request)
    request.session['user']=None
    # Redirect to a success page.
    return HttpResponseRedirect("/loggedout/")

# View for display of a successful logout page
def success_logout(request):
	return render_to_response('logout.html')


def addcart(request,category,item_id):
	"""Adds an item to the cart"""

	user=request.user
	fields=['title','category','price']
	if request.session.get('cur_queryset'):
		queryset=request.session['cur_queryset']
		
		itemid=int(item_id)
		itemid=itemid-1

		item=queryset[itemid]#extracts the item to be added
		prdt={}#dictionary for storing item details
	
		product_id = item[0]
		item=item[1:]# removes loop id
		no=0

		# creates the dictionary for the product
		prdt['id']=product_id
		prdt['category']=category
		prdt['title']=item[0]
		prdt['price']=item[6]

		prdt_list=[]
		# saving user cart session
		if not request.session.get('cart'):
			prdt_list.append(prdt)
			request.session['cart']={'user':user, 'list':prdt_list}
		else:
			cart=request.session['cart']
			prdt_list=cart['list']
			prdt_list.append(prdt)
			request.session['cart']={'user':user, 'list':prdt_list}
	
		return HttpResponseRedirect('/viewcart/')
	else:
	        raise Http404()


def view_cart(request):
	"""Displays the cart"""
	user=request.user

	fields=['title','category','price']
	if request.session.get('cart'):
		cart=request.session['cart']
		prdt_list=cart['list']
		list1=db.build_set(fields,prdt_list)
		return render_to_response('cart.html',{'list':list1, 'field':fields, 'user':user})
	else:
		return render_to_response('cart.html',{'field':fields, 'user':user})

def remove_cart(request,item_no):
	"""Removes a particular item from the cart"""
	user=request.user

	cart=request.session['cart']
	prdt_list=cart['list']
	prdt_list.pop((int(item_no)-1))
	request.session['cart']={'user':user, 'list':prdt_list}
	return HttpResponseRedirect('/viewcart/')

def checkout(request):
	"""Function for enabling checkout"""
	if request.session.get('cart'):
		cart=request.session['cart']
		user1=request.user
	
		prdt=cart['list']
		save={}
		for i in prdt:
			if save.get(i['category']):
				temp_list=save[i['category']]
				temp_list.append(i['id'])
				save[i['category']]=temp_list
			else:
				temp_list=[]			
				temp_list.append(i['id'])
				save[i['category']]=temp_list
	
		data=""
		for i in save.keys():
			data="%s:"%i
			for j in save[i]:
				data+="%s,"%j
			data=data[:-1]
			data+=";\n"
	
		from datetime import datetime
		now=datetime.today()
		date1="%s-%s-%s"%(now.year,now.month,now.day)
		time1="%s:%s:%s"%(now.hour,now.minute,now.second)
	
		s=Cart(user=user1.username,prdts=data,date=date1,time=time1)
		s.save()

		temp=""
		flag=False
		for i in save.keys():
			q = UserData.objects.filter(user=user1.username,category=i)
			if q:
				p=UserData.objects.get(user=user1.username,category=i)
				flag=True
			else:
				p=UserData(user=user1.username,category=i)
			if flag:
				temp=p.prdts
				temp=temp[:-1]
				temp+=','
			for j in save[i]:
				temp+="%s,"%j
			temp=temp[:-1]
			temp+=";"
			p.prdts=temp
			p.save()
		request.session['cart']=None
		return HttpResponseRedirect('/success/')
	else:
		raise Http404()

def success_checkout(request):
	"""Displays successful checkout page"""
	user=request.user
	return render_to_response('checkout.html',{'user':user})



		
		


	
