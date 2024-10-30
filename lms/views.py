from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm  
from lms.forms import *
from django.views.generic import ListView, CreateView , DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
CustomUser = get_user_model()


# Create your views here.
def index(request):
    return render(request, "lms/index.html")


class CustomUserCreate(CreateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = "lms/base_form.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create a User'
        context['button_text'] = 'Create User'
        return context
    

class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "lms/base_form.html"
    success_url = reverse_lazy("student-creation")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create a Student'
        context['button_text'] = 'Create Student'
        return context
    

class InstructorCreate(CreateView):
    model = Instructor
    form_class = InstructorForm
    template_name = "lms/base_form.html"
    success_url = reverse_lazy("instructor-creation")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create a instructor'
        context['button_text'] = 'Create instructor'
        return context
    

class CourseCreate(CreateView):
    model = Course
    form_class = CourseForm
    template_name = "lms/base_form.html"
    success_url = reverse_lazy("course-creation")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create a Course'
        context['button_text'] = 'Create Course'
        return context
    
class StudentListView(ListView):
    model = Student
    template_name = "lms/student_list.html"
    context_object_name = "students"


class InstructorListView(ListView):
    model = Instructor
    template_name = "lms/instructors_list.html"
    context_object_name = "instructors"

class CoursesListView(ListView):
    model = Course
    template_name = "lms/courses_list.html"
    context_object_name = "courses"


class StudentDetails(DetailView):
    model = Student
    template_name = "lms/student_details.html"
    context_object_name = "student"


class InstructorDetails(DetailView):
    model = Instructor
    template_name = "lms/instructor_details.html"
    context_object_name = "instructor"

class CourseDetails(DetailView):
    model = Course
    template_name = "lms/course_details.html"
    context_object_name = "course"



class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentUpdateForm
    template_name = 'lms/student_update.html'
    context_object_name = 'student'
    success_url = reverse_lazy('student-list')

class InstructorUpdateView(UpdateView):
    model = Instructor
    form_class = InstructorUpdateForm
    template_name = "lms/instructor_update.html"
    context_object_name = "instructor"
    success_url =  reverse_lazy('instructor-list')

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseUpdateForm
    template_name = "lms/course_update.html"
    context_object_name = "course"
    success_url  = reverse_lazy("courses-list")

class StudentDelete(DeleteView):
    model = Student
    context_object_name = "student"
    template_name = "lms/student_delete.html"
    success_url = reverse_lazy('student-list')

class InstructorDelete(DeleteView):
    model = Instructor
    success_url = reverse_lazy('instructor-list')

class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('courses-list')

