from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import DriverRegistrationForm, RideForm
from django.contrib.auth.decorators import login_required
from datetime import datetime  # Import datetime module
from .models import Ride

def home(request):
    # Add any necessary context data here
    context = {
        # Add context variables if needed
    }
    return render(request, 'homepage.html', context)

@login_required
def dashboard(request):
    # Get the current user
    user = request.user
    
    # Get upcoming rides for the user
    upcoming_rides = Ride.objects.filter(passengers=user.userprofile).filter(date_time__gte=datetime.now())

    return render(request, 'dashboard.html', {'user': user, 'upcoming_rides': upcoming_rides})

def register(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after successful registration
    else:
        form = RideForm()
    return render(request, 'homepage.html', {'form': form})

def driver_registration(request):
    if request.method == 'POST':
        form = DriverRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after successful registration
    else:
        form = DriverRegistrationForm()
    return render(request, 'driver_registration.html', {'form': form})

