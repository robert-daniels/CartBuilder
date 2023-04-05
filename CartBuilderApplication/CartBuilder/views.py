from django.shortcuts import render
from .models import Ingredient, Recipe, Allergy, Profile, RecipeIngredient, SimpleMaster
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Recipe


class SearchView(ListView):
    template_name = 'search.html'
    model = Recipe
    context_object_name = 'recipes'
    paginate_by = 10

    # https://docs.djangoproject.com/en/4.1/ref/models/querysets/#icontains
    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return self.model.objects.filter(recipe_name__icontains=query)
        else:
            return Recipe.objects.none()


# Create your views here.
def home(request):
    popular_recipes = Recipe.get_popular_recipes()
    ctx = {'popular_recipes': popular_recipes}
    return render(request, 'home.html', ctx)


def about(request):
    return render(request, 'about.html')


def recipes(request):
    recipe_list = SimpleMaster.objects.all()
    context = {'full_recipe_list': recipe_list}
    return render(request, 'recipes.html', context)

def recipe(request, requestedRecipeKey):
    recipeObject = SimpleMaster.objects.get(recipeKey=requestedRecipeKey)
    context = {'recipe': recipeObject}
    return render(request, 'recipe.html', context)

def search(request):
    searchTerm = request.GET.get('query','')
    searchResults = SimpleMaster.objects.filter(recipeNER__contains=searchTerm).values()
    context = {'searchResults': searchResults, 'query': searchTerm}
    return render(request, 'search.html', context)


def ingredients(request):
    return render(request, 'ingredients.html')


def allergies(request):
    return render(request, 'allergies.html')

def profile(request):
    return render(request, 'profile.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')