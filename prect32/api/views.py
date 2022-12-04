from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import Studentserializer
from .models import *
# Create your views here.


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)