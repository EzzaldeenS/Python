from django.db import models
from django.shortcuts import get_object_or_404

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)      


def show_all_courses():
    return Course.objects.all()

def add_course(Izz):
    name = Izz['name']
    description = Izz['description']
    Course.objects.create(name=name, description=description)

def delete_course(course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return course