import io
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from .serializers import studentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from .models import *

# Create your views here.



@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = studentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')


@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data=request.body
        stream= io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not  None:
            stu = student.objects.get(id=id)
            serializer = studentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')

        stu = student.objects.all()
        serializer= studentSerializer(stu,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream=io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = studentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method =='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id = pythondata.get('id')
        stu =student.objects.get(id=id)
        serializer =studentSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data is updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        json_data=request.body
        stream =io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu=student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data is Delete'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(res,safe=False)