from django.shortcuts import render, HttpResponse, redirect#, JsonResponse

from django.contrib.auth import login, authenticate, logout

from django.contrib import messages

from .models import *

from .forms import GoodsForm

from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm

from .MBA import apriori_algo

import razorpay 

from django.views.decorators.csrf import csrf_exempt


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

	upload_prod = Goods.objects.all()
	prod = upload_prod
	print(upload_prod)

	ite = list(items)
	print(customer," - Customer items in cart : ",ite)

	mba = apriori_algo()
	
	cons = []
	antes = []

	for i in range(len(mba.index)):
		cons.append(list(set(mba.consequents[i])))
		antes.append(list(set(mba.antecedents[i])))
	
	print(antes)
	print(cons)
	
	
	ite = list(map(str, ite))

	upload_prod = list(map(str, upload_prod))
	print(list(upload_prod))

	test = [cons[i][0] for i in mba.index if antes[i][0] in ite]
	r = [cons[i][0] for i in mba.index if antes[i][0] in ite and cons[i][0] in upload_prod]
	
	print("test : ",test)
	print("r : ",r)

	display = []
	for i in range(len(r)):
		for j in range(len(prod)):
			if r[i] == str(prod[j]):
				display.append(prod[j])
	
	print(display)

	context = {
		'items': items,
		'order': order,
		'display': display,
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




def techniques_view(request, *args, **kwargs):
	
	return render(request, "farmers/techniques.html", {})

def registerpage_view(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created has been created! You can now login.')
			return redirect('/farmers/login/')
	else:
		form = UserRegisterForm()
	return render(request, 'farmers/register.html', {'form': form})


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


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = int(request.POST.get("amount"))*100
        client = razorpay.Client(auth=("rzp_test_RTPoTn2mcx5PoT" , "KPoZMP1UBKox3v4EDiQyc0V8"))
        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
        print(payment)
        product = Product(name=name ,amount=amount, payment_id=payment['id'])
        product.save()
        return render(request, "pay.html" , {'payment':payment})
    
    return render(request, "pay.html")


@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key , val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
        user = Product.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()
    return render(request, "success.html")

