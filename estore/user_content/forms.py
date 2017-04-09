from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserForm(UserCreationForm):
	"""Form for user signup"""
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	email = forms.EmailField()
	address = forms.CharField( widget=forms.Textarea())
	nationality = forms.CharField()

	

