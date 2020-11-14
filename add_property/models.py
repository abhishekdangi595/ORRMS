from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    ward_no = models.IntegerField()

    def __str__(self):
        return "%s %s %s" % (self.state, self.district, self.municipality)

class FlatImage(models.Model):
    bedroom_img = models.ImageField(max_length=255, null='True', blank='True')
    kitchen_img = models.ImageField(max_length=255, null='True', blank='True')
    bathroom_img = models.ImageField(max_length=255, null='True', blank='True')
    livingroom_img = models.ImageField(max_length=255, null='True', blank='True')

class RoomImage(models.Model):
    room_img = models.ImageField(max_length=255, null='True', blank='True')


class PropertyRoom(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room_images = models.OneToOneField(RoomImage, on_delete=models.CASCADE)
    price = models.IntegerField()
    size = models.DecimalField(max_digits=5, decimal_places=2)
    water_facility = models.BooleanField(default=False)
    electricity = models.BooleanField(default=False)
    Parking_facility = models.BooleanField(default=False)
    short_description = models.TextField(max_length=500)


class PropertyFlat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    flat_images = models.OneToOneField(FlatImage, on_delete=models.CASCADE)
    price = models.IntegerField()
    bedroom_no = models.IntegerField()
    kitchen_no = models.IntegerField()
    bathroom_no = models.IntegerField()
    livingroom_no = models.IntegerField()
    water_facility = models.BooleanField(default=False)
    electricity = models.BooleanField(default=False)
    Parking_facility = models.BooleanField(default=False)
    short_description = models.TextField(max_length=500)


