import MySQLdb
from user_content.models import *

def ask(query):
	"""Function retrieves rows based on the given query"""
	db=MySQLdb.connect("localhost","root","jose",'estore')
	cur=db.cursor()
	cur.execute(query)
	rows=cur.fetchall()
	return rows

def build_set(fields,lists):
	"""Returns a queryset from a list of dictionaries"""
	list1=[]
	#Building a list of added cart items
	for i in lists:
		listin=[]
		for j in fields:
			listin.append(i[j])
		list1.append(listin)
	return list1

def getUserData(user,fields,category):
	"""Gets the user recommendations based on purchase history"""
	q="select prdts from user_content_userdata where user='%s' and category='%s'"%(user,category)
	d=ask(q)

	if not d:
		return
	l=[]
	for i in d[0][0]:
		if ','not in i and ';' not in i:
		       l.append(i)
	
	#reducing l for unique elements
	l=list(set(l))
	
	r=[]
	#gettin the id content from table
	for i in l:
	     q="select * from %s where id='%s'"%(getTable(category),i)
	     x=ask(q)
	     r.append(x)

	#getting rdict
	rdict={}
	for i in fields:
	 temp=[]
	 for j in r:
	  for k in j:
	   temp.append(k[int(i)])
	 rdict[i]=temp
	
	return rdict


def getTable(category):
	"""Gets the appropriate table of category"""
	table=""
	if category=='books':
		table="content_book"
	elif category=='television':
		table="content_television"
	elif category=='laptop':
		table="content_laptop"
	elif category=='mobile':
		table="content_mobile"
	elif category=='camera':
		table="content_camera"
	return table

def getmax(l):
	"""Gets the most common element in the list"""
	no=0
	lar=""
	for i in l:
		if no<=l.count(i):
			no=l.count(i)
			lar=i
	return lar



def getList(rdict,fields,category,field):
	"""Gets the prdts to be recommended to the user"""
	
	q=""
	qlist=[]
	
	if not rdict:
		return
	
	no=0
	rows=[]
	for i in fields:
		fd=rdict[str(field[no])]
		lar=getmax(fd)
		q="select * from %s where %s like '%s'"%(getTable(category),i,fd[-1:][0])
		qr="select * from %s where %s like '%s'"%(getTable(category),i,lar)
		no+=1
		s=ask(q)
		s1=ask(qr)
		if s not in rows:
			rows.append(s)
		if s1 not in rows:
			rows.append(s1)

	rows=list(set(rows))
	
	return rows

def test():
	c=getUserData('tom',['2','3','5'],'books')
	r=getList(c,['section','authors','publisher'],'books',['2','3','5'])
	return r



	


			
		
	
