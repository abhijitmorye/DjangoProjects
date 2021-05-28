from django.db import models

# Create your models here.


class UserData(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    phn_number = models.IntegerField()
    profile_image = models.ImageField(
        default='Images/default/default.png', upload_to='Images/')
