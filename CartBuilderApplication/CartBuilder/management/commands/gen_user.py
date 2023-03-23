import random
from typing import List
from django.db.models import QuerySet
from django.core.management.base import BaseCommand
from ...factory import ProfileFactory, AllergyFactory, RecipeFactory
from ...models import MockRecipe, RecipeFavorite, RecipePersonal, Recipe, Profile, Allergy


class ProfileBuilder:
    def __init__(self):
        self.profile = ProfileFactory()

    def add_allergies(self, allergies=None):
        if allergies:
            for allergy_name in allergies:
                if allergy_name:
                    allergy, _ = Allergy.objects.get_or_create(allergy_name=allergy_name)
                    self.profile.allergies.add(allergy)
        else:
            allergy = AllergyFactory()
            self.profile.allergies.add(allergy)
        self.profile.save()
        return self

    def add_personal_recipes(self, num_recipes, instructions=None):
        for i in range(num_recipes):
            recipe = RecipeFactory.create_recipe(self.profile, instructions=instructions)
        return self

    def add_favorite_recipes(self, favorite_recipe_names=None):
        if favorite_recipe_names:
            favorites = []
            for recipe_name in favorite_recipe_names:
                recipe = Recipe.objects.filter(recipe_name=recipe_name).first()
                if recipe:
                    favorites.append(recipe)
        else:
            favorites = ProfileFactory.favorite_recipes(self.profile)
        self.profile.favorite_recipes.set(favorites)
        self.profile.save()
        return self

    def get_profile(self):
        return self.profile


class Command(BaseCommand):
    help = 'Generate random recipes'

    def add_arguments(self, parser):
        parser.add_argument('--num_recipes', type=int, default=10, help='Number of recipes to generate')
        parser.add_argument('--allergies', nargs='+', help='List of allergies')
        parser.add_argument('--favorite_recipes', nargs='+', help='List of favorite recipe names')
        parser.add_argument('--instructions', nargs='+', help='List of instructions for personal recipes')


def handle(self, *args, **options):
        num_recipes = options.get('num_recipes', 10)
        allergies = options.get('allergies', [])
        favorite_recipes = options.get('favorite_recipes', [])

        # Create a profile object with the builder pattern
        profile_builder = (
            ProfileBuilder()
            .add_allergies(allergies)
            .add_personal_recipes(num_recipes)
            .add_favorite_recipes(favorite_recipes)
        )
        profile = profile_builder.get_profile()

        # Output success messages
        for allergy in profile.allergies.all():
            self.stdout.write(self.style.SUCCESS(
                f'Allergy: "{allergy.allergy_name}" added to profile "{profile.profile_first_name}" successfully.'
            ))

        for recipe in profile.personal_recipes.all():
            self.stdout.write(self.style.SUCCESS(
                f'Recipe: "{recipe.recipe_name}" created successfully for profile {profile.profile_first_name}'
            ))

        for favorite in profile.favorite_recipes.all():
            self.stdout.write(self.style.SUCCESS(
                f'Favorite Recipe: "{favorite.recipe_name}" added by "{favorite.profile.profile_first_name}" was '
                f'successfully added to {profile.profile_first_name}s Favorites'
            ))
