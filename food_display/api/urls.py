from django.urls import path,include
from food_display.api.views import FoodCategoryViewSet,FoodViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'food_cat', FoodCategoryViewSet,basename="food_cat")
router.register(r'food_item', FoodViewSet,basename="food_items")

urlpatterns = [
    path('', include(router.urls)),

]