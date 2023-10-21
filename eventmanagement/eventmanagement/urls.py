from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import CollegeViewSet, StudentViewSet, EventViewSet, CustomUserViewSet

# Create a router for the CustomUserViewSet
user_router = DefaultRouter()
user_router.register(r'users', CustomUserViewSet)

# Combine the routers for colleges, students, events, and users
router = DefaultRouter()
router.register(r'colleges', CollegeViewSet)
router.register(r'students', StudentViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(user_router.urls), name='user'),
]
