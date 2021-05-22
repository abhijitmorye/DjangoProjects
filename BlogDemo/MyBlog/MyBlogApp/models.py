from django.db import models

# Create your models here.

class UserData(models.Model):

    def __str__(self):

        return self.name

    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phn_number = models.CharField(max_length=100)
    profileImage = models.ImageField(default='default.jpg', upload_to='profile_images/')
