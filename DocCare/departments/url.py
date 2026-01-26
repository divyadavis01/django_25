from django.urls import path
from departments import views

app_name="departments"

urlpatterns=[
    path("add-department",views.add_Department,name="add_dep"),
    path("all-departments",views.all_department,name="list_dep"),
    path("edit-department/<int:dept_id>",views.edit_department,name="edit_dept")
]
