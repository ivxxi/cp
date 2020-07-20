from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Driver(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=60)
    avatar = models.ImageField(upload_to='ProfilePicture/')
    vehicle = models.ForeignKey('uber.Car', on_delete=models.CASCADE)
    pickup_location = models.ForeignKey('uber.Location', on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username 


class Car(models.Model):
    car_brand = models.CharField(max_length=50)
    number_plate = models.CharField(max_length=20)
    seat_number = models.CharField(max_length=20)


    def __str__(self):
        return self.user.username 


class Location (models.Model):
    longitude = models.CharField(max_length=10)
    latitude = models.CharField(max_length=10)
    location_name = models.CharField(max_length=20)
    category = models.ForeignKey('uber.Category', on_delete=models.CASCADE)
