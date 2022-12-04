from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import Studentserializer
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from rest_framework.filters import SearchFilter

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    filter_backends = [SearchFilter]
    # filterset_fields= ['city']

    # search_fields= ['name','city']
    search_fields= ['^name',]
