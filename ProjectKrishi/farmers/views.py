from django.shortcuts import render, HttpResponse, redirect#, JsonResponse

from django.contrib.auth import login, authenticate, logout

from django.contrib import messages

from .models import *

from .forms import GoodsForm, CreateUserForm

from django.contrib.auth.decorators import login_required

from .MBA import apriori_algo

# Create your views here.

def home_view(request, *args, **kwargs):
	a = []
	s = list(frozenset(i for i in range(3)))
	for i in range(3):
		a.append(s[i])
	print(a)

	return render(request, "farmers/index.html", {})


def about_view(request, *args, **kwargs):
	
	return render(request, "farmers/about.html", {})


@login_required(login_url = 'login')
def cart_view(request, *args, **kwargs):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = CustomerCart.objects.get_or_create(customer=customer, complete=False)
		items = order.cartitem_set.all()
	
	else:
		items = []


	r = []
	mba = apriori_algo()
	# for i in range(2):
	# print(mba.consequents)
	# print(list(mba.consequents))
	# l = list(mba.consequents.items())
	# print(l)

	# print(mba.antecedents)
	# print(list(mba.antecedents))
	# 	print(mba.index)
	for i in mba.index:
		# print(mba.antecedents[i])
		# print(mba.consequents[i])
		if mba.antecedents[i] == frozenset({'WOODLAND'}):
			print('1')
			print(mba.consequents[i])
	r = [mba.consequents[i] for i in mba.index if mba.antecedents[i] == frozenset({'WOODLAND'})]
	# print(r)


	context = {
		'items': items,
		'order': order,
		'r'  : r,
	}

	return render(request, "farmers/cart.html", context)


@login_required(login_url = 'login')
def checkout_view(request, *args, **kwargs):
	
	return render(request, "farmers/checkout.html", {})

def contact_us_view(request, *args, **kwargs):
	
	return render(request, "farmers/contact-us.html", {})

def gallery_view(request, *args, **kwargs):
	
	return render(request, "farmers/gallery.html", {})

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


@login_required(login_url = 'login')
def wishlist_view(request, *args, **kwargs):
	
	return render(request, "farmers/wishlist.html", {})


@login_required(login_url = 'login')
def profile_view(request, pk):

	if request.user.is_authenticated:
		customer = request.user.customer

	goods = Goods.objects.filter(customer=customer)
	equipments = Equipments.objects.all()

	context = {
		'goods': goods,
		'equipments': equipments,
	}

	return render(request, "farmers/profile.html", context)



def add_to_cart(request, *args, **kwargs):

	#if request.method == "POST":

	
	return render(request, "farmers/shop.html", {})


def upload_view(request):

	if request.user.is_authenticated:
		customer = request.user.customer

	form = GoodsForm(initial = {'customer': customer})
	#form_equip = EquipmentsForm(initial = {'customer': customer})

	if request.method == "POST":
		
		form = GoodsForm(request.POST)

		if form.is_valid():
			
			form.save()

			prod = Goods.objects.last()
			upd = Goods.objects.filter(product_name=prod).update(customer=customer)
			
			return redirect('/farmers/home/')

	context = {
		'form': form,
	}

	return render(request, "farmers/upload.html", context)
	



# def UpdateItem(request):
# 	return JsonResponse('Item was added', safe = False)


def registerpage_view(request):

	# if request.user.is_authenticated:
	# 	return redirect('/farmers/home/')
	# else:	 
	form = CreateUserForm()

	if request.method == "POST":
		form = CreateUserForm(request.POST)

		if form.is_valid():
			form.save()
				
			user = form.cleaned_data.get('username')
			messages.success(request, "Account is created for " + user)
				
			return redirect('/farmers/login/')

	context = {
		'form': form
	}

	return render(request, 'farmers/register.html', context)


def loginpage_view(request):

	if request.user.is_authenticated:
		return redirect('/farmers/home/')
	else:
		if request.method == "POST":
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username = username, password = password)

			if user is not None:
				login(request, user)

				return redirect('/farmers/home/')
			else:
				messages.info(request, 'Username or Password is incorrect')


		context = {}

		return render(request, 'farmers/login.html', context)



def techniques_view(request, *args, **kwargs):
	
	return render(request, "farmers/techniques.html", {})


def search_product(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Goods.objects.filter(name__contains=query_name)
            return render(request, 'main.html', {"results":results})

    return render(request, 'main.html')