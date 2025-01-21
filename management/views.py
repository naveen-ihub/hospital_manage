from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import PatientSignUpForm, AdminSignUpForm, DoctorSignUpForm
from .models import Patient, Admin, Doctor
from .mongo_client import users_collection, admins_collection, doctors_collection

def index(request):
    return render(request, 'management/index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  
            else:
                return render(request, 'management/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'management/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index') 

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'management/dashboard.html')
    else:
        return redirect('login')

def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            users_collection.insert_one({
                "username": user.username,
                "password":user.password,
                "email": user.email,
                "phone_number": user.phone_number,
                "role": "patient"
            })
            return redirect('patient_login')
    else:
        form = PatientSignUpForm()
    return render(request, 'management/signup.html', {'form': form, 'user_type': 'patient'})

def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            doctors_collection.insert_one({
                "username": user.username,
                "password":user.password,
                "email": user.email,
                "phone_number": user.phone_number,
                "role": "Doctor"
            })
            return redirect('doctor_login')
    else:
        form = DoctorSignUpForm()
    return render(request, 'management/signup.html', {'form': form, 'user_type': 'doctor'})

def admin_signup(request):
    if request.method == 'POST':
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            admins_collection.insert_one({
                "username": user.username,
                "password":user.password,
                "email": user.email,
                "phone_number": user.phone_number,
                "role": "Admin"
            })
            return redirect('admin_login')
    else:
        form = AdminSignUpForm()
    return render(request, 'management/signup.html', {'form': form, 'user_type': 'admin'})

def patient_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and isinstance(user, Patient):
                login(request, user)
                print("Login successful")
                return redirect('dashboard')
            else:
                return render(request, 'management/login.html', {'form': form, 'error': 'Invalid credentials', 'user_type': 'patient'})
    else:
        form = AuthenticationForm()
    return render(request, 'management/login.html', {'form': form, 'user_type': 'patient'})

def doctor_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and isinstance(user, Doctor):
                login(request, user)
                print("Login successful")
                return redirect('dashboard')
            else:
                return render(request, 'management/login.html', {'form': form, 'error': 'Invalid credentials', 'user_type': 'doctor'})
    else:
        form = AuthenticationForm()
    return render(request, 'management/login.html', {'form': form, 'user_type': 'doctor'})

def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and isinstance(user, Admin):
                login(request, user)
                print("Login successful")
                return redirect('dashboard')
            else:
                return render(request, 'management/login.html', {'form': form, 'error': 'Invalid credentials', 'user_type': 'admin'})
    else:
        form = AuthenticationForm()
    return render(request, 'management/login.html', {'form': form, 'user_type': 'admin'})