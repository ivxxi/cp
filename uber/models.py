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
