from django.contrib import admin
from django.urls import path , include

from lms import views

urlpatterns = [
    path("", views.index, name = "index" ),
    path("user/" , views.CustomUserCreate.as_view(), name = "user-creation"),
    path("student/" , views.StudentCreate.as_view(), name = "student-creation"),
    path("instructor/" , views.InstructorCreate.as_view(), name = "instructor-creation"),
    path("course/" , views.CourseCreate.as_view(), name = "course-creation"),

    path('student-list/', views.StudentListView.as_view(), name='student-list'),  # URL for the student list
    path('instructor-list/', views.InstructorListView.as_view(), name='instructor-list'),  # URL for the student list
    path('courses-list/', views.CoursesListView.as_view(), name='courses-list'),  # URL for the student list

    path("student_details/<int:pk>/", views.StudentDetails.as_view(), name = "student-details"),
    path("instructor_details/<int:pk>/", views.InstructorDetails.as_view(), name = "instructor-details"),
    path("course_details/<int:pk>/", views.CourseDetails.as_view(), name = "course-details"),

    path('student/update/<int:pk>/', views.StudentUpdateView.as_view(), name='student-update'),
    path('instructor/update/<int:pk>/', views.InstructorUpdateView.as_view(), name='instructor-update'),
    path("course_update/<int:pk>/", views.CourseUpdateView.as_view(), name = "course-update"),


    path("student_delete/<int:pk>/", views.StudentDelete.as_view(), name = "student-delete"),
    path("instructor_delete/<int:pk>/", views.InstructorDelete.as_view(), name = "instructor-delete"),
    path("Course_delete/<int:pk>/", views.CourseDelete.as_view(), name = "course-delete"),



]