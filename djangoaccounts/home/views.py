import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail
from account import settings
# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return redirect("/login") 
    
    return render(request,"index.html")
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        print(request.user)
        if username and password:
            

            if User.objects.filter(username=username).exists():
                messages.info(request,"The username already taken ")
                return redirect(".")

            elif email and User.objects.filter(email=email).exists():
                messages.info(request,"The email already taken ")
                return redirect(".")

                
            else:
                user=User.objects.create_user(username=username,password=password)
                print(user)
                
                if user is not None:
                    user.first_name=firstname
                    user.last_name=lastname
                    user.email=email
                    messages.success(request,user.username+" succesfully registered")


                    subject="welcome to my website - Django login"
                    message="Hello, "+user.first_name+"!! \n"+"Welcome to mywebsite! \n Thankyou for visiting"
                    from_email=settings.EMAIL_HOST_USER
                    to_list=[user.email]
                    send_mail(subject,message,from_email,to_list,fail_silently=True)
                    return redirect("/")

    return render(request,"register.html")
def loginuser(request):
    if request.method=="POST":
        username=request.POST["username"]
        passwd=request.POST['password']
        
            
        
        user=authenticate(request,username=username,password=passwd)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,"Login successful..")
            return redirect("/")
        else:
            messages.info(request,"The user not found..")
            return render(request,"login.html")
    return render(request,"login.html")
def logoutuser(request):
    logout(request)
    messages.success(request,"Logout successfull..")
    return redirect("/")