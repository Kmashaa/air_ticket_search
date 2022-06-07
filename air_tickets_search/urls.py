from django.urls import path
from . import views

urlpatterns = [
    path('', views.hren, name='hren'),
    path('flight/new/', views.flight_new, name='flight_new'),
]