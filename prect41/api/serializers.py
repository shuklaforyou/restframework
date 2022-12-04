from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id','url','name','roll','city']