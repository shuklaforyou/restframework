from .models import Student
from .serializers import Studentserialize
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView
from rest_framework.throttling import ScopedRateThrottle

class Studentlist(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserialize
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserialize
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'

class StudentRetrive(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserialize
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserialize
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'

class StudentDelete(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserialize
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'

# class StudentListCreate(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = Studentserialize
#     throttle_classes = [ScopedRateThrottle]
#
# class StudentRUD(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = Studentserialize
#     throttle_classes = [ScopedRateThrottle]