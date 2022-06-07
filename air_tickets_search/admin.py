from django.contrib import admin
from .models import Flights, Tickets, Flights_bought
#from .models import Post

#admin.site.register(Post)
admin.site.register(Flights)
admin.site.register(Tickets)
admin.site.register(Flights_bought)