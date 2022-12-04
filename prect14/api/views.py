from .models import Student
from .serializers import Studentserialize
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView


class Studentlist(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserialize

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserialize

class StudentRetrive(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserialize

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserialize

class StudentDelete(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserialize

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserialize

class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserialize