from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Destination, Ride, Booking, Message
from .forms import UserRegistrationForm, RideForm

# HOME - Destinations sidebar + recent rides
def home(request):
    destinations = Destination.objects.all()
    available_rides = Ride.objects.filter(seats_available__gt=0).order_by('-created_at')[:5]
    return render(request, 'travel/home.html', {
        'destinations': destinations,
        'available_rides': available_rides
    })

# REGISTER - Form + auto-login
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'✅ Welcome {user.username}! Account created!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'travel/register.html', {'form': form})

# LOGIN - Authentication
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'👋 Welcome back, {user.username}!')
            return redirect('home')
        messages.error(request, '❌ Invalid username or password!')
    return render(request, 'travel/login.html')

# LOGOUT
def user_logout(request):
    logout(request)
    messages.success(request, '👋 Logged out successfully!')
    return redirect('home')

# RIDES LIST - Full search + filters
def rides_list(request):
    rides = Ride.objects.filter(seats_available__gt=0).order_by('-created_at')
    destinations = Destination.objects.all()
    
    # Filter parameters
    query = request.GET.get('q', '')
    destination_filter = request.GET.get('destination', '')
    min_seats = request.GET.get('min_seats', '')
    
    if query:
        rides = rides.filter(
            Q(destination__name__icontains=query) |
            Q(destination__location__icontains=query)
        )
    
    if destination_filter:
        rides = rides.filter(destination__name__icontains=destination_filter)
    
    if min_seats:
        rides = rides.filter(seats_available__gte=int(min_seats))
    
    return render(request, 'travel/rides_list.html', {
        'rides': rides,
        'destinations': destinations,
        'query': query,
        'destination': destination_filter,
        'min_seats': min_seats
    })

# POST RIDE - Form + user assignment
@login_required
def post_ride(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.user = request.user
            ride.save()
            messages.success(request, f'🚙 {ride.destination.name} ride posted successfully!')
            return redirect('my_rides')
    else:
        form = RideForm()
    return render(request, 'travel/post_ride.html', {'form': form})

# BOOK RIDE - Create booking + decrease seats
@login_required
def book_ride(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id, seats_available__gt=0)
    if request.method == 'POST':
        Booking.objects.create(user=request.user, ride=ride)
        ride.seats_available -= 1
        ride.save()
        messages.success(request, f'✅ Booked {ride.destination.name}! Chat with owner.')
        return redirect('my_bookings')
    return render(request, 'travel/book_ride.html', {'ride': ride})

# MY RIDES - User's rides + booking counts
@login_required
def my_rides(request):
    rides = Ride.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'travel/my_rides.html', {'rides': rides})

# MY BOOKINGS - User's bookings
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_time')
    return render(request, 'travel/my_bookings.html', {'bookings': bookings})

# 🚀 NEW: RIDE CHAT (Owner ↔ Passengers)
@login_required
def ride_chat(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id)
    
    # Access control: Only owner OR passengers
    if request.user != ride.user and not Booking.objects.filter(user=request.user, ride=ride).exists():
        messages.error(request, '❌ Access denied! Only ride owner and passengers can chat.')
        return redirect('my_rides')
    
    # Get all messages for this ride
    messages_list = Message.objects.filter(ride=ride).order_by('timestamp')
    
    # Send new message
    if request.method == 'POST':
        message_text = request.POST.get('message', '').strip()
        if message_text:
            Message.objects.create(
                ride=ride,
                sender=request.user,
                message=message_text
            )
            messages.success(request, '✅ Message sent!')
            return redirect('ride_chat', ride_id=ride.id)
        else:
            messages.error(request, '❌ Message cannot be empty!')
    
    return render(request, 'travel/ride_chat.html', {
        'ride': ride,
        'messages': messages_list
    })
