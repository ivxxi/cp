from django.db import models
from uber.models import Location
from django.contrib.auth.models import User
# Create your models here.


class Passenger(models.Model):
    name = models.OneToOneField(User, related_name='rider_profile',on_delete=models.CASCADE)
    bio = models.CharField(max_length=60)
    avatar = models.ImageField(upload_to='ProfilePicture/')
    current_location = models.ForeignKey('uber.Location', related_name='current_location', on_delete=models.CASCADE, null=True)
    pickup_location = models.ForeignKey('uber.Location',related_name='rider_pickup', on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=50)


    def __str__(self):
        return self.user.username 
