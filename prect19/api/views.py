from .serializers import Studentserialize
from .models import Student
from rest_framework import  viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserialize
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    # use any one eithor this IsAuthenticated or AllowAny or
    # permission_classes = [AllowAny]
    # use of permission for only special  IsAdminUser is granted by staff user
    # permission_classes = [IsAdminUser]