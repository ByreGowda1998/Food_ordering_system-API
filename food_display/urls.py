from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('menu/' ,views.menu,name = 'menu_dispaly'),
    
]