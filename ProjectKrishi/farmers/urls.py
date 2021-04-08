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
                        wishlist_view,
                        profile_view,
                        upload_view ,
                        techniques_view, )

app_name = 'farmers'

urlpatterns = [

    path('home/', home_view, name = "home"),
    path('about/', about_view, name = "about"),
    path('cart/', cart_view, name = "cart"),
    path('checkout/', checkout_view, name = "checkout"),
    path('contact_us/', contact_us_view, name = "contact_us"),
    path('gallery/', gallery_view, name = "gallery"),
    path('my_account/', my_account_view, name = "my_account"),
    path('shop_detail/', shop_detail_view, name = "shop_detail"),
    path('shop/', shop_view, name = "shop"),
    path('wishlist/', wishlist_view, name = "wishlist"),
    path('profile/<str:pk>', profile_view, name = "profile"),
    path('upload/', upload_view, name = "upload"),
    path('techniques/', techniques_view, name = "techniques"),
]


