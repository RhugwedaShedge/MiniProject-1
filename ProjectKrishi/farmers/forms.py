from django import forms
from .models import Cart

class CartForm(UserCreationForm):
	class Meta:
		model = Cart
		fields = ['username', 'email', 'password1', 'password2']

