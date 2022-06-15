from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

"""
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
"""
class Flights(models.Model):
    id=models.IntegerField(primary_key=True)
    aviacompany = models.CharField(max_length=50)
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.aviacompany



class Tickets(models.Model):
    seat = models.IntegerField()
    flight = models.ForeignKey(Flights,on_delete=models.CASCADE)

    def __str__(self):
        return self.seat


class Flights_bought(models.Model):
    id=models.IntegerField(primary_key=True)
    aviacompany = models.CharField(max_length=50)
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    price = models.IntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)