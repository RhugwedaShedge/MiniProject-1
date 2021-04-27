


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

	context = {
		'items': items,
		'order': order,
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



def generate_new_rules():
	# "C:\Program Files\R\R-2.15.2\bin\x64\Rscript.exe"
	RScriptCmd = u"C:\\Program Files\\R\\R-3.0.0\\bin\\x64\Rscript.exe"
	Rfilepath = os.path.join(settings.PROJECT_ROOT, 'r', 'generate_new_rules.R')
	Rargs = "--vanilla"
	command = [RScriptCmd, Rfilepath, Rargs]
	print command
	output = subprocess.Popen(command, stdout=subprocess.PIPE).stdout.read()
	print output
	return True

def remove_values_from_list(the_list, val):
	return [value for value in the_list if value != val]

def buy(request):
	if request.method == 'POST':
		form = BuyForm(request.POST) 
		if form.is_valid():
			cart = form.save()
			if Cart.objects.all().count() % 10 == 0:
				generate_new_rules()
			return redirect(buy)
	else:
		form = BuyForm()
	return render_to_response('buy.html', locals(), context_instance=RequestContext(request))

def recommned(request):
	prods =  request.GET.getlist('products')
	rec = [ str(i) for i in Recommendation.objects.filter(buy__pk__in=prods).values_list('rec__name', flat = True)]
	for p in prods:
		rec  = remove_values_from_list(rec, Product.objects.get(pk=p).name)
	c = Counter(rec).most_common()
	data = [ i[0] for i in c]
	return HttpResponse(simplejson.dumps(data), mimetype='application/json')