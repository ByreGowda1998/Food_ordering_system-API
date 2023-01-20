from django.shortcuts import render,redirect
from django.http import JsonResponse
from food_display.models import Food 
from .models import Cart,CartItem,Coupon
import json
from app_login.models import Profile,User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


#add to Cart    
@login_required(login_url='loginto') 
def add_to_cart(request):
    data = json.loads(request.body)
    food_id = data["id"]
    food= Food.objects.get(id=food_id) 
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created =CartItem.objects.get_or_create(cart=cart, food_item=food)
        cartitem.quantity += 1
        cartitem.save()
    return JsonResponse("working",safe=False)
    
# dispaly food items that are added to cart
@login_required(login_url='loginto') 
def cart(request):
    cart = None
    cartitems = []
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()
        context = {"cart":cart, "items":cartitems }
    return render(request, "food_order/cart.html", context)   


#  ordering food from cart

@login_required(login_url='loginto') 
def Orderfood(request):
    print(cart.total_price)
    return render(request,"food_order/cart.html")


"""
     send_mail(
               'Your order placed Successfully',
               "order_id":f"{orderid}" "Total Amount":f"{Total_Amount}",
               f'{fooddeliver@gmail.com}',
               ['f{user.email}'])  
    
"""

# def remove_cart(request):
#     data = json.loads(request.body)
#     food_id = data["id"]
#     food= Food.objects.get(id=food_id) 
#     if request.user.is_authenticated:
#         cart, created = Cart.objects.get_or_create(user=request.user, completed=False).delete()
#         cartitem, created =CartItem.objects.get_or_create(cart=cart, food_item=food)
#         cartitem.quantity -= 1
#         cartitem.save()
#     return JsonResponse("working",safe=False)




    

    
