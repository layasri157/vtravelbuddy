from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Ride, Destination, Booking, Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user)
        return user

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

class RideSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.name', read_only=True)
    driver_name = serializers.CharField(source='driver.username', read_only=True)
    
    class Meta:
        model = Ride
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    ride_details = serializers.SerializerMethodField()
    
    class Meta:
        model = Booking
        fields = '__all__'
    
    def get_ride_details(self, obj):
        return f"{obj.ride.origin} → {obj.ride.destination.name}"
