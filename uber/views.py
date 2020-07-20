from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import url,include
# Create your views here.


def login(request):
    return render(request, "registration/registration_form.html")

def logout(request):
    return render(request, 'registration/registration_form.html')

def landing(request):
    return render(request, 'landingpage/land-page.html')

def dregistration(request):
    return render(request, 'landingpage/land-page.html')


def driver(request):
    return render(request, 'driver/home.html')
