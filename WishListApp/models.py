from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

def upload_avatar_to(instance, filename):
    import os
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'profiles/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )

# Create your models here.

class KadoUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	dob = models.DateField(blank=True, null=True)
	# The file object will be saved to the location specified by 
	# the upload_to argument of the corresponding   
	# FileField/ImageField when calling form.save().
	# It is saved to a file on a path inside the directory 
	# named by MEDIA_ROOT, under a subdirectory named by the field's 
	# upload_to value.
	avatar = models.ImageField(blank=True, upload_to=upload_avatar_to)

	#Django's User contains username, password, email, first name, last name.

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

