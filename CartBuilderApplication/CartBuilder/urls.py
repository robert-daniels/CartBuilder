from django.contrib import admin
from django.urls import path
from . import views
from .views import SearchView

urlpatterns = [
    path('', views.home, name='home'),
    path('search_by_recipe/', SearchView.as_view(), name='search_by_recipe'),
    path('about', views.about, name='about'),
    path('recipes', views.recipes, name="recipes"),
    path('ingredients', views.ingredients, name="ingredients"),
    path('allergies', views.allergies, name="allergies"),
    path('profile', views.profile, name="profile"),
]
