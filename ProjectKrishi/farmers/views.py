from django.shortcuts import render, HttpResponse, redirect

from .models import *

from .forms import GoodsForm

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


def profile_view(request, pk):

	goods = Goods.objects.all()
	equipments = Equipments.objects.all()


	customer = Customer.objects.get(id = pk)

	form = GoodsForm(initial = {'customer': customer})
	#form_equip = EquipmentsForm(initial = {'customer': customer})

	if request.method == "POST":
		
		form = GoodsForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/farmers/home/')

	context = {
		'goods': goods,
		'equipments': equipments,
		'form': form,
	}

	return render(request, "farmers/profile.html", context)



def add_to_cart(request, *args, **kwargs):

	#if request.method == "POST":

	
	return render(request, "farmers/shop.html", {})

def upload_view(request, *args, **kwargs):
	
	return render(request, "farmers/upload.html", {})

def techniques_view(request, *args, **kwargs):
	
	return render(request, "farmers/techniques.html", {})
