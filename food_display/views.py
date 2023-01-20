from django.shortcuts import render
from .models import Food
from django.core.paginator import Paginator  # Importing Paginator
# Create your views here.


def menu(request):
    food_item = Food.objects.all()
    paginator = Paginator(food_item,8)   # Defining no of objects in each page
    page_number = request.GET.get('page') 
    page_obj= paginator.get_page(page_number)
    return render (request,'food_dispaly/menu.html',{'food_item':page_obj})