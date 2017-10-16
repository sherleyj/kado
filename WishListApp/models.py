from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# needed to delete imagefield file from s3 when user replaces it
import boto
from boto.s3.connection import S3Connection, Bucket, Key
from django.conf import settings

from django.core.validators import RegexValidator


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
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list


	#Django's User contains username, password, email, first name, last name.

	def __str__(self):
		return self.user.first_name + " " + self.user.last_name

	def save(self, *args, **kwargs):
		# delete old file when replacing by updating the file
		try:
			this = KadoUser.objects.get(id=self.id)
			# print("self: " + str(self.user.first_name))
			# print("this: " + str(this.user.first_name))
			if this.avatar != self.avatar:
				conn = S3Connection(settings.AWS_S3_ACCESS_KEY_ID, settings.AWS_S3_SECRET_ACCESS_KEY)
				bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
				key = bucket.get_key(str(this.avatar))
				# print("this: "+ str(this.avatar))
				# print("self: " + str(self.avatar))
				bucket.delete_key(key)
		except: pass # when new photo then we do nothing, normal case
		super(KadoUser, self).save(*args, **kwargs)

class WishList(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=2000, blank=True)
	# email, mailing address, phone number,

	def __str__(self):
		return self.name

class WishListItem(models.Model):
	wish_list = models.ForeignKey(WishList)
	name = models.CharField(max_length=100, blank=True)
	url = models.URLField()
	image = models.URLField()
	product_description = models.CharField(max_length=500, blank=True)
	store = models.CharField(max_length=100, blank=True)
	store_shortcut_icon = models.URLField(blank=True) # favicon
	date_added = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	received = models.BooleanField(default=False)
	purchased = models.BooleanField(default=False)
	quantity = models.CharField(blank=True, max_length=1000)
	user_comment = models.CharField(blank=True, max_length=500)

	def __str__(self):
		return self.name

