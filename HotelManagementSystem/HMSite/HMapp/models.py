from django.db import models

# Create your models here.


class RoomType(models.Model):

    def __str__(self):
        return "{}--{}".format(self.roomTypeID, self.roomTypeName)

    roomTypeID = models.IntegerField(primary_key=True)
    roomTypeName = models.CharField(max_length=100)
    roomTypeImage = models.ImageField(
        default='roomImages/default/', upload_to='roomImages/')
    roomPrice = models.FloatField()


class RoomStatus(models.Model):

    def __str__(self):
        return "{}--{}".format(self.roomStatusID, self.roomStatus)

    roomStatusID = models.IntegerField(primary_key=True)
    roomStatus = models.CharField(max_length=100)


class Room(models.Model):

    def __str__(self):
        return "{}".format(self.roomID)

    roomID = models.IntegerField(primary_key=True)
    roomType = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    roomStatus = models.ForeignKey(RoomStatus, on_delete=models.CASCADE)


class Guest(models.Model):

    def __str__(self):
        return "{}--{}".format(self.guestID, self.guestEmailID)

    guestID = models.IntegerField(primary_key=True)
    guestFirstName = models.CharField(max_length=100)
    guestLastName = models.CharField(max_length=100)
    guestAddess = models.CharField(max_length=100)
    guestEmailID = models.CharField(max_length=100, unique=True)
    guestPhone = models.CharField(max_length=100)
    guestProfileImage = models.ImageField(
        default='profileImage/default/', upload_to='profileImage/')


class Reservation(models.Model):

    def __str__(self):
        return "{}".format(self.reservationID)

    reservationID = models.IntegerField(primary_key=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkINDate = models.DateField()
    checkOutDate = models.DateField()
    noOfAdults = models.IntegerField(default=0)
    noOfChildren = models.IntegerField(default=0)
    totolPrice = models.FloatField(default=0.0)
