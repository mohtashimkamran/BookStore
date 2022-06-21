from re import I
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework import generics , mixins
from rest_framework.decorators import api_view

from .serializers import UserSerializer
from .models import User
import json 

def Home(request):
    return render(request, 'adminView/home.html')

@api_view(['POST','GET'])
def Signup(request):
    if request.method == "POST":
        body = request.POST
        username = body['username']
        email = body['email']
        password = body['password']
        new = User(username=username, email=email,password=password)
        new.save()
        new.set_password(new.password)
        new.save()
        return render(request,'adminView/home.html')    
    else:
        return render(request, 'adminView/signup.html')

def Users(request):
    allUsers = User.objects.all()
    for one_user in allUsers:
        print(one_user.username,one_user.email)
    print(allUsers)
    return HttpResponse(allUsers)