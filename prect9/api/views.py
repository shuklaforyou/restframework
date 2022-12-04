from django.shortcuts import render
from rest_framework import serializers
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Studentserialize
# Create your views here.


@api_view(['GET','POST','PUT','DELETE'])
def student_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
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
            return Response({'msg':'Data is created'})
        return Response(serializer.errors)

    if request.method ==  'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = Studentserialize(stu ,data= request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data is updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id =request.data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data is deleted'})

