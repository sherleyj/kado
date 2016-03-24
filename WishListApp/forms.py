from django import forms
from WishListApp.models import KadoUser, WishList, WishListItem
from django.contrib.auth.models import User

class loginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=30)
	psw = forms.CharField(label='Password', max_length=30)

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('first_name', 'last_name','username', 'email', 'password')

class KadoUserForm(forms.ModelForm):
	class Meta:
		model = KadoUser
		fields = ('dob', 'avatar')

class EditUserForm(forms.ModelForm):
	class Meta:
		model = User
		exclude = ('username' ,'password', 'groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined')
		fields = ('first_name', 'last_name', 'email')

class EditKadoUserForm(forms.ModelForm):
	avatar = forms.ImageField(label='picture',required=False)
	class Meta:
		model = KadoUser
		exclude = ('user',)
		fields = ('dob', 'avatar')