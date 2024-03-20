from django.urls import path
from .views import driver_registration
from .views import dashboard
from .views import home
from . import views




urlpatterns = [
    # Your existing URLs
    path('', home, name='home'),
    path('driver_registration/', driver_registration, name='driver_registration'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),



] 
