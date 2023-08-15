from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Car(models.Model):
    picture = models.FileField(null=True)
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    car_make = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)
    fuel = models.CharField(max_length=20, null=True)
    dimensions = models.CharField(max_length=50, null=True)
    transmission = models.CharField(max_length=100, null=True)
    gears = models.IntegerField(null=True)
    seats = models.IntegerField(null=True)
    power = models.IntegerField(null=True)
    tank_capacity = models.IntegerField(null=True)
    engine_displacement = models.IntegerField(null=True)
    added_by = models.ForeignKey(User, on_delete=None, null=True)
    description = models.TextField()

    def __str__(self):
        return self.brand + " " + self.name


class TestDrive(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    time = models.DateField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' - ' + self.car.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    address = models.TextField()
    approved_by = models.ForeignKey(User, on_delete=None, null=True, related_name='approved_by_user')
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' - ' + self.car.name


# class Price(models.Model):
#     brand = models.CharField(max_length=100)
#     fueltype = models.CharField(max_length=20, null=True)
#     powerBHP = models.FloatField(null=True)
#     Numberofyears = models.IntegerField(null=True)
#     mileageKmpl = models.FloatField(null=True)
#     location = models.CharField(max_length=30, null=True)
#     kmdriven=models.IntegerField(null=True)
#     transmission=models.CharField(max_length=20, null=True)
#     ownertype=models.CharField(max_length=20, null=True)
#     engineCC=models.IntegerField(null=True)
#     seats=models.FloatField(null=True)

#     def __str__(self):
#         return self.brand+''+self.fuel+''+self.power+''+self.carbon+''+self.year+''+self.mileage
