from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method=="POST":
        first_name=request.POST["f_name"]
        last_name=request.POST["l_name"]
        email=request.POST["email"]
        password=request.POST["password"]
        if User.objects.filter(username=email).exists():
            messages.info(request,"Username already exist")
        else:
            user=User.objects.create_user(username=email,first_name=first_name,last_name=last_name,password=password)
            # print(user)
            user.save()
            return redirect("credentials:signin")
    return render(request,"credentials/register.html")

def login(request):
    if request.method=="POST":
        email=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=email,password=password)
        # print(user)
        if user is not None:
            auth.login(request,user)
            return redirect("dashboards:manager_dashboard")
        else:
            messages.info(request,"Invalid Credentials")
    return render(request,"credentials/login.html")

def logout(request):
    auth.logout(request)
    return redirect("credentials:signin")

def home(request):
    return render(request,"credentials/index.html")