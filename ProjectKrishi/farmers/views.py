from django.shortcuts import render, HttpResponse

from .models import *

# Create your views here.

def home_view(request, *args, **kwargs):

	return render(request, "farmers/index.html", {})


def about_view(request, *args, **kwargs):
	
	return render(request, "farmers/about.html", {})


def cart_view(request, *args, **kwargs):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = CustomerCart.objects.get_or_create(customer=customer, complete=False)
		items = order.cartitem_set.all()
	else:
		items = []

	context = {
		'items': items,
		'order': order,
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
	goods = Goods.objects.all()

	context = {
		'goods': goods,
	}
	
	return render(request, "farmers/shop.html", context)


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


