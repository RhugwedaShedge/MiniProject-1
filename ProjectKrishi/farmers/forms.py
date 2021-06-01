from django import forms
from django.contrib.auth import models
from .models import Comment, Goods, Reply

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class GoodsForm(forms.ModelForm):
	class Meta:
		model = Goods
		fields = '__all__' 

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm):

	widgets={
		'body': forms.Textarea(attrs={'class':'form-control','rows':4,'cols':70,'placeholder':'Enter the comment here'})
	}
	class Meta:
		model = Comment
		fields = ('body',)
		labels={"body":"Comment:"}

	

class ReplyForm(forms.ModelForm):
	class Meta:
		model = Reply
		fields = ('reply_body',)
		

		widgets={
			'reply_body': forms.Textarea(attrs={'class': 'form-control' ,'rows' :2 , 'cols' : 10})
		}





        