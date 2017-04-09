from django.forms import ModelForm
from content.models import *
from django import forms

class BookForm(ModelForm):
	title = forms.CharField(required=False)
	section = forms.CharField(required=False)
	authors = forms.CharField(required=False)
	subject = forms.CharField(required=False)
	publisher = forms.CharField(required=False)

	class Meta:
	        model = Book
		exclude = ('publication_date','photo', 'price', 'description',)
		fields = ('title', 'authors', 'subject','section', 'publisher')

class TVForm(ModelForm):
	"""Form for getting data from users regarding TV search"""
	title = forms.CharField(required=False)
	tv_type = forms.CharField(required=False)
	company = forms.CharField(required=False)
	size = forms.CharField(required=False)
	resolution = forms.CharField(required=False)

	class Meta:
	        model = Television
		exclude = ('power','launch_date','photo', 'price', 'description','rating')
		fields = ('title','tv_type', 'company', 'size','resolution')


class LapForm(ModelForm):
	"""Form for Laptop details"""
	title = forms.CharField(required=False)
	screen_size = forms.CharField(required=False)
	company = forms.CharField(required=False)
	processor = forms.CharField(required=False)
	resolution = forms.CharField(required=False)
	memory = forms.CharField(required=False)
	graphics_card =forms.CharField(required=False)
	
	class Meta:
	        model = Laptop
		exclude = ('power','launch_date','photo', 'price', 'description','rating','accessories')
		fields = ('title','screen_size', 'company', 'processor','resolution','memory','graphics_card')


class MobForm(ModelForm):
	"""Form for Mobile details"""
	title = forms.CharField(required=False)
	phone_type = forms.CharField(required=False)
	company = forms.CharField(required=False)
	camera = forms.CharField(required=False)
	bluetooth = forms.CharField(required=False)
	GPRS = forms.CharField(required=False)
	
	class Meta:
	        model = Mobile
		exclude = ('size','weight','display_size','dispaly_colours','battery','standby_time','launch_date','photo', 'price', 'description','rating','accessories')
		fields = ('title','phone_type', 'company', 'camera','bluetooth','GPRS')


class CamForm(ModelForm):
	"""Form for camera details"""
	title = forms.CharField(required=False)
	company = forms.CharField(required=False)
	model = forms.CharField(required=False)
	optical_zoom = forms.CharField(required=False)
	digital_camera_type = forms.CharField(required=False)
	
	class Meta:
	        model = Camera
		exclude = ('battery','memory_card_format','display_size','launch_date','photo', 'price', 'description','rating','accessories')
		fields = ('title','company', 'model', 'optical_zoom','digital_camera_type')




