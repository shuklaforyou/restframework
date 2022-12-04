from rest_framework import serializers
from .models import *


class Studentserialize(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =['id','name','roll','city']