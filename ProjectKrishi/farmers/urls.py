from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import ( home_view,
                        about_view,
                        cart_view,
                        checkout_view,
                        registerpage_view,
                        contact_us_view,
                        gallery_view,
                        my_account_view,
                        shop_detail_view,
                        shop_view,
                        wishlist_view,
                        profile_view,
                        upload_view ,
                        techniques_view,
                        home,
                        success, )

app_name = 'farmers'

urlpatterns = [

    path('home/', home_view, name = "home"),
    path('about/', about_view, name = "about"),
    path('cart/', cart_view, name = "cart"),
    # path('checkout/', checkout_view, name = "checkout"),
    path('contact_us/', contact_us_view, name = "contact_us"),
    path('gallery/', gallery_view, name = "gallery"),
    path('my_account/', my_account_view, name = "my_account"),
    path('shop_detail/', shop_detail_view, name = "shop_detail"),
    path('shop/', shop_view, name = "shop"),
    path('wishlist/', wishlist_view, name = "wishlist"),
    path('profile/<str:pk>', profile_view, name = "profile"),
    # path('upload/<str:pk>', upload_view, name = "upload"),
    path('login/', auth_views.LoginView.as_view(template_name='farmers/login.html'), name = "login"),
	path('register/', registerpage_view, name = "register"),
	path('logout/', auth_views.LogoutView.as_view(template_name='farmers/logout.html'), name = "logout"),
    
    path('upload/', upload_view, name = "upload"),
    path('techniques/', techniques_view, name = "techniques"),
    path('checkout/', home, name="checkout"),
    path('success/',success, name="success"),
    

]


