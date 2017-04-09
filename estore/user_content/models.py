from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	"""Implements relating to the user profile"""
	address = models.TextField()
	nationality = models.CharField(max_length=30)
	user = models.ForeignKey(User, unique=True)

class Cart(models.Model):
	"""Implements the shopping cart"""
	user = models.CharField(max_length=30)
	prdts = models.TextField()
	date = models.DateField()
	time = models.TimeField()

class UserData(models.Model):
	"""User data of purchase"""
	user = models.CharField(max_length=30)
	category = models.CharField(max_length=30)
	prdts = models.TextField()


