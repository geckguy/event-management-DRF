from rest_framework import serializers
from .models import College, Student, Event, CustomUser

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('id', 'code', 'name')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'user', 'name', 'roll_number', 'college')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'date', 'college')

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'name', 'college')

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    name = serializers.CharField()
    college = serializers.PrimaryKeyRelatedField(queryset=College.objects.all())
    roll_number = serializers.CharField()

    def create(self, validated_data):
        college = validated_data.pop('college')
        roll_number = validated_data.pop('roll_number')
        user = CustomUser.objects.create(college=college, **validated_data)
        Student.objects.create(user=user, name=validated_data['name'], college=college, roll_number=roll_number)
        return user
