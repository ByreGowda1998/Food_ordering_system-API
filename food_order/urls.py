from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("cart/", views.cart, name="cart"),
    path('add_to_cart/' ,views.add_to_cart,name = 'add'),
    # path('remove_cart/' ,views.remove_cart,name = 'remove'),
    path('order/' ,views.Orderfood ,name='order'),
    
    
]