# from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import sign_up

urlpatterns = [

    path("login/", auth_views.LoginView.as_view(template_name="account/login.html"), name="login"),
    path("signup/", sign_up, name="signup"),

]


