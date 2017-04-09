from django.db import models


# Model implementing book details
class Book(models.Model):
	"""Implementation of a book model"""
	title = models.CharField(max_length=100)
	section = models.CharField(max_length=50)
	authors = models.CharField(max_length=150)
	subject = models.CharField(max_length=50)
	publisher = models.CharField(max_length=50)
	publication_date = models.DateField(blank=True, null=True)
	price = models.DecimalField(max_digits=6,decimal_places=2)
	photo = models.ImageField(upload_to='product_photo/books/',blank=True)
	description = models.TextField()
	rating = models.FloatField()

	def __str__(self):
		return self.title

	def fields(self):
		"""Returns the field in the order of declaration"""
		field_list = ['Title','Section','Authors','Subject','Publisher','Publication Date','Price','Photo','Description','Rating']
		return field_list

	def recommend_list(self):
		"""Returns the list over which the recommendation is done"""
	
		field=['section','authors','publisher']
		return field
	
	def recommend_no(self):
		"""Returns the position of the fields on the table"""
		field=['2','3','5']
		return field
	
	def make_list(self):
		"""Returns a list of object values"""
		l=[]
		l.append(self.title)
		l.append(self.section)
		l.append(self.authors)
		l.append(self.subject)
		l.append(self.publisher)
		l.append(self.publication_date)
		l.append(self.price)
		l.append(self.photo)
		l.append(self.description)
		l.append(self.rating)
		return l

	def make(self,l):
		"""Sets an object with the corresponding values"""
		self.id=l[0]
		self.title=l[1]
		self.section=l[2]
		self.authors=l[3]
		self.subject=l[4]
		self.publisher=l[5]
		self.publication_date=l[6]
		self.price=l[7]
		self.photo=l[8]
		self.description=l[9]
		self.rating=l[10]

	

# Model for implementing television details
class Television(models.Model):
	"""Implementation of a television model"""
	title = models.CharField(max_length=100)
	tv_type = models.CharField(max_length=50)
	company = models.CharField(max_length=150)
	size    = models.CharField(max_length=150)
	resolution = models.CharField(max_length=150)
	power = models.CharField(max_length=150)
	price = models.DecimalField(max_digits=6,decimal_places=2)
	launch_date = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='product_photo/tv/',blank=True)
	description = models.TextField()
	rating = models.FloatField()

	def __str__(self):
		return self.title

	def fields(self):
		"""Returns the field in the order of declaration"""
		field_list = ['Title','Type','Company','Size','Resolution','Power Requirements','Price','Launch Date','Photo','Description','Rating']
		return field_list

	def recommend_list(self):
		"""Returns the list over which the recommendation is done"""
	
		field=['tv_type','company','size']
		return field
	
	def recommend_no(self):
		"""Returns the position of the fields on the table"""
		field=['2','3','4']
		return field

	def make_list(self):
		"""Returns a list of object values"""
		l=[]
		l.append(self.title)
		l.append(self.tv_type)
		l.append(self.company)
		l.append(self.size)
		l.append(self.resolution)
		l.append(self.power)
		l.append(self.price)
		l.append(self.launch_date)
		l.append(self.photo)
		l.append(self.description)
		l.append(self.rating)
		return l

	def make(self,l):
		"""Sets an object with the corresponding values"""
		self.id=l[0]
		self.title=l[1]
		self.tv_type=l[2]
		self.company=l[3]
		self.size=l[4]
		self.resolution=l[5]
		self.power=l[6]
		self.price=l[7]
		self.launch_date=l[8]
		self.photo=l[9]
		self.description=l[10]
		self.rating=l[11]

# Model for implementing laptop details
class Laptop(models.Model):
	"""Implemnetation of a laptop model"""
	title = models.CharField(max_length=100)
	company = models.CharField(max_length=150)
	screen_size = models.CharField(max_length=150)
	resolution = models.CharField(max_length=150)
	power = models.CharField(max_length=150)
	processor = models.CharField(max_length=150)
	price = models.DecimalField(max_digits=6,decimal_places=2)
	memory = models.CharField(max_length=150)
	graphics_card = models.CharField(max_length=150)
	accessories = models.TextField()
	launch_date = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='product_photo/laptop/',blank=True)
	description = models.TextField()
	rating = models.FloatField()

	def __str__(self):
		return self.title

	def fields(self):
		"""Returns the field in the order of declaration"""
		field_list = ['Title','Company','Screen Size','Resolution','Power Requirements','Processor','Price','Memory Capacity','Graphics Card','Accessories','Launch Date','Photo','Description','Rating']
		return field_list

	def recommend_list(self):
		"""Returns the list over which the recommendation is done"""
	
		field=['company','screen_size','processor','memory','graphics_card']
		return field
	
	def recommend_no(self):
		"""Returns the position of the fields on the table"""
		field=['2','3','5','7','8']
		return field

	def make_list(self):
		"""Returns a list of object values"""
		l=[]
		l.append(self.title)
		l.append(self.company)
		l.append(self.screen_size)
		l.append(self.resolution)
		l.append(self.power)
		l.append(self.processor)
		l.append(self.price)
		l.append(self.memory)
		l.append(self.graphics_card)
		l.append(self.accessories)
		l.append(self.launch_date)
		l.append(self.photo)
		l.append(self.description)
		l.append(self.rating)
		return l

	def make(self,l):
		"""Sets an object with the corresponding values"""
		self.id=l[0]
		self.title=l[1]
		self.company=l[2]
		self.screen_size=l[3]
		self.resolution=l[4]
		self.power=l[5]
		self.processor=l[6]
		self.price=l[7]
		self.memory=l[8]
		self.graphics_card=l[9]
		self.accessories=l[10]
		self.launch_date=l[11]
		self.photo=l[12]
		self.description=l[13]
		self.rating=l[14]

# Model for implementing mobile phone details
class Mobile(models.Model):
	"""Implementation of a mobile phone model"""
	title = models.CharField(max_length=100)
	phone_type = models.CharField(max_length=150)
	company = models.CharField(max_length=150)
	camera = models.CharField(max_length=150)
	bluetooth = models.CharField(max_length=150)
	GPRS = models.CharField(max_length=150)
	size  = models.CharField(max_length=150)
	price = models.DecimalField(max_digits=6,decimal_places=2)
	weight = models.CharField(max_length=150)
	display_size = models.CharField(max_length=150)
	display_colours = models.CharField(max_length=150)
	battery = models.CharField(max_length=150)
	standby_time = models.CharField(max_length=150)
	accessories = models.TextField()
	launch_date = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='product_photo/mobile/',blank=True)
	description = models.TextField()
	rating = models.FloatField()


	def __str__(self):
		return self.title

	def fields(self):
		"""Returns the field in the order of declaration"""
		field_list = ['Title','Type','Company','Camera','Bluetooth','GPRS','Size','Price','Weight','Display Size','Display Colors','Battery','Stand By Time', 'Accessories','Launch Date','Photo','Description','Rating']
		return field_list

	def recommend_list(self):
		"""Returns the list over which the recommendation is done"""
	
		field=['type','company']
		return field
	
	def recommend_no(self):
		"""Returns the position of the fields on the table"""
		field=['2','3']
		return field

	def make_list(self):
		"""Returns a list of object values"""
		l=[]
		l.append(self.title)
		l.append(self.phone_type)
		l.append(self.company)
		l.append(self.camera)
		l.append(self.bluetooth)
		l.append(self.GPRS)
		l.append(self.size)
		l.append(self.price)
		l.append(self.weight)
		l.append(self.display_size)
		l.append(self.display_colours)
		l.append(self.battery)
		l.append(self.standby_time)
		l.append(self.accessories)
		l.append(self.launch_date)
		l.append(self.photo)
		l.append(self.description)
		l.append(self.rating)
		return l

	def make(self,l):
		"""Sets an object with the corresponding values"""
		self.id=l[0]
		self.title=l[1]
		self.phone_type=l[2]
		self.company=l[3]
		self.camera=l[4]
		self.bluetooth=l[5]
		self.GPRS=l[6]
		self.size=l[7]
		self.price=l[8]
		self.weight=l[9]
		self.display_size=l[10]
		self.display_colours=l[11]
		self.battery=l[12]
		self.standby_time=l[13]
		self.accessories=l[14]
		self.launch_date=l[15]
		self.photo=l[16]
		self.description=l[17]
		self.rating=l[18]

# Model for implementing camera details
class Camera(models.Model):
	"""Implementation of a camera model"""
	title = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	model = models.CharField(max_length=100)
	optical_zoom = models.CharField(max_length=100)
	battery = models.CharField(max_length=100)
	digital_camera_type = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=6,decimal_places=2)
	memory_card_format = models.CharField(max_length=100)
	display_size = models.CharField(max_length=100)
	accessories = models.TextField()
	launch_date = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='product_photo/camera/',blank=True)
	description = models.TextField()
	rating = models.FloatField()
		
	
	def __str__(self):
		return self.title

	def fields(self):
		"""Returns the field in the order of declaration"""
		field_list = ['Title','Company','Model','Optical Zoom','Battery','Camera Type','Price','Memory Card Format','Display Size', 'Accessories','Launch Date','Photo','Description','Rating']
		return field_list

	def recommend_list(self):
		"""Returns the list over which the recommendation is done"""
	
		field=['company','model','digital_camera_type']
		return field
	
	def recommend_no(self):
		"""Returns the position of the fields on the table"""
		field=['2','3','6']
		return field

	def make_list(self):
		"""Returns a list of object values"""
		l=[]
		l.append(self.title)
		l.append(self.company)
		l.append(self.model)
		l.append(self.optical_zoom)
		l.append(self.battery)
		l.append(self.digital_camera_type)
		l.append(self.price)
		l.append(self.memory_card_format)
		l.append(self.display_size)
		l.append(self.accessories)
		l.append(self.launch_date)
		l.append(self.photo)
		l.append(self.description)
		l.append(self.rating)
		return l

	def make(self,l):
		"""Sets an object with the corresponding values"""
		self.id=l[0]
		self.title=l[1]
		self.company=l[2]
		self.model=l[3]
		self.optical_zoom=l[4]
		self.battery=l[5]
		self.digital_camera_type=l[6]
		self.price=l[7]
		self.memory_card_format=l[8]
		self.display_size=l[9]
		self.accessories=l[10]
		self.launch_date=l[11]
		self.photo=l[12]
		self.description=l[13]
		self.rating=l[14]

