from django.db import models
import datetime

# Create your models here.


class Expenses(models.Model):

    def __str__(self):
        return self.expenseName

    expenseName = models.CharField(max_length=100)
    expenseAmount = models.FloatField()
    expenseCategory = models.CharField(max_length=100)
    expenseDate = models.DateField(default=datetime.datetime.now)
