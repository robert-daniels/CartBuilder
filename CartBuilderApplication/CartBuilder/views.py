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
    ####
    # for food_for_thought_card.html
    recipe_keys = SimpleMaster.objects.values_list('recipeKey', flat=True)

    random_key = random.choice(recipe_keys)

    random_recipe = SimpleMaster.objects.get(recipeKey=random_key)

    ####
    # for review_cards.html
    reviews = [
        {
            'review': "I've been using Recipe Box for a few weeks now and it has truly transformed my cooking "
                      "experience! The variety of recipes available is impressive, and I love the user-friendly "
                      "interface. Adding my own recipes to the platform has been a breeze.",
            'name': "Jonathan"
        },
        {
            'review': "Recipe Box has become my go-to app when meal planning. The search functionality is fantastic, "
                      "allowing me to find recipes based on specific ingredients or dietary restrictions. The "
                      "step-by-step instructions are clear and concise, which has helped me improve my culinary "
                      "skills tremendously.",
            'name': "Susan"
        },
        {
            'review': "I'm a busy mom, and Recipe Box has been a game-changer for me. The allergy information is a "
                      "great feature for my family since my son has a nut allergy. I've recommended Recipe Box to all "
                      "my friends!",
            'name': "Jill"
        },
        {
            'review': "As a beginner in the kitchen, I was initially overwhelmed with the thought of cooking. "
                      "Recipe Box has made it so much easier for me to learn and gain confidence. "
                      "The app has a great selection of beginner-friendly recipes, and the instructional videos are "
                      "incredibly helpful.",
            'name': "Tod"
        }
    ]

    # Select a random review from the list
    selected_review = random.choice(reviews)

    # Pass the selected review to your template
    context = {'selected_review': selected_review, 'random_recipe': random_recipe}

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


def random_review(request):
    reviews = [
        "I've been using Recipe Box for a few weeks now and it has truly transformed my cooking experience! "
        "The variety of recipes available is impressive, and I love the user-friendly interface. Adding my own recipes "
        "to the platform has been a breeze.",
        "Recipe Box has become my go-to app when meal planning. The search functionality is fantastic, "
        "allowing me to find recipes based on specific ingredients or dietary restrictions. The step-by-step "
        "instructions are clear and concise, which has helped me improve my culinary skills tremendously.",
        "I'm a busy mom, and Recipe Box has been a game-changer for me. The allergy information is a great feature for "
        "my family since my son has a nut allergy. I've recommended Recipe Box to all my friends!",
        "As a beginner in the kitchen, I was initially overwhelmed with the thought of cooking. "
        "Recipe Box has made it so much easier for me to learn and gain confidence. "
        "The app has a great selection of beginner-friendly recipes, and the instructional videos are incredibly "
        "helpful."
    ]

    # Select a random review from the list
    selected_review = random.choice(reviews)

    # Pass the selected review to your template
    context = {'selected_review': selected_review}
    return render(request, 'random_review.html', context)


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
