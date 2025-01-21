from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Patient, Admin, Doctor
from .mongo_client import users_collection, admins_collection, doctors_collection

class MongoDBBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        # Check in Patient collection
        patient_data = users_collection.find_one({"username": username})
        if patient_data and check_password(password, patient_data['password']):
            patient = Patient(username=username)
            patient.password = patient_data['password']
            return patient

        # Check in Doctor collection
        doctor_data = doctors_collection.find_one({"username": username})
        if doctor_data and check_password(password, doctor_data['password']):
            doctor = Doctor(username=username)
            doctor.password = doctor_data['password']
            return doctor

        # Check in Admin collection
        admin_data = admins_collection.find_one({"username": username})
        if admin_data and check_password(password, admin_data['password']):
            admin = Admin(username=username)
            admin.password = admin_data['password']
            return admin

        return None

    def get_user(self, user_id):
        try:
            # Check in Patient collection
            patient_data = users_collection.find_one({"username": user_id})
            if patient_data:
                patient = Patient(username=user_id)
                patient.password = patient_data['password']
                return patient

            # Check in Doctor collection
            doctor_data = doctors_collection.find_one({"username": user_id})
            if doctor_data:
                doctor = Doctor(username=user_id)
                doctor.password = doctor_data['password']
                return doctor

            # Check in Admin collection
            admin_data = admins_collection.find_one({"username": user_id})
            if admin_data:
                admin = Admin(username=user_id)
                admin.password = admin_data['password']
                return admin
        except Exception:
            return None
        return None 