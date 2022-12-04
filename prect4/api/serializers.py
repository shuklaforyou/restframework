from rest_framework import serializers
from .models import student


def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('name should be start r')



class studentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100,validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


    def create(self, validate_data):
        return student.objects.create(**validate_data)


    def validate_roll(self, value):
        if value>=200:
            raise serializers.ValidationError('seat full')
        return value

    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='rohit' and ct.lower()!='rachi':
            raise serializers.ValidationError('city must be rachi')
        return data

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
