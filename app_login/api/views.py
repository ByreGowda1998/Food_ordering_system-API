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
import csv
import io
from rest_framework.decorators import action
import json
from .task import read_csv_file_all
from django.http import HttpResponse
from rest_framework_api_key.permissions import HasAPIKey
#from rest_framework import permission_classes
from rest_framework_api_key.models import APIKey
from.curlgenrate import generate_curl_with_api_key
from rest_framework import serializers


class ContactViewSet(viewsets.ViewSet):
    queryset = Contact.objects.all()
  
    def get_permissions(self):
        if self.action in ['update', 'delete', 'list']:
            self.permission_classes = [HasAPIKey, ]
        elif self.action in ['create']:
            self.permission_classes = [HasAPIKey]
        return super().get_permissions()
    
    def list(self, request):
        api_key, key = APIKey.objects.create_key(name="my-remote-service2")
        # print(key)

        url="http://127.0.0.1:8000/app/contactus/"
        # headers = {
        # 'Content-Type': 'application/json',
        # 'Authorization': f'Bearer {key}'}


        curl_command=f'curl -H "X-Api-Key: {key}" "{url}"'
        print(curl_command)

        #curl_command=curl -H "X-Api-Key: ePYN96GC.yoKsr9nFQL0X7dOX0TMXhXitnzazhJ3x" "http://127.0.0.1:8000/app/contactus/"

        queryset = Contact.objects.all()
        serializer = ContactSerializer(self.queryset, many=True)
        serialized_data_json = json.dumps(serializer.data)

      
     
       
        return Response(serializer.data)

    # def retrieve(self, request, pk=None): 
    #     contact = get_object_or_404(Contact, pk=pk) i9J08cYr.wMYCmQxBm4LxpVa8IwOfLoQZ8e8aeKXV
    #     serializer = ContactSerializer(contact)
    #     return Response(serializer.data)

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
            
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request,pk):
        contact = Contact.objects.get(pk=pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    @action(detail=False, methods=['POST'])
    def read_csv_file(self,request): 
        read_csv_file_all(request)
        # print("complted task")
        # # return Response(data=read_csv_file_all.data, status=status.HTTP_201_CREATED)
        return HttpResponse("worked")


        # paramFile = request.FILES['file'].read().decode('utf-8')
        # reader = csv.DictReader(io.StringIO(paramFile))
        # content = paramFile  
        # data = [line for line in reader]
        # upload_file = request.FILES['file']
        # print(content)
        # json_obj = json.dumps(data,indent = 4)
        # contactus_details= json.loads(json_obj)
        # sucess_details=[]
        # for row in contactus_details:
        #     send_details={}
        #     send_details["email"] =row["Email"]
        #     send_details["subject"] =row["Subject"]
        #     send_details["message"] =row["Message"]
        #     serializer = ContactSerializer(data=send_details,context={'request':request})
        #     print(serializer)
        #     if serializer.is_valid():
        #         print(serializer.validated_data)
        #         serializer.save()
        #         sucess_details.append(send_details)
        #         send_mail(
        #         "Contact form",
        #          serializer.data['message'],
        #          serializer.data['email'],
        #         ['fooddeliver@gmail.com'])
        #         sucess_details.append(send_details)
        #     else:
        #         pass
       
        # return Response(data = sucess_details)
      

                
    
    
    
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