from food_order.models import Cart,CartItem,Coupon,FoodOrder
from rest_framework import serializers
from food_display.api.serializers import FoodSerializer

class FoodOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model =FoodOrder
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id","food_item","quantity","price","cart"]
        #exclude = ['id',"cart"]

class CartSerializer(serializers.ModelSerializer):
    food_item=FoodSerializer(many=True, read_only=True)
    cartitems=CartItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Cart
        fields = ["user","id",'food_item',"cartitems","num_of_items","total_price","completed"]
      
        

























class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

