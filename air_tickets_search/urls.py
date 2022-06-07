from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_list, name='flight_list'),
    path('flight/new/', views.flight_new, name='flight_new'),
    path('hren',views.hren,name='hren'),
    path('flight/<int:fl>/', views.flight_detail, name='flight_detail'),
]