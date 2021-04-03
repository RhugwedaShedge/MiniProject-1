from django.contrib import admin

# Register your models here.

from .models import Cart, Goods, Equipments

admin.site.register(Cart)

admin.site.register(Goods)

admin.site.register(Equipments)