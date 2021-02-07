from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
class User_Attributes(models.Model):
    SEX = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    date_posted = models.DateTimeField(default=timezone.now)
    details_filled = models.BooleanField(default=False)
    age = models.IntegerField()
    pneumonia = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=1,
        choices=SEX,

    )
    #user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    user = models.IntegerField(default='1')
    obesity = models.BooleanField(default=False)
    breathing = models.BooleanField(default=False)
    pregnant = models.BooleanField(default=False)
    smoker = models.BooleanField(default=False)
    diabetic = models.BooleanField(default=False)
    heart = models.BooleanField(default=False)
    asthma = models.BooleanField(default=False)
    blood = models.BooleanField(default=False)
    others = models.BooleanField(default=False)
    def __str__(self):
        a=User.objects.filter(id=self.user)[0]
        return a.username

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address =  models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    total_Vaccine = models.IntegerField()
    available_Vaccine = models.IntegerField()
    def __str__(self):
        return self.name

class Request_Manager(models.Manager):
    def create_data(self, user,hospital,fulfilled,confirmtime):
        details = self.create(user=user,hospital=hospital,time=datetime.datetime.now(),fulfilled=fulfilled,confirmtime=confirmtime)
        return details

class Request(models.Model):
    user = models.IntegerField()
    hospital = models.IntegerField()
    time = models.DateTimeField()
    fulfilled = models.BooleanField()
    confirmtime = models.CharField(max_length=50)
    objects = Request_Manager()
    def __str__(self):
        a=User.objects.filter(id=self.user)[0]
        return a.username
