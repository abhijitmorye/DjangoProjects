from django.db import models
import datetime

# Create your models here.

class UserData(models.Model):

    def __str__(self):

        return self.name

    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phn_number = models.CharField(max_length=100)
    profileImage = models.ImageField(default='default..png', upload_to='profile_images/')

class Blogs(models.Model):

    def __str__(self):

        return self.title
    
    title = models.CharField(max_length=100)
    author = models.ForeignKey(UserData, on_delete=models.CASCADE)
    createdOn = models.DateField(default=datetime.datetime.now())
    coverImage = models.ImageField(default='blogdefault.jpg', upload_to='blog_images/')
    content = models.TextField()
