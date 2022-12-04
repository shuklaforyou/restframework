from django.shortcuts import render
from .models import *
from .serializers import StudentSerializer
from rest_framework.generics import  ListAPIView
 # Create your views here.
from .mypaginations import MyCursorPagination


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyCursorPagination