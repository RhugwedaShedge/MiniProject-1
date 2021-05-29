from django.contrib import admin

# Register your models here.

from .models import *

#admin.site.register(Cart)

admin.site.register(Goods)

admin.site.register(Equipments)

admin.site.register(Customer)

admin.site.register(CustomerCart)

admin.site.register(CartItem)

admin.site.register(Product)

