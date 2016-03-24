from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from WishListApp.models import KadoUser, WishList, WishListItem
from django.core.urlresolvers import reverse
from WishListApp.scrape import amazon_images, gen_images, gen_title, get_soup
from WishListApp.forms import UserForm, KadoUserForm, EditUserForm, EditKadoUserForm
import json
from django.contrib.auth.decorators import login_required
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
				# django function login() as authlogin so my own login can exist
				auth_login(request, user)
				wishlist = WishList.objects.get(user=user, name='public-'+str(user.id))
				# return HttpResponse(username)
				return HttpResponseRedirect(reverse('WishListApp:user',args=(user.id,wishlist.id,)))
			else:
				return HttpResponse("User Not Active.")
		else:
			msg = "invalid login"
			# form = loginForm();
	
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

def editItem(request, user_id, wishlist_id):
	user = get_object_or_404(User, pk=user_id)
	wishlist = get_object_or_404(WishList, pk=wishlist_id)
	url = ""
	title = ""
	images = []
	try:
		url = request.POST['url']
		title = gen_title(url)
		if "amazon" in url:
			images = amazon_images(url)
		else:
			images = gen_images(url)
		json_images = json.dumps(images)
		return render(request, 'WishListApp/edit_item.html', {'user':user, 'wishlist':wishlist, 'item_url':url, 'current_user':request.user, 'title':title, 'images': images, 'json_images': json_images})
	except Exception, e:
		wishlist_items = WishListItem.objects.filter(wish_list=wishlist)
		error_msg = "Error: "
		return render(request, 'WishListApp/user.html',{'user':user, 'wishlist_items':wishlist_items, 'current_user':request.user, 'wishlist':wishlist, 'error_msg': error_msg + str(e)})
		# return HttpResponseRedirect(reverse('WishListApp:user', args=(user_id, wishlist.id)))
	return HttpResponseRedirect(reverse('WishListApp:user', args=(user_id, wishlist.id)))

def addItem(request, user_id, wishlist_id):
	user = get_object_or_404(User, pk=user_id)
	wishlist = get_object_or_404(WishList, pk=wishlist_id)
	error_msg = ""
	wishlist_items = WishListItem.objects.filter(wish_list=wishlist)
	title = ""
	img_url = ""
	description = ""
	item_url = ""
	try:
		title = request.POST['title']
		img_url = request.POST['img_url']
		description = request.POST['description']
		item_url = request.POST['item_url']
		new_wishlist_item = WishListItem.objects.create(name=title, url=item_url, image=img_url, wish_list=wishlist, descripton=description)
		return HttpResponseRedirect(reverse('WishListApp:user', args=(user_id, wishlist.id)))
	except Exception, e:
		error_msg = "Failed to add Item. Error: " 
		# return HttpResponseRedirect(reverse('WishListApp:user', args=(user_id, wishlist.id)))

		return render(request, 'WishListApp/user.html', {'user':user, 'wishlist_items':wishlist_items, 'current_user':request.user, 'wishlist':wishlist, 'error_msg': error_msg + str(e)})

	return HttpResponseRedirect(reverse('WishListApp:user', args=(user_id, wishlist.id)))


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
			# upload_photo_thumb(new_kado_user, img)
			new_wishlist = WishList.objects.create(name="public-" + str(new_user.id) ,user=new_user)
		# except ValueError:
		# 	return render(request, 'WishListApp/signup.html', {'error_message':"username field must be set."})
		except Exception, e:
			return render(request, 'WishListApp/signup.html', {'error_message':str(e)})
		return HttpResponseRedirect(reverse('WishListApp:user', args=(new_user.id, new_wishlist.id)))
	
	return render(request, 'WishListApp/signup.html',{'error_message':error_message})
	# return HttpResponse("Login In Here")

def signUpNew(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		kado_user_form = KadoUserForm(data=request.POST)

		if user_form.is_valid() and kado_user_form.is_valid():
			# user_form is a ModelForm so save() returns a new 
			# user instance. It also saves it to the db unless 
			# commit = False is specified.  
			new_user = user_form.save()
			new_user.set_password(new_user.password)
			new_user.save()
			# we should set the one to one relationship before
			# saving to db
			new_kado_user = kado_user_form.save(commit=False)
			new_kado_user.user = new_user

			if 'avatar' in request.FILES:
				new_kado_user.avatar = request.FILES['avatar']

			new_kado_user.save()
			new_wishlist = WishList.objects.create(name="public-" + str(new_user.id) ,user=new_user)
			registered = True
			new_user = authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
			auth_login(request, new_user)
			return HttpResponseRedirect(reverse('WishListApp:user', args=(new_user.id, new_wishlist.id)))

		# Invalid Forms
		else:
			return render(request, 'WishListApp/signup.html', {'kado_user_form': kado_user_form, 'user_form': user_form, 'error_message': str(user_form.errors) + " " + str(kado_user_form.errors), 'registered':registered})

	# clean form
	else:
		user_form = UserForm()
		kado_user_form = KadoUserForm()

	return render(request, 'WishListApp/signup.html', {'kado_user_form': kado_user_form, 'user_form': user_form,'error_message': "", 'registered':registered})

@login_required
def editUserInfo(request, user_id, wishlist_id):
	user = get_object_or_404(User, pk=user_id)
	kado_user = KadoUser.objects.get(user=user)
	# kado_user = get_object_or_404(KadoUser, user=user)
	wishlist = get_object_or_404(WishList, pk=wishlist_id)
	updatedInfo = False

	if request.method == 'POST':
		user_form = EditUserForm(data=request.POST, instance=request.user)
		kado_user_form = EditKadoUserForm(data=request.POST, instance=KadoUser.objects.get(user=request.user))

		if user_form.is_valid() and kado_user_form.is_valid():
			# user_form is a ModelForm so save() returns a new 
			# user instance. It also saves it to the db unless 
			# commit = False is specified.  
			updated_user = user_form.save()
			# we should set the one to one relationship before
			# saving to db
			updated_kado_user = kado_user_form.save(commit=False)

			if 'avatar' in request.FILES:
				updated_kado_user.avatar = request.FILES['avatar']

			updated_kado_user.save()
			updatedInfo = True
		# Invalid Forms
		else:
			return render(request, 'WishListApp/editUserInfo.html', {'kado_user_form': kado_user_form, 'user_form': user_form, 'error_message': str(user_form.errors) + " " + str(kado_user_form.errors), 'updatedInfo':updatedInfo, 'user': user, 'wishlist': wishlist})

	# clean form
	else:
		user_form = EditUserForm(instance=request.user)
		kado_user_form = EditKadoUserForm(instance=KadoUser.objects.get(user=request.user))

	return render(request, 'WishListApp/editUserInfo.html', {'kado_user_form': kado_user_form, 'user_form': user_form,'error_message': "", 'updatedInfo':updatedInfo, 'user': user, 'wishlist': wishlist})

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/rango/')








