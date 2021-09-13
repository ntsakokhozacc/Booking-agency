from django import VERSION
from django.urls import path

from . import views 
#url to every page in use within the website

urlpatterns=[
    path("register",views.register, name="register"),
    path("login",views.login, name="login"),

    #Comment out logotu feature to run the project
    path("logout",views.logout, name="logout")
]