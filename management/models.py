from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Patient(AbstractUser):
    # Add patient-specific fields here
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name="patient_set",
        related_query_name="patient",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="patient_set",
        related_query_name="patient",
    )
    pass

class Doctor(AbstractUser):
    # Add doctor-specific fields here
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="doctor_set",
        related_query_name="doctor",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="doctor_set",
        related_query_name="doctor",
    )
    pass

class Admin(AbstractUser):
    # Add admin-specific fields here
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="admin_set",
        related_query_name="admin",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="admin_set",
        related_query_name="admin",
    )
    pass
