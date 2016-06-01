from django import forms
from WishListApp.models import KadoUser, WishList, WishListItem
from django.contrib.auth.models import User

class loginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=30)
	psw = forms.CharField(label='Password', max_length=30)

class UserForm(forms.ModelForm):
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
	last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
	email = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	class Meta:
		model = User
		fields = ('first_name', 'last_name','username', 'email', 'password')


class KadoUserForm(forms.ModelForm):
	avatar = forms.ImageField(label='Profile picture',required=False)
	dob = forms.DateField(label='', widget=forms.SelectDateWidget(empty_label=("Year", "Month", "Day"),))
	class Meta:
		model = KadoUser
		fields = ('dob', 'avatar')

class EditUserForm(forms.ModelForm):
	class Meta:
		model = User
		exclude = ('username' ,'password', 'groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined')
		fields = ('first_name', 'last_name', 'email')

class EditKadoUserForm(forms.ModelForm):
	avatar = forms.ImageField(label='Profile picture',required=False)
	class Meta:
		model = KadoUser
		exclude = ('user',)
		fields = ('dob', 'avatar')

class addItemForm(forms.ModelForm):
	class Meta:
		model = WishListItem
		exclude = ('name', 'wish_list', 'image', 'description', 'store')
		fields = ('url',)

class EditItemForm(forms.ModelForm):
	name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Item name'}))
	image = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Image URL'}))
	description = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Description'}))
	class Meta:
		model = WishListItem
		fields = ('name', 'description')
		exclude = ('url', 'wish_list', 'store', 'image')



