from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"index.html")

def addTask(request):
    return render(request,"add_task.html")