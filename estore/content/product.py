from forms import *


class product:
	"""The class defines routines in relation to product
	   categorization and the related backedn query 
	   bulding and HTML display"""
	
	def product_table_select(self,category):
		"""Attains the table name in association to a specific
		   category"""
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

	def optimize(self,query_dict):
		"""Optimizes the given query list"""
				
		for i in query_dict.keys():
			query_dict[i]=query_dict[i].replace("'#","'%")# replaces for beginning of substring check '%<some_data>%'
			query_dict[i]=query_dict[i].replace("$'","%'")# replaces for end of substring check '%<some_data>%'
			
			
		
		return query_dict

	def splitter(self,data,field):
		"""Splits the data given as a combination to specific
		   filed queries"""
		data_list=data.split(',')
		ret_string=""
		
		for i in data_list:
			ret_string=ret_string+" %s like '#%s$' ||" %(field,i)

		if ret_string[-2:]=='||':#checks if last 2 characters are '||'
			ret_string=ret_string[:-2]#removes the last '||' from the query
		
		return ret_string
			
	def form(self,category,form_data):
		"""The funtion builds the query list in a decreasing
		   order of priority for recommendation"""
	
		query_base = "select * from %s where"%(self.product_table_select(category))
		query_dict = {}#stores the query dictionary of decreasing priority
		query=query_base
	
		for i in form_data.keys():
			if form_data[i]:
				if ',' in form_data[i]:
					query=query+self.splitter(form_data[i],i)+" &&"#to redierect field data having combinational data(egs:authors)
				else:
					query=query+" %s like '#%s$' &&"%(i,form_data[i])#builds the query for matching the parameters exactly
		
		if query[-2:]=='&&':#checks if last 2 characters are '&&'
			query=query[:-2]#removes the last '&&' from the query
		query_dict['exact']=query
		
		#loop for building the list of queries
		for i in form_data.keys():
			if form_data[i]:
				if 'title' not in i:
					query=query_base
					if ',' in form_data[i]:
						query=query+self.splitter(form_data[i],i)#to redierect field data having combinational data(egs:authors)
					else:
						query=query+" %s like '#%s$'"%(i,form_data[i])#builds the query for matching the parameters exactly
		
					query_dict[i]=query

		query_dict=self.optimize(query_dict) #call for the optimization function

		return query_dict

#end of class
