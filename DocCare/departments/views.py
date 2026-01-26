from django.shortcuts import render,redirect
from departments.models import Department
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def add_Department(request):
    if request.method=="POST":
        department=request.POST["dep"]
        desc=request.POST["description"]
        Department(name=department,description=desc).save()
        messages.info(request,"New department added")
    return render(request,"departments/add_department.html")

def all_department(request):
    dept=Department.objects.all()
    return render(request,"departments/all_department.html",{"departments":dept})

def edit_department(request,dept_id):
    department=Department.objects.get(id=dept_id)
    if request.method=="POST":
        deptmt=request.POST["dep"]
        desc=request.POST["description"]
        department.name=deptmt
        department.description=desc
        department.save()
        return redirect("departments:list_dep")
    dept=Department.objects.get(id=dept_id)
    return render(request,"departments/edit_department.html",{"department":dept})


