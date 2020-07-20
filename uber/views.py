from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import url,include
# Create your views here.


def login(request):
    return render(request, "registration/registration_form.html")
