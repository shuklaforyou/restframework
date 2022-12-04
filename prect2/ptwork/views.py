from django.shortcuts import render
from .models import *
from .serializers import Studentserializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def student_detail(request,pk):
    stu = student.objects.get(id=pk)
    serialzer = Studentserializer(stu)
    json_data = JSONRenderer().render(serialzer.data)
    return HttpResponse(json_data,content_type='application/json')

def student_list(request):
    stu = student.objects.all()
    serialzer = Studentserializer(stu,many=True)
    # json_data = JSONRenderer().render(serialzer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serialzer.data ,safe=False)