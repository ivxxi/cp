from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^driver/home',views.landing, name = 'landing'),
    url(r'^driver/profile',views.dprofile, name = 'driver profile page'),
    url(r'^driver/destination',views.ddestination, name = 'driver pick destination page'),
] 