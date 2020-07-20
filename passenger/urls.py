from django.conf.urls import url
from django.urls import include, path
from .import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns=[
    path('^$',views.landing,name = 'landing'),
]