from django.shortcuts import render
from django.http import HttpResponse



def landing(request):
    return render(request, 'landingpage/land-page.html')

def passenger(request):
    return render(request, 'passenger/home.html')

def pprofile(request):
    return render(request, 'passenger/profile.html')

def pdestination(request):
    return render(request, 'passenger/destination.html')

def about(request):
    return render(request, 'uber/about.html')