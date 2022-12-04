from .models import Student
from .serializers import Studentserialize
from rest_framework.generics import GenericAPIView

from  rest_framework.response import Response
from .models import Student
from .serializers import Studentserialize
from rest_framework import status
from rest_framework import viewsets


class StudentViewssets(viewsets.ViewSet):
    def list(self,request):
        print("********list********")
        print("Basename:",self.basename)
        print("Actions:",self.action)
        print("Details:",self.detail)
        print("Name:",self.name)
        print("descriptions:",self.description)
        stu = Student.objects.all()
        serializer = Studentserialize(stu,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        print("********retrieve********")
        print("Basename:", self.basename)
        print("Actions:", self.action)
        print("Details:", self.detail)
        print("Name:", self.name)
        print("descriptions:", self.description)
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = Studentserialize(stu)
            return Response(serializer.data)

    def create(self,request):
        print("********create********")
        print("Basename:", self.basename)
        print("Actions:", self.action)
        print("Details:", self.detail)
        print("Name:", self.name)
        print("descriptions:", self.description)
        serializer = Studentserialize(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        print("********update********")
        print("Basename:", self.basename)
        print("Actions:", self.action)
        print("Details:", self.detail)
        print("Name:", self.name)
        print("descriptions:", self.description)
        id=pk
        stu = Student.objects.get(id=id)
        serializer = Studentserialize(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updataed'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):
        print("********partial_update********")
        print("Basename:", self.basename)
        print("Actions:", self.action)
        print("Details:", self.detail)
        print("Name:", self.name)
        print("descriptions:", self.description)
        id=pk
        stu = Student.objects.get(id=id)
        serializer = Studentserialize(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data is partial updataed'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
        print("********destroy********")
        print("Basename:", self.basename)
        print("Actions:", self.action)
        print("Details:", self.detail)
        print("Name:", self.name)
        print("descriptions:", self.description)
        id=pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'data is deleted'})