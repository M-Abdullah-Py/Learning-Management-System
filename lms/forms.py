
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import *

CustomUser = get_user_model()


class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email"]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = "__all__"


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class InstructorUpdateForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = "__all__"

class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"