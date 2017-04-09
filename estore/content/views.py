from django.shortcuts import render_to_response
from django.http import HttpResponse
from content.forms import *
from content.product import *
from content import db
from content.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404


# View for category search 
def search(request,category):
	"""Function to identify the user request of an advanced search and 
	   present appropriate form"""

	user=request.session['user']

	###FROM OBJECT CREATION###
	#if contruct to set the form with the right object variable
	if category=='books':
		form = BookForm(request.GET or None)
		field_list = Book().fields()
	elif category=='television':
		form = TVForm(request.GET or None)
		field_list = Television().fields()
	elif category=='laptop':
		form = LapForm(request.GET or None)
		field_list = Laptop().fields()
	elif category=='mobile':
		form = MobForm(request.GET or None)
		field_list = Mobile().fields()
	elif category=='camera':
		form = CamForm(request.GET or None)
		field_list = Camera().fields()
	
	###REQUEST HANDLING###
	if request.method == 'GET' and form.is_valid():#check for the form validity and request method
		cd  = form.cleaned_data#extract the form data
		query = product().form(category,cd)#extracts the queries in relation to the form
		head = query.keys()
		if len(head)>1:
			store_data = {'category':category, 'head':head, 'dict':query, 'field':field_list}
			request.session[category] = store_data
			query_result=db.ask(query['exact'])
			###ADDING RESULTS TO THE CART###
			request.session['cur_queryset']=query_result
			
			return render_to_response('search_result.html', {'category': category, 'query':query_result, 'field':field_list, 'head':head, 'user': user})
		else:
			head = []
			return render_to_response('search_result.html', {'category': category, 'head':head, 'user': user})
	
   	return render_to_response('search_form.html', {'category':category, 'form': form, 'user':user})

def suggest(request,category,field):
	"""Function presents suggestion to the user based on a specific query"""

	###EXTRACTION OF SESSION DATA###
	store_data = request.session[category]
	field_list=store_data['field']
	qu=store_data['dict']
	qu=qu[field]
	r=db.ask(qu)

	user=request.session['user']
	if request.user.is_authenticated():
				request.session['cur_queryset']=r

	###RENDERING RESPONSE###
	if r:
		return render_to_response('suggest_result.html', {'query':r, 'field':field_list, 'user': user, 'category':category})
	else:
		return render_to_response('suggest_result.html', {'query':"No results", 'category':CAT, 'user': user})


def product_view(request,category,item_id):
	"""Function displays the product information"""

	user=request.session['user']
	befor=request.session['cur_queryset']
	result=befor[int(item_id)-1]
	request.session['prdt']=result
	result=result[1:]
	
	field_list=[]
	request.session['category']=category
	###CHECKING FOR THE CATEGORY FOR QUERY###
	store_data = request.session[category]
	field_list=store_data['field']

	if result:
		return render_to_response('product.html', {'query':result, 'field':field_list, 'user': user})
	else:
		return render_to_response('product.html', {'query':result,'user': user})

@csrf_exempt	
def category_page(request,category):
	"""Function that displays the recommended products of the category"""

	###INITIALIZING DETAILS###
	rlist=[]
	ulist=[]
	llist=[]
	user=request.user
	request.session['category']=category
	
	###RETRIVING PRODUCT DETAILS FROM THE DATABASE###
	#Getting user recommendations
	if request.user.is_authenticated():
		if category=='books':
			rdict=db.getUserData(user.username,Book().recommend_no(),category)
			ulist=db.getList(rdict,Book().recommend_list(),category,Book().recommend_no())
		elif category=='television':
			rdict=db.getUserData(user.username,Television().recommend_no(),category)
			ulist=db.getList(rdict,Television().recommend_list(),category,Television().recommend_no())
		elif category=='laptop':
			rdict=db.getUserData(user.username,Laptop().recommend_no(),category)
			ulist=db.getList(rdict,Laptop().recommend_list(),category,Laptop().recommend_no())
		elif category=='mobile':
			rdict=db.getUserData(user.username,Mobile().recommend_no(),category)
			ulist=db.getList(rdict,Mobile().recommend_list(),category,Mobile().recommend_no())
		elif category=='camera':
			rdict=db.getUserData(user.username,Camera().recommend_no(),category)
			ulist=db.getList(rdict,Camera().recommend_list(),category,Camera().recommend_no())
			
		
		ul=[]
		if ulist:
			for i in ulist[0]:
				if category=='books':
					p=Book()
				elif category=='television':
					p=Television()
				elif category=='laptop':
					p=Laptop()
				elif category=='mobile':
					p=Mobile()
				elif category=='camera':
					p=Camera()
				p.make(i)
				ul.append(p)

	#Getting recommendations common for all users		
	if category=='books':
		rlist = Book.objects.order_by("-rating")[0:20]# Product selection based on the rating
		llist = Book.objects.order_by("-id")[0:20]# Product selection based on product age
	elif category=='television':
		rlist = Television.objects.order_by("-rating")[0:20]# Product selection based on the rating
		llist = Television.objects.order_by("-id")[0:20]# Product selection based on product age
	elif category=='laptop':
		rlist = Laptop.objects.order_by("-rating")[0:20]# Product selection based on the rating
		llist = Laptop.objects.order_by("-id")[0:20]# Product selection based on product age
	elif category=='mobile':
		rlist = Mobile.objects.order_by("-rating")[0:20]# Product selection based on the rating
		llist = Mobile.objects.order_by("-id")[0:20]# Product selection based on product age
	elif category=='camera':
		rlist = Camera.objects.order_by("-rating")[0:20]# Product selection based on the rating
		llist = Camera.objects.order_by("-id")[0:20]# Product selection based on product age

	###REQUEST HANDLING###
	if request.method == 'POST':
		selection = request.POST['basis']
		
		#Selecting the list to pass
		if 'Rat' in selection:
			request.session['curlist']=rlist
			return render_to_response('cat_page.html',{'plist':rlist,'user':user,'category':category,'sel':selection})
		elif 'Rec' in selection and request.user.is_authenticated():
			request.session['cur_list']=ul
			return render_to_response('cat_page.html',{'plist':ul,'user':user,'category':category,'sel':selection,})
		
		elif 'New' in selection:
			request.session['curlist']=llist			
			return render_to_response('cat_page.html',{'plist':llist,'user':user,'category':category,'sel':selection})
		
	else:
		if user.is_authenticated() and ulist:
			selection = 'Recommended'
			request.session['cur_list']=ul
			n=ul
		else:
			selection = 'Product Rating'
			request.session['curlist']=rlist
			n=rlist
		
		return render_to_response('cat_page.html',{'user':user,'category':category,'sel':selection,'plist':n})


def prdt(request,category,item_id):
	"""Displays a recommended product info"""
	
	user=request.session['user']
	plist=request.session['curlist']
	n=len(plist)
	
	p=plist[n-int(item_id)]
	if category=='books':
		field_list = Book().fields()
	elif category=='television':
		field_list = Television().fields()
	elif category=='laptop':
		field_list = Laptop().fields()
	elif category=='mobile':
		field_list = Mobile().fields()
	elif category=='camera':
		field_list = Camera().fields()
	j=p.make_list()
	return render_to_response('product.html', {'field':field_list,'query':j,'p':p,'plist':plist})

def rate(request,rated):
	if request.session.get('prdt'):
		prdt=request.session['prdt']
		p=Book.objects.get(title=prdt[1])
		r=p.rating
		rated=int(rated)/2
		r+=(r-rated/10)
		r="%.1f"%r
		p.rating=r
		p.save()
		return HttpResponseRedirect('../')
	else:
		raise Http404()



		
	
	


		
	
