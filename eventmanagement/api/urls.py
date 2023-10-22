from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, CollegeViewSet, StudentViewSet, EventViewSet, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'colleges', CollegeViewSet)
router.register(r'students', StudentViewSet)
router.register(r'events', EventViewSet, basename='event')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]
