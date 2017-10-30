from django.conf.urls import url

from . import views

#add all urls here
app_name='WishListApp'
urlpatterns = [
    url(r'^home/', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<error_msg>[0-9]+)$', views.index, name='index-error'),
    # url(r'^home/(?P<error_msg>[:print:]+)$', views.index, name='index-error'),
    url(r'^about/', views.about, name='about'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    # url(r'^signup/', views.signUp, name='signup'),
    url(r'^signup/', views.signUpNew, name='signup'),
    url(r'^give/', views.give, name='give'),
    url(r'^user/(?P<user_id>[0-9]+)/(?P<wishlist_id>[0-9]+)/$', views.user, name='user'),
    # url(r'^user/(?P<user_id>[0-9]+)/add-wish-list/$', views.addWishList, name='addWishList'),
    url(r'^user/(?P<user_id>[0-9]+)/add-wishlist/$', views.addWishList, name='add_wishlist'),
    url(r'^user/(?P<user_id>[0-9]+)/wishlist/(?P<wishlist_id>[0-9]+)/$', views.wishList, name='wishlist'),
    url(r'^user/(?P<user_id>[0-9]+)/(?P<wishlist_id>[0-9]+)/edit_item/$', views.editItem, name="edititem"),
    url(r'^user/(?P<user_id>[0-9]+)/(?P<wishlist_id>[0-9]+)/add_item/$', views.addItem, name="additem"),
    url(r'^user/(?P<user_id>[0-9]+)/(?P<wishlist_id>[0-9]+)/edit_profile/$', views.editUserInfo, name="editinfo"),
    url(r'^user/(?P<user_id>[0-9]+)/(?P<wishlist_id>[0-9]+)/$', views.findUser, name='finduser'),
    url(r'^user/(?P<user_id>[0-9]+)/(?P<wishlist_id>[0-9]+)/(?P<item_id>[0-9]+)/edit_item/$', views.editItem, name="edititemuser"),
    url(r'^submitedititem/(?P<item_id>[0-9]+)/$', views.submitEditItem, name="submitedititem"),
    url(r'^deleteitem/(?P<item_id>[0-9]+)/$', views.deleteItem, name="deleteitem"),
    url(r'^search/', views.search, name='search'),

]