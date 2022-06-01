from django.shortcuts import render
from .models import Flight, Ticket

def flight_list(request):
    flights = Flight.objects.filter().order_by('total_number_of_seats')
    return render(request, 'air_tickets_search/flight_list.html', {'flights'= flights})
