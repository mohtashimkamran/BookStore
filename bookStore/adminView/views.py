from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework import generics , mixins

from .serializers import UserSerializer
from .models import User
import json 

def Home(request):
    return HttpResponse("HELLO")

class NewUser(generics.GenericAPIView):
    def post(self,request):
        body = json.loads(request.body.decode('utf-8'))
        username = body['username']
        email = body['email']
        password = body['password']
        mobile = body['mobile']

        new = User(username=username, email=email,mobile=mobile,password=password,is_staff=True,is_admin=True,is_superuser=True,is_active=True)
        print(new)
        new.save()
        new.set_password(new.password)
        new.save()

        return JsonResponse('Naya user bangaya hai bhai',safe=False,status=201)