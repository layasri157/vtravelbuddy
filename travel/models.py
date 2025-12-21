from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Destination(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} - {self.location}"

class Ride(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    seats_available = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Booking count property for frontend
    @property
    def bookings_count(self):
        return Booking.objects.filter(ride=self).count()
    
    def __str__(self):
        return f"{self.destination.name} - {self.departure_time}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} booked {self.ride.destination.name}"

class Message(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['timestamp']
    
    def __str__(self):
        return f"{self.sender.username}: {self.message[:30]}"
