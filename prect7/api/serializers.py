from rest_framework import serializers
from .models import student



class studentSerializer(serializers.ModelSerializer):
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('name should be start r')

    name=serializers.CharField(validators=[start_with_r])
    class Meta:
        model=student
        fields=['name','roll','city']
        #read_only_fields=['name','roll']
        # extra_kwargs={'name':{'read_only':True}}

    # def create(self, validate_data):
    #     return student.objects.create(**validate_data)


    def validate_roll(self, value):
        if value>=200:
            raise serializers.ValidationError('seat full')
        return value

    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower() == 'veeru' and ct.lower() != 'rachi':
            raise serializers.ValidationError('city must be rachi')
        return data
    #
    # def update(self, instance, validated_data):
    #     print(instance.name)
    #     instance.name = validated_data.get('name',instance.name)
    #     print(instance.name)
    #     instance.roll = validated_data.get('roll',instance.roll)
    #     instance.city = validated_data.get('city',instance.city)
    #     instance.save()



