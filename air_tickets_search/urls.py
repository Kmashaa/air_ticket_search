from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_list_p, name='flight_list_p'),
    path('d', views.flight_list_d, name='flight_list_d'),
    path('p', views.flight_list_p, name='flight_list_p'),
    path('b', views.flight_list_bought, name='flight_list_bought'),
    path('flight/new/', views.flight_new, name='flight_new'),
    path('flight/<int:fl>/', views.flight_detail, name='flight_detail'),
]