from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from WishListApp.models import KadoUser, WishList, WishListItem
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	return render(request, 'WishListApp/index.html')
	# return HttpResponse("Hello, world.  You're at the WishListApp index.")

def about(request):
	return HttpResponse("About Us / How it works")

def user(request, user_id):
	if not request.user.is_authenticated():
		return render(request, 'WishListApp/login.html')
	if int(request.user.id) != int(user_id):
		return HttpResponse("You are user %s. You can access user %s's profile" % (request.user.id, user_id))
		# return render(request, 'WishListApp/login.html')
	user = get_object_or_404(User, pk=user_id)
	wishlists = WishList.objects.filter(user=user).distinct()
	return render(request, 'WishListApp/user.html',{'user':user, 'wishlists':wishlists})

def login(request):
	# return HttpResponse("Login here!")
	username = request.POST.get('username')
	password = request.POST.get('psw')
	user = authenticate(username=username, password=password)
	msg = ""

	if request.method == 'POST':
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				# return HttpResponse(username)
				return HttpResponseRedirect(reverse('WishListApp:user',args=(user.id,)))
			else:
				return HttpResponse("User Not Active!")
		else:
			msg = "invalid login"
	
	return render(request, 'WishListApp/login.html', {'error_message':msg})
			# return HttpResponse("invalid login")

def addWishList(request, user_id):
	# try:
	# 	u = User.objects.get(id=user_id)
	# 	user_name = u.first_name
	# except:
	# 	return HttpResponse("User doesn't exist!")
	user = get_object_or_404(User, pk=user_id)
	try:
		new_wishlist = WishList.objects.create(name=request.POST['name'],user=user)
	except:
		return render(request, 'WishListApp/user.html', {'user':user, 'error_message': "Error wish list not created."})
	return HttpResponseRedirect(reverse('WishListApp:wishlist', args=(user_id, new_wishlist.id)))

def wishList(request, user_id, wishlist_id):
	user = get_object_or_404(User, pk=user_id)
	wish_list = get_object_or_404(WishList, pk=wishlist_id)
	wishlist_items = WishListItem.objects.filter(wish_list=wish_list)
	return render(request, 'WishListApp/wishlist.html', {'user':user, 'wishlist':wish_list, 'wishlist_items':wishlist_items})

def addItem(request, user_id, wishlist_id):
	user = get_object_or_404(User, pk=user_id)
	wish_list = get_object_or_404(WishList, pk=wishlist_id)
	try:
		new_wishlist_item = WishListItem.objects.create(name=request.POST['name'], url=request.POST['url'], wish_list=wish_list)
	except:
		return render(request, 'WishListApp/wishlist.html', {'user':user, 'wishlist':wish_list, 'error_message':"Error: item not added to wishlist."})
	return HttpResponseRedirect(reverse('WishListApp:wishlist', args=(user_id, wishlist_id)))



