from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from django.shortcuts import get_object_or_404
from booking_app.api.serializers import BookingSerializer,RestaurantSerializer
from booking_app.models import Booking, Restaurant
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from django.core.mail import send_mail
# Creating Viewsets Booking

class BookingViewSet(viewsets.ViewSet):
    queryset = Booking.objects.all()
    
    def list(self, request):                                                         # Listing all the booking details of the users 
        queryset = Booking.objects.all()
        serializer = BookingSerializer(queryset, many=True,context={"request": 
                      request})
        return Response(serializer.data)
    
    def create(self, request):                                                         # Creating New  and sending email on succesfull booking 
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            booking_id = serializer.data['booking_id']
            Restaurant = serializer.data['restaurant']
            no_seats = serializer.data['seats_booked']
            date_of_booking = serializer.data['date_of_booking']
            send_mail('Your Booking Details', 
            f"Your Booking_id ={booking_id} \n Restaurant details ={Restaurant}  /n No of seats {no_seats}  \n Date of booking = {date_of_booking}",
            "fooddeliver@gmail.com", 
            [f"{request.user.email}"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):                                              #Retriving Booking details by  user id
        booking = get_object_or_404(Booking, pk=pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)
    
    def update(self, request, pk=None):                                                # Upating Booking details by  user id
        booking = get_object_or_404(Booking, pk=pk)
        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_)
    
    def delete(self, request, pk=None):                                                 # Deleting Booking details by  user id
        booking = get_object_or_404(Booking, pk=pk)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
# Creating Viewsets Restaurant
    
class RestaurantViewSet(viewsets.ViewSet):                                         
    queryset = Restaurant.objects.all()
    
    def list(self, request):                                                #   Listing all the restaurant  and thee booking details of each Restaurant
        queryset = Restaurant.objects.all()
        serializer = RestaurantSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):                                              # CReating New Restaurant
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def retrieve(self, request, pk=None):                                   # Retriving Restaurant details by Restaurant id
        restaurant = get_object_or_404(Restaurant, pk=pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)
    
    def delete(self, request, pk=None):                                    # Deleting Restaurant details by Restaurant id
        restaurant = Restaurant.objects.get(pk=pk)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):                                       # Updating Restaurant details by
        restaurant = get_object_or_404(Restaurant, pk=pk)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     



