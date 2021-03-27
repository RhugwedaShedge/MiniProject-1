from django.contrib import admin
from django.urls import path

from farmers.views import home_view

app_name = 'farmers'

urlpatterns = [

    path('home/', home_view, name = 'home'),
]