from django.urls import path
from doctors import views

app_name="doctors"
urlpatterns=[
    path("add-doctor",views.addDoctor,name="add_doctor"),
    path("list-doctor",views.listDoctors,name="list_doctor"),
    path("edit-doctor/<int:dr_id>",views.editDoctor,name="edit_doctor")
]

