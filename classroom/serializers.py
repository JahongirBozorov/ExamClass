from rest_framework import serializers

from .models import Student, Teacher, StudentMarks, StudentsInClass, ClassAssignment, SubmitAssignment, User


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMarks
        fields = '__all__'


class StudentsInClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsInClass
        fields = '__all__'


class ClassAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassAssignment
        fields = '__all__'


class SubmitAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitAssignment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
