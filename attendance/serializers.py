from rest_framework import serializers
from .models import User, Department, Student, Course, AttendanceLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'type', 'full_name', 'username', 'email', 'password', 'submitted_by', 'updated_at']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'department_name', 'submitted_by', 'updated_at']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'department_id', 'student_class', 'submitted_by', 'updated_at']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'department_id', 'semester', 'class_name', 'lecture_hours', 'submitted_by', 'updated_at']

class AttendanceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceLog
        fields = ['id', 'student_id', 'course_id', 'present', 'submitted_by', 'updated_at']
