from django.urls import path

from . import views 
#url to every page in use within the website
urlpatterns=[
    path("register",views.register, name="register"),
    path("login",views.login, name="login"),
    path("exit",views.exit, name="exit")
]