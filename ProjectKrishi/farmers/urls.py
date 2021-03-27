from django.contrib import admin
from django.urls import path

from .views import ( home_view,
                        about_view,
                        cart_view,
                        checkout_view,
                        contact_us_view,
                        gallery_view,
                        my_account_view,
                        shop_detail_view,
                        shop_view,
                        wishlist_view  )

app_name = 'farmers'

urlpatterns = [

    path('home/', home_view, name = "home"),
    path('about/', about_view, name = "about"),
    path('cart/', cart_view, name = "cart"),

]


