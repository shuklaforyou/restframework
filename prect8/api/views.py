from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# @api_view()
# def hello(request):
#     return Response({'msg':'hello world'})


# @api_view(['GET'])
# def hello(request):
#     return Response({'msg':'hello world'})

# @api_view(['POST'])
# def hello(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':'This is post request'})


@api_view(['GET','POST'])
def hello(request):
    if request.method == 'GET':
        return Response({'msg':'This is GET request'})
    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'This is post request','data':request.data})