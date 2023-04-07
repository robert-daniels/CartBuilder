from django.shortcuts import render, redirect
from .models import Ingredient, Recipe, Allergy, Profile, RecipeIngredient, SimpleMaster
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Recipe
from django.shortcuts import render, get_object_or_404
import random
from django.contrib import messages


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
    # Get all recipeKeys from the SimpleMaster model
    recipe_keys = SimpleMaster.objects.values_list('recipeKey', flat=True)

    # Select a random recipeKey
    random_key = random.choice(recipe_keys)

    # Retrieve the recipe with the selected recipeKey
    random_recipe = SimpleMaster.objects.get(recipeKey=random_key)

    context = {'random_recipe': random_recipe}

    return render(request, 'home.html', context)


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
    searchTerm = request.GET.get('query', '')
    searchResults = SimpleMaster.objects.filter(recipeNER__contains=searchTerm).values()
    context = {'searchResults': searchResults, 'query': searchTerm}
    return render(request, 'search.html', context)


def add_recipe(request):
    if request.method == 'POST':
        recipe_title = request.POST['recipeTitle']
        recipe_ingredients = request.POST['recipeIngredients']
        recipe_directions = request.POST['recipeDirections']
        recipe_ner = request.POST['recipeNER']

        # our Mock data ends at 500. (hopefully no collisions, this isn't perfect)
        random_key = random.randint(501, 10000000000)

        new_recipe = SimpleMaster(
            recipeKey=random_key,
            recipeTitle=recipe_title,
            recipeIngredients=recipe_ingredients,
            recipeDirections=recipe_directions,
            recipeNER=recipe_ner
        )
        new_recipe.save()

        print("Recipe saved")

        messages.success(request, "Recipe added successfully!")
        return redirect('/cartbuilder')

    return render(request, 'add_recipe.html')


def ingredients(request):
    return render(request, 'ingredients.html')


def allergies(request):
    return render(request, 'allergies.html')


def profile(request, profile_id):
    # Retrieve the Profile object
    profile_obj = Profile.objects.get().all()
    profile_id = profile_obj.id

    # Pass the profile_id to the template context
    context = {'profile_id': profile_id}

    # CAN NOT FIND THE STATIC ASSETS in templates folder?
    return render(request, 'profile.html', context)


def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registration.html')
