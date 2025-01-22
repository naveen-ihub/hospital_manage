from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def home(request):
    return Response({
        "message": "Hello, World!",
        "status": "API is working"
    }, status=status.HTTP_200_OK)