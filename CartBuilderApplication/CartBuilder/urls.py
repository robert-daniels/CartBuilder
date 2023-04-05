from django.contrib import admin
from django.urls import path
from . import views
from .views import SearchView

urlpatterns = [
    path('', views.home, name='home'),
    path('search_by_recipe/', views.search, name='search_by_recipe'),
    path('about', views.about, name='about'),
    path('recipes', views.recipes, name="recipes"),
    path('ingredients', views.ingredients, name="ingredients"),
    path('allergies', views.allergies, name="allergies"),
    path('profile/<int:profile_id>/', views.profile, name="profile"),
    path('login', views.login, name='login'),
    path('registration', views.registration, name="registration"),
    path('recipe/<requestedRecipeKey>/', views.recipe, name="recipe")
]
