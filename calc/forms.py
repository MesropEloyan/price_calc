from django import forms
from .models import Trip

class TripForm(forms.ModelForm):

    class Meta:
        model = Trip
        fields = ['departure_point', 'destination_point', 'distance', 'price_for_km','toll_road', 'toll_road_cost']