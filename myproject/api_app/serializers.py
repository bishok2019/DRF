from rest_framework import serializers
from .models import Student

### Regular Serializer
# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length = 100)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length = 100)

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance
    


### Model Seralizer
class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    # city = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['id','name', 'roll', 'city']
        # read_only_fields = ['name', 'roll']
        # extra_kwargs = {'name':{'read_only':True}}

    # Field Level Validation
    def validate_roll(self, data):
        if data >= 201:
            raise serializers.ValidationError('Roll not Available !!')
        return data

    # Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'everest' and ct.lower() != 'solu':
            raise serializers.ValidationError("City must be 'Solu'")
        return data