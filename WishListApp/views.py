from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from WishListApp.models import KadoUser, WishList, WishListItem
from django.core.urlresolvers import reverse
from WishListApp.scrape import amazon_images, gen_images, gen_title, get_soup
import json
# from . import srape
# from bs4 import BeautifulSoup


# Create your views here.
def index(request):
	return render(request, 'WishListApp/index.html')
	# return HttpResponse("Hello, world.  You're at the WishListApp index.")

def about(request):
	return HttpResponse("About Us / How it works")

def give(request):
	return render(request, 'WishListApp/give.html')

def user(request, user_id, wishlist_id, error_msg=""):
	# must be loggen in to see user pages/wishlists
	if not request.user.is_authenticated():
		return render(request, 'WishListApp/login.html')
	# if int(request.user.id) != int(user_id):
	# 	return HttpResponse("You are user %s. You cannot access user %s's profile" % (request.user.id, user_id))
		# return render(request, 'WishListApp/login.html')
	user = get_object_or_404(User, pk=user_id)
	wishlist = get_object_or_404(WishList, pk=wishlist_id)
	#list of items in wish list
	wishlist_items = WishListItem.objects.filter(wish_list=wishlist)
	return render(request, 'WishListApp/user.html',{'user':user, 'wishlist_items':wishlist_items, 'current_user':request.user, 'wishlist':wishlist, 'error_msg': error_msg})

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
				wishlist = WishList.objects.get(user=user, name='public-'+str(user.id))
				# return HttpResponse(username)
				return HttpResponseRedirect(reverse('WishListApp:user',args=(user.id,wishlist.id,)))
			else:
				return HttpResponse("User Not Active.")
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
	wishlist = get_object_or_404(WishList, pk=wishlist_id)
	url = ""
	name = ""
	images = []
	try:
		url = request.POST['url']
		# soup = get_soup(url)
		name = gen_title(url)
		if "amazon" in url:
			images = amazon_images(url)
		else:
			images = gen_images(url)
		json_images = json.dumps(images)
		# new_wishlist_item = WishListItem.objects.create(name=name, url=request.POST['url'], image=??, wish_list=wishlist)
		# new_wishlist_item = WishListItem.objects.create(name=request.POST['name'], url=request.POST['url'], image=request.POST['image'], wish_list=wishlist)
		# wishlist_items = WishListItem.objects.filter(wish_list=wishlist)

		return render(request, 'WishListApp/add_item.html', {'user':user, 'wishlist':wishlist, 'url':url, 'name':name, 'images': images, 'json_images': json_images})
	except Exception, e:
		wishlist_items = WishListItem.objects.filter(wish_list=wishlist)
		error_msg = "Failed to add item. Error: "
		return render(request, 'WishListApp/user.html',{'user':user, 'wishlist_items':wishlist_items, 'current_user':request.user, 'wishlist':wishlist, 'error_msg': error_msg + str(e)})
		# return HttpResponseRedirect(reverse('WishListApp:user', args=(user_id, wishlist.id)))
	return HttpResponseRedirect(reverse('WishListApp:user', args=(user_id, wishlist.id)))
	# render(request, 'WishListApp/user.html',{'user':user, 'wishlist_items':wishlist_items, 'current_user':request.user, 'wishlist':wishlist, 'error_msg': ""})
	# return HttpResponse("Added Item")

def signUp(request):
	username = request.POST.get('username')
	psw = request.POST.get('psw')
	psw2 = request.POST.get('psw2')
	first_name = request.POST.get('first-name')
	last_name = request.POST.get('last-name')
	email = request.POST.get('email')
	error_message = ''

	if request.method == 'POST':
		if(psw != psw2):
			return render(request, 'WishListApp/signup.html', {'error_message':"Passwords do not match."})

		if(len(psw) < 1):
			return render(request, 'WishListApp/signup.html', {'error_message':"No password entered."})

		first_name = first_name[0].upper() + first_name[1:].lower()
		last_name = last_name[0].upper() + last_name[1:].lower()
		try:
			new_user = User.objects.create_user(username=username, password=psw, first_name=first_name, last_name=last_name, email=email)
			new_user.save()
			new_kado_user = KadoUser.objects.create(user=new_user)
			new_kado_user.save()
			new_wishlist = WishList.objects.create(name="public-" + str(new_user.id) ,user=new_user)
		# except ValueError:
		# 	return render(request, 'WishListApp/signup.html', {'error_message':"username field must be set."})
		except Exception, e:
			return render(request, 'WishListApp/signup.html', {'error_message':str(e)})
		return HttpResponseRedirect(reverse('WishListApp:user', args=(new_user.id, new_wishlist.id)))
	
	return render(request, 'WishListApp/signup.html',{'error_message':error_message})
	# return HttpResponse("Login In Here")