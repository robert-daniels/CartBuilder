from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
   path('registration', views.register_request, name="registration"),
   path("login", views.login_request, name="login"),
   path("profile", views.profile, name="profile"),
   path('logout', views.logout_user, name='logout'),
]