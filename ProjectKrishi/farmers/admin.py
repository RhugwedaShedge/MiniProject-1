from django.contrib import admin

# Register your models here.

from .models import Cart, Description

admin.site.register(Cart)
admin.site.register(Description)

