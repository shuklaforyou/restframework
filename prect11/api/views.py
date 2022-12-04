from django.shortcuts import render
from rest_framework import serializers
from .models import *

from rest_framework.response import Response
from .serializers import Studentserialize
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class studentAPI(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializers = Studentserialize(stu)
            return Response(serializers.data)
        stu = Student.objects.all()
        serializers = Studentserialize(stu, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializer = Studentserialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = Studentserialize(stu ,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' complete data is updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = Studentserialize(stu ,data= request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' partial data is updated'})
        return Response(serializer.errors)

    def delete(self, request, pk=None, format=None):
        id =pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data is deleted'})

