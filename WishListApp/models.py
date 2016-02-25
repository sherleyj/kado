from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class KadoUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	dob = models.DateField(blank=True, null=True)
	photo = models.URLField(blank=True)


	def __str__(self):
		return self.user.first_name + " " + self.user.last_name

class WishList(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=200, blank=True)
	# email, mailing address, phone number,

	def __str__(self):
		return self.name

class WishListItem(models.Model):
	wish_list = models.ForeignKey(WishList)
	name = models.CharField(max_length=100, blank=True)
	url = models.URLField()
	image = models.URLField()
	descripton = models.CharField(max_length=500, blank=True)
	store = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.name