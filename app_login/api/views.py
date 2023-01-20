from app_login.models import Contact
from rest_framework.response import Response
from rest_framework import viewsets
from app_login.api.serializers import ContactSerializer,RegistrationSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from app_login.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser

#from rest_framework import permission_classes

class ContactViewSet(viewsets.ViewSet):
    queryset = Contact.objects.all()
    #permission_classes=[IsAuthenticated,IsAdminUser]
    def get_permissions(self):
        if self.action in ['update', 'delete', 'list']:
            self.permission_classes = [IsAdminUser, ]
        elif self.action in ['create']:
            self.permission_classes = [AllowAny,]
        return super().get_permissions()
    
    def list(self, request):
        queryset = Contact.objects.all()
        serializer = ContactSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        contact = get_object_or_404(Contact, pk=pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def create(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                "Contact form",
                 serializer.data['message'],
                 serializer.data['email'],
                ['fooddeliver@gmail.com'])
           
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_)
    

    def delete(self, request,pk):
        contact = Contact.objects.get(pk=pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    # Registrtioning the new user using api and genrating the Token
class RegistrationViewSet(viewsets.ViewSet):
    
    def create(self, request):
        serializer = RegistrationSerializer(data=request.data)
         
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
        
            data['response'] = "Registration Successfyl !"
            data['username'] = account.username
            data['email'] = account.email
                
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
    
   # Logout the user  and delete the token of the particular user
        
class LogoutViewSet(viewsets.ViewSet):
    
    def create(self, request):
        try:
            print(request.user.auth_token)
            request.user.auth_token.delete()
        except (AttributeError):
            pass
        from django.contrib.auth import logout
        logout(request)

        return Response({"success": ("Successfully logged out.")},
                        status=status.HTTP_200_OK)