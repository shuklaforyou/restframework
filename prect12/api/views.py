from .models import Student
from .serializers import Studentserialize
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin



class Studentlsit(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = Studentserialize
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = Studentserialize
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentRetrive(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = Studentserialize
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = Studentserialize
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class StudentDestroy(GenericAPIView,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = Studentserialize
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

