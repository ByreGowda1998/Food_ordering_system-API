from rest_framework import serializers
from booking_app.models import Booking,Restaurant

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
        
class RestaurantSerializer(serializers.ModelSerializer):
    booking_details=BookingSerializer(many=True,read_only=True)
    id =serializers.URLField()
    class Meta:
        model = Restaurant
        fields = '__all__'
        
