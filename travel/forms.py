from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ride, Destination

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['destination', 'departure_time', 'seats_available']
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'seats_available': forms.NumberInput(attrs={'min': 1, 'max': 10}),
        }
