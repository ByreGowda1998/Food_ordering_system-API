from django.urls import path,include
from rest_framework import routers
from booking_app.api.views import BookingViewSet,RestaurantViewSet


router = routers.DefaultRouter()
router.register('booking', BookingViewSet,basename="booking")
router.register('restaurant', RestaurantViewSet,basename="restaurant")

urlpatterns = [
   path('', include(router.urls)),

]