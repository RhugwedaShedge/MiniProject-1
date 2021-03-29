from django.db import models

# Create your models here.
<<<<<<< HEAD
class Description(models.Model):

	#image  		 = models.ImageField(default = "farmers/product_default.png", null = True, blank = True) 
    Category = models.CharField(max_length = 120, null = True)
	product_name = models.CharField(max_length = 120, null = True)
	price		 = models.DecimalField(decimal_places = 2, max_digits = 100)
	stock     = models.DecimalField(decimal_places = 0, max_digits = 100)
	desc = models.CharField(max_length = 500, null = True)
=======

from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
	image  		 = models.ImageField(default = "farmers/product_default.png", null = True, blank = True) 
	product_name = models.CharField(max_length = 120, null = True)
	price		 = models.DecimalField(decimal_places = 2, max_digits = 100)
	quantity     = models.DecimalField(decimal_places = 0, max_digits = 100)
	total_price  = models.DecimalField(decimal_places = 2, max_digits = 100)
>>>>>>> eb7294bfa2d592cf5267a7940220c871cf78ac44
