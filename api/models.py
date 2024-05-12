from django.db import models

# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=100)
    year=models.IntegerField()
    colour=models.CharField(max_length=100)
    seats=models.IntegerField()
    type=models.CharField(max_length=100)
