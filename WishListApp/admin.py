from django.contrib import admin

# Register your models here.
from WishListApp.models import KadoUser, WishList, WishListItem

admin.site.register(KadoUser)
admin.site.register(WishList)
admin.site.register(WishListItem)