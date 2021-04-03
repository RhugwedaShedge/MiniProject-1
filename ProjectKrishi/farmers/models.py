from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Cart(models.Model):
	image  		 = models.ImageField(default = "product_default.png", null = True, blank = True) 
	product_name = models.CharField(max_length = 120, null = True)
	price		 = models.DecimalField(decimal_places = 2, max_digits = 100)
	quantity     = models.DecimalField(decimal_places = 0, max_digits = 100)
	total_price  = models.DecimalField(decimal_places = 2, max_digits = 100)

class Goods(models.Model):
	#image  		 = models.ImageField(default = "farmers/product_default.png", null = True, blank = True) 
    category     = models.CharField(max_length = 120, null = True)
    product_name = models.CharField(max_length = 120, null = True)
    price		 = models.DecimalField(decimal_places = 2, max_digits = 100)
    stock        = models.DecimalField(decimal_places = 0, max_digits = 100)
    desc         = models.CharField(max_length = 500, null = True)

class Equipments(models.Model):

	#image       = models.ImageField(default = "farmers/product_default.png", null = True, blank = True) 
	#category    = models.CharField(max_length = 120, null = True)
	product_name = models.CharField(max_length = 120, null = True)
	price		 = models.DecimalField(decimal_places = 2, max_digits = 100)
	stock        = models.DecimalField(decimal_places = 0, max_digits = 100)
	min_purchase = models.DecimalField(decimal_places = 0, max_digits = 100, default=5)
	desc         = models.CharField(max_length = 500, null = True)


