from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, StudentViewSet, CourseViewSet, DepartmentViewSet, AttendanceLogViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'attendance', AttendanceLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
