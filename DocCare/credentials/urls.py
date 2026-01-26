from django.urls import path
from credentials import views

app_name="credentials"

urlpatterns=[
    path("register",views.register,name="signup"),
    path("login",views.login,name="signin"),
    path("logout",views.logout,name="signout"),
    path("",views.home,name="home_page")
]