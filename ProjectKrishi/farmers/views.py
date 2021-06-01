

from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
 
from django.urls import reverse_lazy



from django.shortcuts import render, HttpResponse, redirect, get_object_or_404


from os import name
from django.shortcuts import render, HttpResponse, redirect#, JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from django.http import JsonResponse

from django.contrib.auth import login, authenticate, logout

from django.contrib import messages
from numpy import product
from razorpay import client

from .models import *

from .forms import CommentForm, GoodsForm

from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm,CommentForm,ReplyForm

from .MBA import apriori_algo

import razorpay, bz2

from django.views.decorators.csrf import csrf_exempt

import json, requests


# Create your views here.

def home_view(request, *args, **kwargs):

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

'''
def shop_view(request, *args, **kwargs):
	
	goods = Goods.objects.all()
	context = {
		'goods': goods,
		
	}
	return render(request, "farmers/shop.html", context)
'''

	
def shop_view(request, *args, **kwargs):

	goods = Goods.objects.all()
	context = {
		'goods': goods,
		
	}
	model=Goods
	form_class=CommentForm
	second_form_class=ReplyForm


	def get_context_data(self,**kwargs):
		context=super(shop_view,self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form']=self.form_class(request=self.request)
		
		if 'form2' not in context:
			context['form2']=self.second_form_class(request=self.request)
	
		return context


	def post(self,request,*args,**kwargs):
		self.object=self.get_object()
		if 'form' in request.POST:
			form_class=self.get_form_class()
			form_name='form'
		else:
			form_class=self.second_form_class
			form_name='form2'

		form=self.get_form(form_class)

		if form_name=='form' and form.isvalid():
			print("comment form is returned")
			return self.form_valid(form)
		elif form_name=='form2' and form.isvalid():
			print("reply form is returned")
			return self.form2_valid(form)

	def get_success_url(self):
		self.object=self.get_object()
		price=self.object.price
		image=self.object.image
		return reverse_lazy('goods:shop',kwargs={'price':price.slug,'image':image.slug,'slug':self.object.slug})

	def form_valid(self,form):
		self.object=self.ge_object()
		fm=form.save(commit=False)
		fm.author=self.request.user
		fm.product_name=self.object.comments.name
		fm.product_name_id=self.object.id
		fm.save()
		return HttpResponseRedirect(self.get_success_url())

	def form2_valid(self,form):
		self.object=self.ge_object()
		fm=form.save(commit=False)
		fm.author=self.request.user
		fm.comment_name_id=self.request.POST.get('comment.id')
		fm.save()
		return HttpResponseRedirect(self.get_success_url())


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



def add_to_cart(request, productId):

	print(productId)
	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = CustomerCart.objects.get_or_create(customer=customer, complete=False)

	cartItem, created = CartItem.objects.get_or_create(order=order, product=product)

	# if action == 'add':
	# 	cartItem.quantity = (cartItem.quantity + 1)
	# elif action == 'remove':
	# 	cartItem.quantity = (cartItem.quantity - 1)

	cartItem.save() 
	

	# prod = Goods.objects.all()

	# customer = get_object_or_404(Customer, user=request.user)
	# print(customer)

	# product = Goods.objects.filter(id=pk).first()

	# # if product in request.user.customer.CustomerCart.order.all():
	# # 	messages.info(request, 'You already have this in your cart')
	# # 	return redirect(reverse('product:product-list'))
	
	# cart_item, status = CartItem.objects.get_or_create(product=product)

	# customer_cart, status = CustomerCart.objects.get_or_create(customer=customer)
	# customer_cart.CartItem.add(customer_cart)

	# # if status:
	# # 	customer_cart.ref_code = generate_order_id()
	# # 	customer_cart.save()

	messages.info(request, "item added to cart")
	
	# context = {
	# 	'prod': prod,
	# }
	
	# return render(request, "farmers/shop.html", context)


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
			# user = request.user
			# print(user)
			# customer = Customer.objects.create(user = username.id)
			# print(customer)
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


	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = CustomerCart.objects.get_or_create(customer=customer, complete=False)
		items = order.cartitem_set.all()	
		
	if request.method == "POST":
		name = request.POST.get("name")
		amount = int(request.POST.get("amount"))#*100
		client = razorpay.Client(auth=("rzp_test_RTPoTn2mcx5PoT" , "KPoZMP1UBKox3v4EDiQyc0V8"))
		payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
		print(payment)
		product = Product(name=name ,amount=amount, payment_id=payment['id'])
		product.save()
		return render(request, "farmers/pay.html" , {'payment':payment})
		
	
	context = {
		'items': items,
		'order': order,
	}
	
	return render(request, "farmers/pay.html", context)

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
    return render(request, "farmers/success.html")

def searchbar_view(request):
	if request.method == "POST":
		searched = request.POST['searched']
		# goods = Goods.objects.filter(category__contains = searched)
		goods = Goods.objects.filter(product_name__contains = searched)
		return render(request, "farmers/searchbar.html", {'searched' : searched, 'goods': goods})
	else:
		return render(request, "farmers/searchbar.html")

def updateItem(request):
	# print("11")

	# data = json.loads(request.body)
	# print("22")
	# productId = data['productId']
	# action = data['action']

	# print('Action:', action)
	# print('ProductId:', productId)

	# customer = request.user.customer
	# product = Product.objects.get(id=productId)
	# order, created = Cart.objects.get_or_create(customer=customer, complete=False)

	# cartItem, created = CartItem.objects.get_or_create(order=order, product=product)

	# if action == 'add':
	# 	cartItem.quantity = (cartItem.quantity + 1)
	# elif action == 'remove':
	# 	cartItem.quantity = (cartItem.quantity - 1)

	# cartItem.save() 

	return JsonResponse('Item was added', safe=False)

