from django.contrib import admin
from .models import Flights, Tickets, Flights_bought
from .models import Profile
#from .models import Post

#admin.site.register(Post)
admin.site.register(Flights)
admin.site.register(Tickets)
admin.site.register(Flights_bought)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

admin.site.register(Profile, ProfileAdmin)