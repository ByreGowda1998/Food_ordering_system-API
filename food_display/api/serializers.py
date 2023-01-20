from food_display.models import Food_Category,Food
from rest_framework import serializers



        
class FoodSerializer(serializers.ModelSerializer):
    # image = serializers.SerializerMethodField()
  
    
    
    
    class Meta:
        model = Food
        fields = '__all__'
    
        
class FoodCategorySerializer(serializers.ModelSerializer):
    food_category=FoodSerializer(many=True,read_only=True)

    class Meta:
        model = Food_Category
        fields = '__all__'        