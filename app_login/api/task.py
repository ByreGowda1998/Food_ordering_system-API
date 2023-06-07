from celery import shared_task 
from django.core.mail import send_mail
from time import sleep
from .serializers import ContactSerializer
import csv
import json
import io
from rest_framework.response import Response
from django.http import HttpResponse

@shared_task(bind=True)
def read_csv_file_all(self,request):  # sourcery skip: merge-dict-assign
        paramFile = request.FILES['file'].read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(paramFile))
        content = paramFile  
        data = [line for line in reader]
        upload_file = request.FILES['file']
        print(content)
        json_obj = json.dumps(data,indent = 4)
        contactus_details= json.loads(json_obj)
        sucess_details=[]
        for row in contactus_details:
            send_details={}
            send_details["email"] =row["Email"]
            send_details["subject"] =row["Subject"]
            send_details["message"] =row["Message"]
            sucess_details.append(send_details)
            serializer = ContactSerializer(data=send_details,context={'request':request})
            print(serializer)
            if serializer.is_valid():
                print(serializer.validated_data)
                serializer.save()
                send_mail(
                "Contact form",
                 serializer.data['message'],
                 serializer.data['email'],
                ['fooddeliver@gmail.com'])
                sucess_details.append(send_details)
            else:
                pass
        read_csv_file_all.data={"sucess_details":sucess_details}

        print("completed the task")

