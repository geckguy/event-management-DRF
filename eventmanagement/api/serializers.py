from rest_framework import serializers
from .models import College, Student, Event, CustomUser

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'name', 'college')

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('id', 'code', 'name')