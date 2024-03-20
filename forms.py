from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import DriverProfile
from django.contrib.auth.models import User
from .models import Ride


class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['source', 'destination', 'date_time']

class DriverRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    car_model = forms.CharField(max_length=255, required=True)
    license_plate = forms.CharField(max_length=20, required=True)
    driving_license = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.password = self.cleaned_data['password']
        if commit:
            user.save()
            # Assuming you have a DriverProfile model associated with the User
            driver_profile = DriverProfile.objects.create(
                user=user,
                car_model=self.cleaned_data['car_model'],
                license_plate=self.cleaned_data['license_plate'],
                driving_license=self.cleaned_data['driving_license']
            )
        return user
 
