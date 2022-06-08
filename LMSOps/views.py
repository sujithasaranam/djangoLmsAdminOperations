from django.shortcuts import render

# Create your views here.
import email
import imp
from django.shortcuts import render, redirect 
from django.http import HttpResponseRedirect,HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import *
from operator import itemgetter
from django.contrib import messages
from .serializers import BookSerializer
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

def registerPage(request):
    global p
    if request.method=='POST':
        user=User()
        user.Username=request.POST['username']
        user.email=request.POST['email']
        user.password=request.POST['password']
        user.conformpassword=request.POST['confirm-password']
        p=1
        if user.Username=='' or user.email=='' or user.password=='' or user.conformpassword=='':
            p=0
            messages.add_message(request, messages.WARNING, 'Some fields are empty.Please fill all the fields and click on "Register Now"')
            return redirect('register')

        if user.password!=user.conformpassword:
            p=0
            messages.add_message(request, messages.WARNING, 'Password and confirm Password did not match. Please try again')
            return redirect('register')
        x=User.objects.all()
        for i in x:
            if i.email==user.email:
                messages.add_message(request, messages.WARNING, 'Email already exists.Please try again')
                p=0
        if(p==1):
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Registered Successfully')
            return redirect('login')
    return render(request,'accounts/register.html')
			


def loginPage(request):
    global p2
    if request.method == 'POST':
        email = request.POST['email']
        password =request.POST['password']
        x=User.objects.all()
        for i in x:
            p2=0
            if i.email==email and i.password==password:
                p1=1
                return redirect('addbook')
        if(p2!=1):
            messages.error(request, "Bad Credentials!!")
            return redirect('login')
    
    return render(request, "accounts/login.html")

def addbook(request):
    return HttpResponseRedirect('http://127.0.0.1:8000/api/book/')


def home(request):
    books = Book.objects.all()
    return render(request, 'accounts/home.html', {'books':books})

def logoutUser(request):
	logout(request)
	return redirect('login')





