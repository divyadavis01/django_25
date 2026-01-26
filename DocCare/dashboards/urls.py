from django.urls import path
from dashboards import views

app_name="dashboards"

urlpatterns=[
    path("manager-dashboard",views.managerDashboard,name="manager_dashboard"),
]