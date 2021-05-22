from django.db import models


# Create your models here.
# it is used to create DB rekated stuff

class Book(models.Model):

    def __str__(self):
        return self.name + " : " + self.genre + " : " + str(self.price)

    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    price = models.IntegerField()
    book_image = models.ImageField(default='default.jpg', upload_to='book_images/')
