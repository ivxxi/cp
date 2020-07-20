from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import render, redirect

urlpatterns=[
    path('',views.landing,name = 'landing'),
    path('passenger/home',views.passenger, name = 'passenger home page'),
    path('passenger/profile',views.pprofile, name = 'passenger profile page'),
    path('passenger/destination',views.pdestination, name = 'passenger pick destination page'),
    path('about',views.about, name = 'about page for app'),
]