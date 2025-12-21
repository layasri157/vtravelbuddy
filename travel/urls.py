from django.urls import path
from . import views

urlpatterns = [
    # Home & Authentication
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    # Rides
    path('rides/', views.rides_list, name='rides_list'),
    path('post-ride/', views.post_ride, name='post_ride'),
    path('book-ride/<int:ride_id>/', views.book_ride, name='book_ride'),
    
    # User Dashboard
    path('my-rides/', views.my_rides, name='my_rides'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    
    # 🚀 NEW CHAT FEATURE
    path('chat/<int:ride_id>/', views.ride_chat, name='ride_chat'),
]
