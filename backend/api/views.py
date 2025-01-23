from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["healthcare"]
collection_patient = db["patients"]
collection_doctor = db["doctors"]
collection_admin = db["admins"]


@api_view(['GET'])
def home(request):
    return Response({
        "message": "Hello, World!",
    }, status=status.HTTP_200_OK)

@api_view(['POST'])
def signup(request):
    try:
        print(request.data)
        data = request.data
        if data['role'] == 'patient':
            if collection_patient.find_one({'username': data['username'],'email': data['email']}):
                return Response({
                    "message": "Username and email already exists",
                }, status=status.HTTP_400_BAD_REQUEST)
            collection_patient.insert_one(data)
        elif data['role'] == 'doctor':
            if collection_doctor.find_one({'username': data['username'],'email': data['email']}):
                return Response({
                    "message": "Username and email already exists",
                }, status=status.HTTP_400_BAD_REQUEST)
            collection_doctor.insert_one(data)
        elif data['role'] == 'admin':
            if collection_admin.find_one({'username': data['username'],'email': data['email']}):
                return Response({
                    "message": "Username and email already exists",
                }, status=status.HTTP_400_BAD_REQUEST)
            collection_admin.insert_one(data)
        else:
            return Response({
                "message": "Invalid role",
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "message": "Signup successful",
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": str(e),
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    try:
        data = request.data
        if data['role'] == 'patient':
            result = collection_patient.find_one(data)
        elif data['role'] == 'doctor':
            result = collection_doctor.find_one(data)
        elif data['role'] == 'admin':
            result = collection_admin.find_one(data)
        else:
            return Response({
                "message": "Invalid role",
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if result:
            return Response({
                "message": "Login successful",
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "message": "Invalid credentials",
            }, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({
            "message": str(e),
        }, status=status.HTTP_400_BAD_REQUEST)



