from django.db import models

# Create your models here.

class Car(models.Model):
    car_name=models.CharField(max_length=200)
    speed=models.IntegerField(default=50)


    def __str__(self):
        return self.car_name
    

class Employees(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    address=models.TextField()
    phone=models.IntegerField()

    def __str__(self):
        return self.name