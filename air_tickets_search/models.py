from django.conf import settings
from django.db import models
from django.utils import timezone

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


class Flight(models.Model):
    aviacompany = models.CharField(max_length=50)
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    flight_time = models.DateTimeField()
    total_number_of_seats = models.IntegerField()
    reserved_number_of_seats = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.departure_date


class Ticket(models.Model):
    seat = models.IntegerField()
