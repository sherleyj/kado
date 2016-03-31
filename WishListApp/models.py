from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# needed to delete imagefield file from s3 when user replaces it
import boto
from boto.s3.connection import S3Connection, Bucket, Key
from django.conf import settings


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

	def save(self, *args, **kwargs):
		# delete old file when replacing by updating the file
		try:
			this = KadoUser.objects.get(id=self.id)
			if this.avatar != self.avatar:
				conn = S3Connection(settings.AWS_S3_ACCESS_KEY_ID, settings.AWS_S3_SECRET_ACCESS_KEY)
				bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
				# k = Key(bucket)
				key = bucket.get_key(str(this.avatar))
				print(this.avatar)
				# k.key = str(this.avatar)
				bucket.delete_key(key)
				# this.avatar.delete(save=False)
		except: pass # when new photo then we do nothing, normal case
		super(KadoUser, self).save(*args, **kwargs)

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

