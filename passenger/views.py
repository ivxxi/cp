from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.conf.urls.static import static
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def landing(request):
    return render(request, 'landingpage/land-page.html')

def passenger(request):
    return render(request, 'passenger/home.html')

@login_required(login_url='/accounts/login/')
def pprofile(request):
    return render(request, 'passenger/profile.html')

@login_required(login_url='/accounts/login/')
def pdestination(request):
    return render(request, 'passenger/destination.html')

@login_required(login_url='/accounts/login/')
def about(request):
    return render(request, 'uber/about.html')

