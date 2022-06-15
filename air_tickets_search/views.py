from django.shortcuts import render,get_object_or_404
from .models import Flights, Tickets, Flights_bought, Profile
from .forms import PostForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
import logging

"""def flight_bought(request, fl):
    flight = get_object_or_404(Flights, id=fl)
    return render(request, 'air_tickets_search/flight_bought.html', { 'flight' : flight })"""

def flight_list(request):
    submitbutton=request.POST.get("submit")
    departurecity=''
    arrivalcity=''
    form=PostForm(request.POST)
    return render(request,'air_tickets_search/flight_list.html',{'form' :form})

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
    if form.is_valid():
        departurecity = form.cleaned_data.get("departure_city")
        arrivalcity = form.cleaned_data.get("arrival_city")
        flights = Flights.objects.filter(departure_city=departurecity, arrival_city=arrivalcity)
    return render(request, 'air_tickets_search/flight_list.html', { 'flights' : flights ,'form' :form})

def flight_list_bought(request):
    user_id = request.user.id
    if request.user.is_superuser:
        flights = Flights_bought.objects.order_by('departure_date')
    else:
        flights = Flights_bought.objects.filter(user=user_id).order_by('departure_date')
    return render(request, 'air_tickets_search/flight_list_bought.html', { 'flights' : flights })



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
                    return render(request, 'air_tickets_search/login_done.html', { 'flights' : flights ,'form' :form})
                else:
                    return render(request, 'air_tickets_search/login.html', { 'form' :form})
            else:
                return render(request, 'air_tickets_search/login.html', { 'form' :form})
    else:
        form = LoginForm()
    return render(request, 'air_tickets_search/login.html', {'form': form})

def logout_view(request):
    logout(request)
    form = PostForm(request.POST)
    flights = Flights.objects.order_by('price')
    return render(request, 'air_tickets_search/logout.html', { 'flights' : flights ,'form' :form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'air_tickets_search/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'air_tickets_search/register.html', {'user_form': user_form})




@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            form = PostForm(request.POST)
            flights = Flights.objects.order_by('price')
            return render(request, 'air_tickets_search/flight_list.html', { 'flights' : flights ,'form' :form})
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'air_tickets_search/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})
    return render(request, 'air_tickets_search/flight_list.html')
