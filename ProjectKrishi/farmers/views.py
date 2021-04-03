from django.shortcuts import render, HttpResponse

from .models import *

# Create your views here.

def home_view(request, *args, **kwargs):

	return render(request, "farmers/index.html", {})


def about_view(request, *args, **kwargs):
	
	return render(request, "farmers/about.html", {})


def cart_view(request, *args, **kwargs):

	carts = Cart.objects.all()
	print(carts)
	context = {
		'carts': carts,
	}

	return render(request, "farmers/cart.html", context)

# def Desciption_view(request, *args, **kwargs):


def checkout_view(request, *args, **kwargs):
	
	return render(request, "farmers/checkout.html", {})

def contact_us_view(request, *args, **kwargs):
	
	return render(request, "farmers/contact-us.html", {})

def gallery_view(request, *args, **kwargs):
	
	return render(request, "farmers/gallery.html", {})

def checkout_view(request, *args, **kwargs):
	
	return render(request, "farmers/checkout.html", {})

def my_account_view(request, *args, **kwargs):
	
	return render(request, "farmers/my-account.html", {})

def shop_detail_view(request, *args, **kwargs):
	
	return render(request, "farmers/shop-detail.html", {})

def shop_view(request, *args, **kwargs):
	
	return render(request, "farmers/shop.html", {})

def wishlist_view(request, *args, **kwargs):
	
	return render(request, "farmers/wishlist.html", {})


def profile_view(request, *args, **kwargs):

	goods = Goods.objects.all()
	equipments = Equipments.objects.all()

	print(goods)
	print(equipments)

	context = {
		'goods': goods,
		'equipments': equipments,
	}

	return render(request, "farmers/profile.html", context)


def add_to_cart(request, *args, **kwargs):

	#if request.method == "POST":

	
	return render(request, "farmers/shop.html", {})


