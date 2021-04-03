from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Cart(models.Model):
	image  		 = models.ImageField(default = "product_default.png", null = True, blank = True) 
	product_name = models.CharField(max_length = 120, null = True)
	price		 = models.DecimalField(decimal_places = 2, max_digits = 100)
	quantity     = models.DecimalField(decimal_places = 0, max_digits = 100)
	total_price  = models.DecimalField(decimal_places = 2, max_digits = 100)

class Description(models.Model):

	#image  		 = models.ImageField(default = "farmers/product_default.png", null = True, blank = True) 
    category     = models.CharField(max_length = 120, null = True)
    product_name = models.CharField(max_length = 120, null = True)
    price		 = models.DecimalField(decimal_places = 2, max_digits = 100)
    stock        = models.DecimalField(decimal_places = 0, max_digits = 100)
    desc         = models.CharField(max_length = 500, null = True)

class Product(models.Model):
	name    = models.CharField(max_length=200)
	price   = models.FloatField()
	digital = models.BooleanField(default=False,null=True, blank=True)
	image   = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

