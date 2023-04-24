from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
   path('registration', views.register_request, name="registration"),
]