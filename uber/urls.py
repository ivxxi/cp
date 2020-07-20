from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path(r'^driver/home',views.landing, name = 'landing'),     path('^$',views.driver, name = 'drivers home page'),
    path(r'^driver/profile',views.dprofile, name = 'driver profile page'),
    path(r'^driver/destination',views.ddestination, name = 'driver pick destination page'),
    path('about',views.about, name = 'about page for app'),
] 