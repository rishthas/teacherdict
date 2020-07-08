from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('listTeachers/',views.listTeachers,name='listTeachers'),
    path('teacher/<int:inid>',views.teacher,name='teacher'),
    path('upload/',views.upload,name='upload'),
]