from .serializers import Studentserialize
from .models import Student
from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserialize
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
