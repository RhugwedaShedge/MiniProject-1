from django import forms
from .models import Goods

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class GoodsForm(forms.ModelForm):
	class Meta:
		model = Goods
		fields = '__all__' 

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']