from .serializers import Studentserialize
from .models import Student
from rest_framework import  viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserialize
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # use any one eithor this IsAuthenticated or AllowAny or
    # permission_classes = [AllowAny]
    # use of permission for only special  IsAdminUser is granted by staff user
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]