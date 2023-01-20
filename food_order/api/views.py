from food_order.models import Cart,CartItem ,FoodOrder
from rest_framework.response import Response
from rest_framework import viewsets
from food_order.api.serializers import CartSerializer,CartItemSerializer,FoodOrderSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from food_display.models import Food
#from food_display.api.permissions import IsOwnerOfObject
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.http import JsonResponse,HttpResponse
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser



class CartViewSet(viewsets.ViewSet):
    
    
    def get_permissions(self):
        if self.action in ['update', 'delete', 'list',"create",'destroy']:
            self.permission_classes = [IsAuthenticated() ]
            return super().get_permissions()
            
       
    def list(self ,request):
        queryset = Cart.objects.all().filter()
        serializer = CartSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        

    def create(self, request):
        queryset = Cart.objects.get_or_create(user=request.user, completed=False)
        serializer = CartSerializer(data=request.data,user=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def retrieve(self, request, pk=None):
        cart = get_object_or_404(Cart, pk=pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        cart = get_object_or_404(Cart, pk=pk)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        cart = get_object_or_404(Cart, pk=pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
            
class CartItemViewSet(viewsets.ViewSet):
    def get_permissions(self):
        if self.action in ['update', 'delete', 'list',"create",'delete']:
            self.permission_classes = [IsAuthenticated() ]
            return super().get_permissions()
            
    
    def list(self,request):
        queryset = CartItem.objects.all()#.filter(user=request.user)
        serializer = CartItemSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request,pk=None):
        cart_item = CartItem.objects.get(pk=pk)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

    def retrieve(self, request, pk=None):
        cart_item = get_object_or_404(CartItem, pk=pk)
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)
        
        
        

    def update(self, request,pk=None):
        cart_item = get_object_or_404(CartItem, pk=pk)
        serializer = CartItemSerializer(cart_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
      #  Ordring functionality 
     
class OrderViewSet(viewsets.ViewSet):
    def get_permissions(self):
        if self.action in ['retrieve',"list"]:
            self.permission_classes = [IsAdminUser, ]
        elif self.action in ['create']:
            self.permission_classes = [IsAuthenticated,]
        return super().get_permissions()
    
    
    def list(self,request):                                                 # Listing all the orders
        queryset = FoodOrder.objects.all()
        serializer = FoodOrderSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    
    def create(self, request):                                             # Users orders the food from his cart  and gets mail from website with order details
        serializer = FoodOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cart_id=serializer.data['cart_id']
            print(cart_id)
            cart= Cart.objects.get(id=cart_id)
            total_amount=cart.total_price
            Order_id =serializer.data['id']
            print(total_amount,Order_id)
            send_mail('Your Order Details', 
                      f"Your Order_id is {Order_id}/n Total Amount is {total_amount}",
                      "fooddeliver@gmail.com", 
                      [f"{request.user.email}"])
        
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    def retrieve(self, request, pk=None):                       # Retriving the individual orders      
        order = get_object_or_404(FoodOrder, pk=pk)
        serializer = FoodOrderSerializer(order)
        return Response(serializer.data)
    
    def delete(self, request, pk=None):                          # Deleting the individual orders                 
        order = get_object_or_404(FoodOrder, pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
    
    
    
    
    
#         name = request.user.username
#         email = request.user.email
#         cart_details = Cart.objects.get(user=user.id)
#         total_price = (cart_details.num_of_items )
#         FoodOrder =FoodOrder.objects.create(name=name, email=email, total_price=total_price).save()
        
#         def list(self,request):
#             queryset = FoodOrder.objects.all()#.filter()
#             serializer = FoodOrderSerializer(queryset,many=True)
#             return Response(serializer.data,status=status.HTTP_200_OK)
            
#         def create(self, request): 
#             name = request.user.username
#             email = request.user.email
#             cart_details = Cart.objects.get(user=user.id)
#             total_price = (cart_details.num_of_items )
#             FoodOrder =FoodOrder.objects.create(name=name, email=email, total_price=total_price)
#             queryset =FoodOrder.objects.all()
#             serializer = FoodOrderSerializer(queryset,many=True)
#             return Response(serializer.data,status=status.HTTP_200_OK)
        
            
                
        
    
    
    
    
# #     def list(self,request):
# #         user=request.user
# #         print(user.id)
# #         print(user.username)
# #         items=Cart.objects.get(user=user.id)
# #         print(items.num_of_items)
# #         print(items.total_price)
# #         print(items.cartitems.values())
# #         #print(items.cartitems.id)
# #         items2=CartItem.objects.get(id=items.id)
#         print(item2)
#         # print(Cart.objects.all().filter(id=items))
#         # queryset = Cart.objects.filter(id=user.id)
# #         # return HttpResponse(queryset.values())
       
#     def create(self, request):
#         name = request.user.username
#         email = request.user.email
#         cart_details = Cart.objects.get(user=user.id)
#         total_price = (cart_details.num_of_items )
#         Order = Order.objects.create(name=name, email=email, total_price=total_price)
#         Order.save()
        
        
        
        
        
    
    
        
    
   