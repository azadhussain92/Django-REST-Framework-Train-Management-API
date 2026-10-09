from django.db import models

# Create your models here.

class  AllTrain(models.Model):
    trainno = models.CharField(max_length=100)
    trainname = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    dest = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    total_seats = models.CharField(max_length=100)
    price= models.CharField(max_length=100)
    food_supply = models.BooleanField()