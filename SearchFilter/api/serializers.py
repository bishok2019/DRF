from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name', 'roll', 'city', 'passby']

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