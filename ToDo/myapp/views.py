from django.shortcuts import render,redirect
from myapp.models import ToDo
from django.http import HttpResponse

# Create your views here.

def home(request):
    # username="Biya"
    todos=ToDo.objects.all()      # all data are retrived as objects in django
    # print(todos)
    # todos = [
    #     {
    #         "task": "Learn Python",
    #         "is_completed": False,
    #         "date": "2025-01-05"
    #     },
    #     {
    #         "task": "Complete LMS task",
    #         "is_completed": True,
    #         "date": "2025-01-06"
    #     },
    #     {
    #         "task": "Start MiniProject",
    #         "is_completed": False,
    #         "date": "2025-01-10"
    #     }
    # ]
    context={"tasks":todos}
    return render(request,"index.html",context)

def addTask(request):
    if request.method=="POST":
        t=request.POST["task"]
        ToDo(task=t).save()
        return redirect("index")
        # return HttpResponse("New task added")
    return render(request,"add-task.html")

def editTask(request,task_id):
    tasks=ToDo.objects.get(id=task_id)   # retrives row of the selected id
    if request.method=="POST":
        t=request.POST["tk"]
        status=request.POST.get("status",False)
        tasks.task=t
        tasks.is_completed=status
        tasks.save()
        return redirect("index")
    return render(request,"edit-task.html",{"todo":tasks})

def deletetask(request,task_id):
    tasks=ToDo.objects.get(id=task_id)
    tasks.delete()
    return redirect("index")