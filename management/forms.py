from django import forms
from .models import Patient, Admin, Doctor

class PatientSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=20)
    class Meta:
        model = Patient
        fields = ['username', 'password', 'email', 'phone_number'] 

class AdminSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=20)
    class Meta:
        model = Admin
        fields = ['username', 'password', 'email', 'phone_number'] 

class DoctorSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=20)
    class Meta:
        model = Doctor
        fields = ['username', 'password', 'email', 'phone_number'] 