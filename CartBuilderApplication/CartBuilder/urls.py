from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search_by_ingredient/', views.search, name='search_by_ingredient'),
    path('search_by_recipe/', views.search_by_recipe, name='search_by_recipe'),
    path('about', views.about, name='about'),
    path('recipes', views.recipes, name="recipes"),
    path('ingredients', views.ingredients, name="ingredients"),
    path('allergies', views.allergies, name="allergies"),
    path('login', views.login, name='login'),
    path('registration', views.registration, name="registration"),
    path('recipe/<requestedRecipeKey>/', views.recipe, name="recipe"),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
]
