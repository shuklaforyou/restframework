from rest_framework import serializers
from .models import *

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =  ['id','name','roll','city','passby']