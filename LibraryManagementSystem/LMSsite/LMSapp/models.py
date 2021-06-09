from django.db import models

# Create your models here.


class Students(models.Model):

    def __str__(self):
        return self.studentName

    studentID = models.IntegerField(primary_key=True)
    studentName = models.CharField(max_length=100)
    studentEmailID = models.CharField(max_length=100)


class Books(models.Model):

    def __str__(self):
        return self.bookname

    bookID = models.IntegerField(primary_key=True)
    bookname = models.CharField(max_length=100)
    bookPrice = models.FloatField()
    bookState = models.CharField(max_length=100)


class BoorowedBooks(models.Model):

    def __str__(self):
        return str(self.borrowID)

    borrowID = models.IntegerField(primary_key=True)
    stduent = models.ForeignKey(Students, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
