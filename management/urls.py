from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
path('dashboard/', views.dashboard, name='dashboard'),
path('signup/patient/', views.patient_signup, name='patient_signup'),
path('signup/admin/', views.admin_signup, name='admin_signup'),
path('signup/doctor/', views.doctor_signup, name='doctor_signup'),
path('login/patient/', views.patient_login, name='patient_login'),
path('login/doctor/', views.doctor_login, name='doctor_login'),
path('login/admin/', views.admin_login, name='admin_login'),
]