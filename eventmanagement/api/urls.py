from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, CollegeViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'colleges', CollegeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
