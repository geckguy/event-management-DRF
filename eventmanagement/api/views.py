from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from .models import College, Student, Event, CustomUser
from .serializers import CollegeSerializer, StudentSerializer, EventSerializer, CustomUserSerializer
from .permissions import IsSameCollege

class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        college_id = data.get('college')
        if not (email and password and name and college_id):
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        college = College.objects.get(id=college_id)
        user = CustomUser.objects.create(email=email, password=make_password(password), name=name, college=college)
        return Response(CustomUserSerializer(user).data)

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsSameCollege]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return Event.objects.all()  # Superuser should see all events
            else:
                return Event.objects.filter(college=user.college)
        else:
            return Event.objects.none()  # Return an empty queryset for unauthenticated users



class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
