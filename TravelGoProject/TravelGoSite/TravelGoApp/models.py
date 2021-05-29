from django.db import models

# Create your models here.


class UserData(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    addess = models.CharField(max_length=100)
    profile_image = models.ImageField(
        default='Images/Default/default.png', upload_to='Images/ProfileImage/')


class Flight(models.Model):

    def __str__(self):
        return self.flightName

    flightName = models.CharField(max_length=100)
    flightSource = models.CharField(max_length=100)
    flightDest = models.CharField(max_length=100)
    flightDepartureTime = models.TimeField()
    flightArrivalTime = models.TimeField()
    duration = models.TimeField()
    noOfSeats = models.IntegerField()
    price = models.FloatField()
