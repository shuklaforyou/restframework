from .serializers import Studentserialize
from .models import Student
from rest_framework import  viewsets
from .customauth import CustomAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserialize
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
