from django.db import models
from django.utils.text import slugify
# Create your models here.

from django.contrib.auth.models import User
from django.utils.timezone import now

class Customer(models.Model):
	user		= models.OneToOneField(User, null = True, on_delete = models.CASCADE)
	name  		= models.CharField(max_length = 120, null = True)
	phone		= models.CharField(max_length = 120, null = True)
	email		= models.CharField(max_length = 120, null = True)
	address     = models.CharField(max_length = 120, null = True)
	date_created= models.DateTimeField(auto_now_add = True, null = True)

	def __str__(self):
		return self.name


class Goods(models.Model): 
	customer     = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
	image  		 = models.ImageField(default = "rice.jpg", null = True, blank = True)
	category     = models.CharField(max_length = 120, null = True)
	product_name = models.CharField(max_length = 120, null = True)
	price		 = models.DecimalField(decimal_places = 2, max_digits = 100)
	stock        = models.DecimalField(decimal_places = 0, max_digits = 100)
	min_purchase = models.DecimalField(decimal_places = 0, max_digits = 100, default=5)
	desc         = models.CharField(max_length = 500, null = True)
	
	def __str__(self):
		return self.product_name


class Equipments(models.Model):
	image  		 = models.ImageField(default = "product_default.jpg", null = True, blank = True)
	product_name = models.CharField(max_length = 120, null = True)
	price		 = models.DecimalField(decimal_places = 2, max_digits = 100)
	stock        = models.DecimalField(decimal_places = 0, max_digits = 100)
	min_purchase = models.DecimalField(decimal_places = 0, max_digits = 100, default=5)
	desc         = models.CharField(max_length = 500, null = True)

	def __str__(self):
		return self.product_name


class CustomerCart(models.Model):
	customer      = models.OneToOneField(Customer, on_delete=models.SET_NULL, blank=True, null=True)
	complete      = models.BooleanField(default=False, null=True, blank=False)
	delivery_cost = models.DecimalField(decimal_places = 2, max_digits = 100)


	@property
	def get_cart_total(self):
		cartitems = self.cartitem_set.all()
		total = sum([item.get_total for item in cartitems])

		return total

	@property
	def get_grand_total(self):
		total = int(self.delivery_cost + self.get_cart_total)

		return total


class CartItem(models.Model):
	product     = models.ForeignKey(Goods, on_delete=models.SET_NULL, blank=True, null=True)
	order       = models.ForeignKey(CustomerCart, on_delete=models.SET_NULL, blank=True, null=True)
	quantity    = models.DecimalField(decimal_places = 0, max_digits = 100)

	def __str__(self):
		return self.product.product_name

	@property
	def get_total(self):
		total = self.product.price * self.quantity

		return total
	
class Product(models.Model):
    name       = models.CharField(max_length=100)
    amount     = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid       = models.BooleanField(default=False)



class Comment(models.Model):
	product_name = models.ForeignKey(Goods,null=True,on_delete=models.CASCADE,related_name='comments')
	comm_name = models.CharField(max_length=100,blank=True)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	body = models.TextField(max_length=500)
	date_added=models.DateTimeField(auto_now_add=True)

	def save(self,*args,**kwargs):
		self.comm_name= slugify ("comment by"+"-"+str(self.author)+str(self.date_added))
		super().save(*args,**kwargs)


	def __str__(self):
		return self.comm_name

	class Meta:
		ordering =['-date_added']



class Reply(models.Model):
	comment_name=models.ForeignKey(Comment,on_delete=models.CASCADE,related_name='replies')
	reply_body=models.TextField(max_length=500)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	date_added=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "reply to"+str(self.comment_name.comm_name)
