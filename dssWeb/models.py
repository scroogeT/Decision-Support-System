from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
#from pytz import timezone
from datetime import datetime,timedelta
from django.utils.timezone import get_current_timezone, is_aware

# Create your models here.

class customer(models.Model):
    user = models.OneToOneField(User)
    custID = models.CharField(max_length=30, default='0000000')
    address = models.TextField(blank=True, max_length=200)
    location = models.PointField(srid=4326)
    objects = models.GeoManager()
    #cstomer aknowledge receipt

    def __str__(self):
        return  str(self.user)+ " "+str(self.user.first_name)

class driver(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=15)
    qualifications = models.TextField(max_length=100, blank=True)
    profilePic = models.URLField(blank=True)

    def __str__(self):
        return str(self.user.first_name)+ " "+ str(self.phone)

class distributionPoint(models.Model):
    name = models.CharField(max_length=50)
    location = models.PointField(srid=4326)
    objects = models.GeoManager()
    address = models.TextField(max_length=300)

    def __str__(self):
        return str(self.name)

class truck(models.Model):
    driver = models.ForeignKey(driver)
    name = models.CharField(max_length=20)
    numberPlate = models.CharField(max_length=10)
    tonnage = models.IntegerField(default=0)
    milleage = models.IntegerField(default=0)
    location = models.PointField(srid=4326)
    objects = models.GeoManager()
    isAllocated = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)+ ' '+str(self.numberPlate)

class deliveryState(models.Model):
    state = models.CharField(max_length=10)
    description = models.TextField(max_length=30)

    def __str__(self):
        return str(self.state)

class importedOrders(models.Model):
    custID = models.CharField(max_length=30)
    customerName = models.CharField(max_length=100)
    address = models.CharField(max_length=500, blank=True)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=300, blank=True)
    value = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    charge = models.FloatField(default=0)
    isAssigned = models.BooleanField(default=False)
    isDelivered = models.BooleanField(default=False)
    deliveryStatus = models.ForeignKey(deliveryState, blank=True, default=4)
    isReceived = models.BooleanField(default=False)
    tripNumber = models.IntegerField(blank=True, default=00)
    departingAt = models.CharField(max_length=20, blank=True)
    arrivingAt = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.customerName)+ " " +str(self.custID)


class consignment(models.Model):
    truck = models.ForeignKey(truck, blank=True)
    source = models.ForeignKey(distributionPoint)
    destination = models.ForeignKey(customer)
    description = models.TextField(max_length=300, blank=True)
    value = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    charge = models.FloatField(default=0)
    #departureTime = models.DateTimeField(default=datetime.now())
    #arrivalTime = models.DateTimeField(default=datetime.now())
    departingAt = models.CharField(max_length=20, blank=True)
    arrivingAt = models.CharField(max_length=20, blank=True)
    isAssigned = models.BooleanField(default=False)
    isDelivered = models.BooleanField(default=False)
    deliveryStatus = models.ForeignKey(deliveryState, blank=True)
    isReceived = models.BooleanField(default=False)
    tripNumber = models.IntegerField(blank=True, default=00)

    def __str__(self):
        return str(self.description)+ ' on trip: '+ str(self.tripNumber)
