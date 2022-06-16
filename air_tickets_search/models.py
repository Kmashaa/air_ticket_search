from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Flights(models.Model):
    id=models.IntegerField(primary_key=True)
    aviacompany = models.CharField(max_length=50)
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='flights_liked', blank=True)


    def __str__(self):
        return self.id



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

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)