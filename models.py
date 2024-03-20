from django.db import models
from django.contrib.auth.models import User

class DriverProfile(models.Model):
    first_name = models.CharField(max_length=255)  
    last_name = models.CharField(max_length=255)   
    email = models.EmailField(max_length=255)      
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    car_model = models.CharField(max_length=255)
    license_plate = models.CharField(max_length=20)
    driving_license = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional user-related fields as needed

class Ride(models.Model):
    driver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='driver_rides')
    passengers = models.ManyToManyField(UserProfile, related_name='passenger_rides', blank=True)
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    date_time = models.DateTimeField()


