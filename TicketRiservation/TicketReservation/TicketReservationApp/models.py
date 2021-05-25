from django.db import models


# Create your models here.

class UserData(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    phn_no = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    profile_image = models.ImageField(default='default.png', upload_to='profile_images/')
