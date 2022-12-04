from .serializers import Studentserialize
from .models import Student
from rest_framework import  viewsets

class StudentModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserialize