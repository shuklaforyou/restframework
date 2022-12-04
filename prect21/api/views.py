from .serializers import Studentserialize
from .models import Student
from rest_framework import  viewsets
from rest_framework.authentication import SessionAuthentication
from .custompermissions import Mypermission

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserialize
    authentication_classes = [SessionAuthentication]
    permission_classes = [Mypermission]
