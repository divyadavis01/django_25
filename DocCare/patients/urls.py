from django.urls import path
from . import views

app_name="patients"

urlpatterns=[
    path("add-patient",views.add_patients,name="new_patient"),
    path("edit-patient/<int:patient_id>",views.edit_patient,name="edit_patient"),
    path("list-patients",views.listpatients,name="all_patients"),
    path("patient-detail/<int:patient_id>",views.viewPatient,name="patient_details"),
    path("delete-patient/<int:patient_id>",views.deletePatient,name="delete_patient")
]