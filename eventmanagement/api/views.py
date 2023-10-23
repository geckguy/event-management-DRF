import logging
from django.shortcuts import render
from django.db import IntegrityError
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from .models import College, Student, Event, CustomUser
from .serializers import CollegeSerializer, StudentSerializer, EventSerializer, CustomUserSerializer, RegisterSerializer
from .permissions import IsSameCollege
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)

class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# class RegisterView(APIView):
#     def post(self, request):
#         data = request.data
#         email = data.get('email')
#         password = data.get('password')
#         name = data.get('name')
#         college_id = data.get('college')
#         roll_number = data.get('roll_number')
#         if not (email and password and name and college_id and roll_number):
#             logger.error('All fields are required for registration')
#             return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             college = College.objects.get(id=college_id)
#         except ObjectDoesNotExist:
#             logger.error(f'College with id {college_id} does not exist')
#             return Response({'error': 'Invalid college ID'}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             if Student.objects.filter(roll_number=roll_number).exists():
#                 logger.error(f'Student with roll number {roll_number} already exists')
#                 return Response({'error': 'Student with this roll number already exists'}, status=status.HTTP_400_BAD_REQUEST)
#             user = CustomUser.objects.create(email=email, password=make_password(password), name=name, college=college)
#             Student.objects.create(user=user, name=name, college=college, roll_number=roll_number)
#         except IntegrityError:
#             logger.error(f'User with email {email} already exists')
#             return Response({'error': 'User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)
#         logger.info(f'User registered successfully with email {email}')
#         return Response(CustomUserSerializer(user).data)

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(CustomUserSerializer(user).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsSameCollege]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return Event.objects.all()
            try:
                return Event.objects.filter(college=user.college)
            except College.DoesNotExist:
                logger.error(f'College with id {user.college.id} does not exist')
                return Response({'error': 'Invalid college ID'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Event.objects.none()

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        Student.objects.create(user=user, name=user.name, college=user.college)
