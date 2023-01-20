
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from django.shortcuts import get_object_or_404
from food_display.api.serializers import FoodCategorySerializer,FoodSerializer
from food_display.models import Food_Category,Food
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny,IsAdminUser

# Viewsets for the diffrent food categories

class FoodCategoryViewSet(viewsets.ViewSet):           
    queryset = Food_Category.objects.all()
    
    def get_permissions(self):
        if self.action in ['update', 'delete',"create"]:
            self.permission_classes = [IsAdminUser, ]
        elif self.action in ['retrieve',"list"]:
            self.permission_classes = [AllowAny]
        return super().get_permissions()
    
    
    def list(self, request):                                                       #  Listing all food categories and foods
        queryset = Food_Category.objects.all()
        serializer = FoodCategorySerializer(queryset, many=True,context={"request": 
                      request})
        return Response(serializer.data)
    
    def create(self, request):                                                    # Create a new food category
        serializer = FoodCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    def retrieve(self, request, pk=None):                                         # Retrieve a food category
        food_category = get_object_or_404(Food_Category, pk=pk)
        serializer = FoodCategorySerializer(food_category)
        return Response(serializer.data)
    
    def delete(self, request, pk):                                               # Deleting a food category
        category_name =Food_Category.objects.get(pk=pk)
        category_name.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # viewsets for the diffrent foods
    
class FoodViewSet(viewsets.ViewSet):
    queryset = Food.objects.all()
    
    def get_permissions(self):                                       # Customizing the permissions using in built permission
        if self.action in ['update', 'delete',"create"]:
            self.permission_classes = [IsAdminUser, ]
        elif self.action in ['retrieve','list']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()
    
        
    def list(self, request):                                             #Listing all the food details
            queryset = Food.objects.all()
            serializer = FoodSerializer(queryset,context={"request": 
                      request}, many=True)
            return Response(serializer.data)
        
    def create(self, request):                                           # creating new food
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):                                     # Retrieve a  individual food
        food = get_object_or_404(Food, pk=pk)
        serializer = FoodSerializer(food)
        return Response(serializer.data)
    
    def delete(self, request, pk):                                            # Deleting a  individual   details
        food_name = Food.objects.get(pk=pk)
        food_name.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    def update(self, request, pk):                                            # Updating a  individual food details
        food_name = Food.objects.get(pk=pk)
        serializer = FoodSerializer(food_name, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            