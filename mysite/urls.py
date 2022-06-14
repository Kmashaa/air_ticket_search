"""mysite URL Configuration

[...]
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('air_tickets_search.urls')),
    path(r'^air_tickets_search/', include('air_tickets_search.urls')),
]