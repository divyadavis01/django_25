from django.urls import path
from myapp import views

urlpatterns=[
    path("",views.home,name="index"),
    path("add-task/",views.addTask,name="add_task"),
    path("edit-task/<int:task_id>",views.editTask,name="edit_task"),
    path("delete-task/<int:task_id>",views.deletetask,name="delete_task")
    
]
