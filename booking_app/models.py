
from django.db import models
import uuid
from app_login.models import User

# Create your models here.
class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=100)
    restaurant_about = models.CharField(max_length=100)
    restaurant_address = models.CharField(max_length=400)
    
    def __str__(self):
        return self.restaurant_name
   
    
class Booking(models.Model):
    booking_id=models.UUIDField(default=uuid.uuid4, editable=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,related_name='booking_details')
    no_seats=((i,i) for i in range (1,40))
    seats_booked =models.IntegerField(default=1,choices=no_seats)
    date_of_booking = models.DateField()
    completed = models.BooleanField(default=False)
    
    
        
    def __str__(self):
        return self.booking_id 
