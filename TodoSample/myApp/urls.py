from django.urls import path
from myApp import views

urlpatterns=[
    path("",views.home),
    path("add-task/",views.addTask)
]