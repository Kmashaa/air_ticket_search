from django import forms
#from .models import Post
from .models import Flights

class PostForm(forms.Form):
    departure_city=forms.CharField()
    arrival_city=forms.CharField()
    """class Meta:
        model = Flights
        fields = ('departure_city','arrival_city')"""
