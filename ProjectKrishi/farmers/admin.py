from django.contrib import admin
from recsys.models import *
# Register your models here.

from .models import *

admin.site.register(Cart)

admin.site.register(Goods)

admin.site.register(Equipments)

admin.site.register(Customer)

admin.site.register(CustomerCart)

admin.site.register(CartItem)

