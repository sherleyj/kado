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
	user = get_object_or_404(User, pk=user_id)
	if not request.user.is_authenticated():
				return render(request, 'WishListApp/login.html')

	return render(request, 'WishListApp/user.html',{'user':user})

def login(request):
	# return HttpResponse("Login here!")
	username = request.POST.get('username')
	password = request.POST.get('psw')
	user = authenticate(username=username, password=password)

	# if request.method =
	if user is not None:
		if user.is_active:
			auth_login(request, user)
			# return HttpResponse(username)
			return HttpResponseRedirect(reverse('WishListApp:user',args=(user.id,)))
		else:
			return HttpResponse("User Not Active!")
	else:
		return render(request, 'WishListApp/login.html', {'error_message':'invalid login'})
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
	return render(request, 'WishListApp/wishlist.html', {'user':user, 'wishlist':wish_list})
