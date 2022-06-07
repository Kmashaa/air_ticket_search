from django import forms
#from .models import Post
from .models import Flights

class PostForm(forms.ModelForm):

    class Meta:
        model = Flights
        fields = ('departure_city', 'arrival_city')
