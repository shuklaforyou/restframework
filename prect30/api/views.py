from .serializers import Studentserialize
from .models import Student
from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from .throttling import JackRateThrottle

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserialize
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle,JackRateThrottle]
    throttle_classes = [AnonRateThrottle,UserRateThrottle]
