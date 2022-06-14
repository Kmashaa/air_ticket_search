from django.urls import path
from . import views


urlpatterns = [
    path('', views.flight_list_p, name='flight_list_p'),
    path('d', views.flight_list_d, name='flight_list_d'),
    path('p', views.flight_list_p, name='flight_list_p'),
    path('b', views.flight_list_bought, name='flight_list_bought'),
    #path('init', views.flight_search, name='flight_search'),
    path('flight/new/', views.flight_new, name='flight_new'),
    path('flight/<int:fl>/', views.flight_detail, name='flight_detail'),
    #path('sign-in/', LoginPage.as_view(), name='sign-in'),
    path('login/', views.user_login, name='login'),
]