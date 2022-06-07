from django.shortcuts import render
from .models import Flights, Tickets
from django.utils import timezone
from .forms import PostForm


def flight_list(request):
    flights = Flights.objects.order_by('price')
    return render(request, 'air_tickets_search/flight_list.html', { 'flights' : flights })

def flight_new(request):
    if request.method =="POST":
        form=PostForm(request.Post)
        if form.is_valid():
            flights=form.save(commit=False)
            flights.aviacompany=request.aviacompany
            flights.departure_city=request.departure_city
            flights.arrival_city = request.arrival_city
            flights.departure_date = request.departure_date
            flights.arrival_date = request.arrival_date
            flights.total_number_of_seats = request.total_number_of_seats
            flights.price = request.price
    form = PostForm()
    return render(request, 'air_tickets_search/flight_edit.html', {'form': form})

def flight_search(request):
    flights=Flights.objects.filter(departure_city=request.departure_city, arrival_city=request.arrival_city)
    return render(request, 'air_tickets_search/flight_search.html', { 'flights' : flights })

def hren(request):
    return render(request, 'air_tickets_search/hren.html',{})