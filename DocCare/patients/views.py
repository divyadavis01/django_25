from django.shortcuts import render,redirect
from patients.forms import PatientForm
from django.http import HttpResponse
from django.contrib import messages
from patients.models import Patient
# Create your views here.

def add_patients(request):
    if request.method=="POST":
        p_form=PatientForm(request.POST)
        if p_form.is_valid():
            p_form.save()
            messages.info(request,"New Patient Added")
    else:
        p_form=PatientForm()
    return render(request,"patients/add_patients.html",{"pf_form":p_form})

def edit_patient(request,patient_id):
    patient=Patient.objects.get(id=patient_id)
    if request.method=="POST":
        p_form=PatientForm(request.POST,instance=patient)
        if p_form.is_valid():
            p_form.save()
            return redirect("patients:patient_details",patient_id)
    else:
        p_form=PatientForm(instance=patient)
    return render(request,"patients/edit_patient.html",{"pf_form":p_form})

def viewPatient(request,patient_id):
    patient=Patient.objects.get(id=patient_id)
    return render(request,"patients/view_patient.html",{"patient":patient})

def listpatients(request):
    all_patients=Patient.objects.all()
    return render(request,"patients/list_patient.html",{"patients":all_patients})

def deletePatient(request,patient_id):
    patient=Patient.objects.get(id=patient_id)
    patient.delete()
    return redirect("patients:all_patients")