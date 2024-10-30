from django.db import models
from django.contrib.auth.models import AbstractUser
# from .models import CustomUser
# from django.contrib.auth import get_user_model
# CustomUser = get_user_model()


# Create your models here.

class CustomUser(AbstractUser):
    pass


# Student should be created 
# Instructor too 
# Course 


class Student(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Instructor(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE,related_name="instructor")
    bio = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name= "courses")
    students = models.ManyToManyField(Student, related_name="courses" )


    def __str__(self):
        return self.name
    
