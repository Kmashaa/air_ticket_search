from django.shortcuts import render
from .models import Flight, Ticket

def flight_list(request):
    return render(request, 'air_tickets_search/flight_list.html', {})
