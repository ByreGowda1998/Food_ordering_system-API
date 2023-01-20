from django.urls import path,include
from food_order.api.views import CartViewSet,CartItemViewSet,OrderViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet,basename="Cart")
router.register(r'cartitem', CartItemViewSet,basename="CartItem")
router.register(r'order', OrderViewSet,basename="Order")

urlpatterns = [
    path('', include(router.urls)),

]