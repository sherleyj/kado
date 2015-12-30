from django.conf.urls import url

from . import views

#add all urls here
app_name='WishListApp'
urlpatterns = [
    url(r'^home/', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^login/', views.login, name='login'),
    url(r'^user/(?P<user_id>[0-9]+)/$', views.user, name='user'),
    # url(r'^user/(?P<user_id>[0-9]+)/add-wish-list/$', views.addWishList, name='addWishList'),
    url(r'^user/(?P<user_id>[0-9]+)/add-wishlist/$', views.addWishList, name='add_wishlist'),
    url(r'^user/(?P<user_id>[0-9]+)/wishlist/(?P<wishlist_id>[0-9]+)$', views.wishList, name='wishlist')
]