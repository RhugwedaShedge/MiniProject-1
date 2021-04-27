from django import forms
from .models import Goods

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class GoodsForm(forms.ModelForm):
	class Meta:
		model = Goods
		fields = '__all__' 


