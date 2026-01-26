from django.shortcuts import render,redirect
from django.http import HttpResponse
from doctors.models import Doctor
from departments.models import Department
from django.contrib import messages

# Create your views here.

def addDoctor(request):
    if request.method=="POST":
        d_name=request.POST["name"]
        dep=request.POST["department"]
        dob=request.POST["dob"]
        gender=request.POST["gender"]
        j_date=request.POST["join_date"]
        salary=request.POST["salary"]
        q=request.POST["qualification"]
        about=request.POST["about"]
        pic=request.FILES.get("image",None)
        dep_instance=Department.objects.get(id=dep)

        data={"name":d_name,"department":dep_instance,
               "dob":dob,"gender":gender,
               "join_date":j_date,"salary":salary,
               "qualification":q,"about":about}
        
        if pic is not None:
            data["image"]=pic
        
        Doctor(**data).save()
        messages.info(request,"New Doctor added")
    dep=Department.objects.all()
    return render(request,"doctors/add_doctor.html",{"department":dep})

def listDoctors(request):
    drs=Doctor.objects.all()
    return render(request,"doctors/list_doctors.html",{"doctor":drs})

def editDoctor(request,dr_id):
    dr=Doctor.objects.get(id=dr_id)
    if request.method=="POST":
        d_name=request.POST["name"]
        dep=request.POST["department"]
        dob=request.POST["dob"]
        gender=request.POST["gender"]
        j_date=request.POST["join_date"]
        s=request.POST["salary"]
        q=request.POST["qualification"]
        about=request.POST["about"]
        pic=request.FILES.get("image",None)
        dep_instance=Department.objects.get(id=dep)
        dr.name=d_name
        dr.department=dep_instance
        dr.dob=dob
        dr.gender=gender
        dr.join_date=j_date
        dr.qualification=q
        dr.salary=s
        dr.about=about
        if pic:
            dr.image=pic
        dr.save()
        return redirect("doctors:list_doctor")
     
    dep=Department.objects.all()
    return render(request,"doctors/edit_doctor.html",{"doctor":dr,"departments":dep})
