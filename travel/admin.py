from django.contrib import admin
from .models import Destination, Ride, Booking

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'price']

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ['destination', 'user', 'seats_available', 'departure_time']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'ride', 'booking_time']
