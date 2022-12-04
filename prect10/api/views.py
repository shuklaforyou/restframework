from django.shortcuts import render
from rest_framework import serializers
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Studentserialize
from rest_framework import status
# Create your views here.


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request,pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializers = Studentserialize(stu)
            return Response(serializers.data)
        stu = Student.objects.all()
        serializers = Studentserialize(stu,many=True)
        return Response(serializers.data)

    if request.method == 'POST':
        serializer = Studentserialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data is created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method ==  'PUT':
        id = pk
        stu = Student.objects.get(id=id)
        serializer = Studentserialize(stu ,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' complete data is updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method ==  'PATCH':
        id = pk
        stu = Student.objects.get(id=id)
        serializer = Studentserialize(stu ,data= request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' partial data is updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id =pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data is deleted'})

