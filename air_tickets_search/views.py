from django.shortcuts import render,get_object_or_404
from .models import Flights, Tickets
from django.utils import timezone
from .forms import PostForm

def tickets_list(request,departure_city=None,arrival_city=None):
    flights=Flights.objects.all()
    tickets=Tickets.objects.filter(available=True)
    if departure_city:
        tickets.filter(departure_city=departure_city)
    return render (request, 'air_tickets_search/tickets_list.html',{'departure_city':departure_city,'arriva_city':arrival_city,'tickets':tickets})

def tickets_detail(request,id,departure_city):
    ticket=get_object_or_404(Tickets,id=id,departure_city=departure_city,available=True)
    return render(request,'air_tickets_search/detail.html',{'ticket':ticket})


def flight_list_p(request):
    flights = Flights.objects.order_by('price')
    return render(request, 'air_tickets_search/flight_list.html', { 'flights' : flights })

def flight_list_d(request):
    flights = Flights.objects.order_by('departure_date')
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
    depart_city = ""
    arriv_city = ""
    if request.method =="POST":
        form=PostForm(request.Post)
        if form.is_valid():
            depart_city = request.departure_city
            arriv_city = request.arrival_city
    form = PostForm()
    flights=Flights.objects.filter(departure_city=depart_city, arrival_city=arriv_city)
    return render(request, 'air_tickets_search/flight_search.html', {'form': form})


def hren(request):
    return render(request, 'air_tickets_search/hren.html',{})

def flight_detail(request, fl):
    flight = get_object_or_404(Flights, id=fl)
    return render(request, 'air_tickets_search/flight_detail.html', {'flight': flight})