import factory
from .models import Ingredient, Recipe, Allergy, Profile, RecipeIngredient
from .models import MockCookingInstruction, MockRecipe, MockIngredient, MockRecipeIngredient


class RecipeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Recipe


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    profile_first_name = factory.Faker('first_name')
    profile_last_name = factory.Faker('last_name')