from django.shortcuts import render

# Create your views here.
def managerDashboard(request):
    return render(request,"dashboards/manager_dashboard.html")