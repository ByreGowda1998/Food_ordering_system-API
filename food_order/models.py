from django.db import models
import uuid
from app_login.models import User
from food_display.models import Food


# Creating Cupon code  for discount

class Coupon(models.Model):
    code = models.CharField(primary_key=True, max_length=50, unique=True)
    active = models.BooleanField()

    def __str__(self):
        return self.code



class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)   #creating Unique id for every order
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)

 #Convert to Api
 
    @property
    def total_price(self):
        cartitems = self.cartitems.all()
        total = sum([item.price for item in cartitems])
        return total
      
    @property
    def num_of_items(self):
        cartitems = self.cartitems.all()
        quantity = sum([item.quantity for item in cartitems])
        return quantity

    

#Cerating Model for store the  items that are added to the cart
class CartItem(models.Model):
    food_item = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='food_item')
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE, related_name="cartitems")
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.food_item)


    @property
    def price(self):
        new_price = self.food_item.price * self.quantity
        return new_price

 
class FoodOrder(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    cart_id =models.ForeignKey(Cart, on_delete= models.CASCADE,related_name="cart_details")
    
    
    def __str__(self):
        return str(self.id)