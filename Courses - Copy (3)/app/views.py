from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .models import Course

def index(request):
    courses = Course.objects.all()
    context = {
        "courses": courses
    }
    return render(request, "index.html", context)

def add_course(request):
    if request.method == 'POST':
        models.add_course(request.POST)
        return redirect('index')
    return render(request, 'add_course.html')

def confirm_delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'delete.html', {'course': course})

def delete_course(request, course_id):
    models.delete_course(course_id)
    return redirect('index')
