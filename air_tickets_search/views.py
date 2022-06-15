from django.shortcuts import render,get_object_or_404
from .models import Flights, Tickets, Flights_bought
from .forms import PostForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def tickets_list(request,departure_city=None,arrival_city=None):
    flights=Flights.objects.all()
    tickets=Tickets.objects.filter(available=True)
    if departure_city:
        tickets.filter(departure_city=departure_city)
    return render (request, 'air_tickets_search/tickets_list.html',{'departure_city':departure_city,'arriva_city':arrival_city,'tickets':tickets})

def tickets_detail(request,id,departure_city):
    ticket=get_object_or_404(Tickets,id=id,departure_city=departure_city,available=True)
    return render(request,'air_tickets_search/detail.html',{'ticket':ticket})

def flight_bought(request, fl):
    flight = get_object_or_404(Flights, id=fl)
    return render(request, 'air_tickets_search/flight_bought.html', { 'flight' : flight })

def flight_list_p(request):
    submitbutton=request.POST.get("submit")
    departurecity=''
    arrivalcity=''
    form=PostForm(request.POST)
    flights = Flights.objects.order_by('price')
    if form.is_valid():
        departurecity=form.cleaned_data.get("departure_city")
        arrivalcity=form.cleaned_data.get("arrival_city")
        flights = Flights.objects.filter(departure_city=departurecity,arrival_city=arrivalcity)
    return render(request,'air_tickets_search/flight_list.html',{'form' :form, 'departure_city': departurecity,'arrival_city':arrivalcity,'flights':flights})

def flight_list_d(request):
    submitbutton = request.POST.get("submit")
    departurecity = ''
    arrivalcity = ''
    form = PostForm(request.POST)
    flights = Flights.objects.order_by('departure_date')
    return render(request, 'air_tickets_search/flight_list.html', { 'flights' : flights ,'form' :form})

def flight_list_bought(request):
    user_id = request.user.id
    if request.user.is_superuser:
        flights = Flights_bought.objects.order_by('departure_date')
    else:
        flights = Flights_bought.objects.filter(user=user_id).order_by('departure_date')
    return render(request, 'air_tickets_search/flight_list_bought.html', { 'flights' : flights })

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
    flights = Flights.objects.filter(departure_city=depart_city)
    return render(request, 'air_tickets_search/City_selection.html', {'form':form,'flights':flights})


def hren(request):
    return render(request, 'air_tickets_search/hren.html',{})

def flight_detail(request, fl):
    flight = get_object_or_404(Flights, id=fl)
    flight_bought=Flights_bought.objects.create(id=fl,
                                                aviacompany=flight.aviacompany,
                                                departure_city=flight.departure_city,
                                                arrival_city=flight.arrival_city,
                                                departure_date=flight.departure_date,
                                                arrival_date=flight.arrival_date,
                                                price=flight.price,
                                                user_id=request.user.id
                                                )
    flight.delete()
    return render(request, 'air_tickets_search/flight_detail.html', {'flight': flight_bought})



"""class LoginPage(LoginView):
    
    template_name = 'login/sign_in.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def form_invalid(self, form):
        return render(self.request, 'login/sign_in_error.html')

    def get_success_url(self):
        return render(self.request, 'air_tickets_search/flight_list.html')"""
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    form = PostForm(request.POST)
                    flights = Flights.objects.order_by('price')
                    return render(request, 'air_tickets_search/flight_list.html', { 'flights' : flights ,'form' :form})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'air_tickets_search/login.html', {'form': form})

def logout_view(request):
    logout(request)
    form = PostForm(request.POST)
    flights = Flights.objects.order_by('price')
    return render(request, 'air_tickets_search/flight_list.html', { 'flights' : flights ,'form' :form})

"""@login_required
def dashboard(request):
    return render(request, 'air_tickets_search/flight_list.html')"""