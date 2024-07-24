from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/add/', views.add_course, name='add_course'),
    path('courses/confirm_delete/<int:course_id>/', views.confirm_delete_course, name='confirm_delete_course'),
    path('courses/destroy/<int:course_id>/', views.delete_course, name='delete_course'),
]
