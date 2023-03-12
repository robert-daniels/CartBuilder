import random
from typing import List
from django.db.models import QuerySet
from django.core.management.base import BaseCommand
from ...factory import ProfileFactory, AllergyFactory, RecipeFactory
from ...models import MockRecipe, RecipeFavorite, RecipePersonal, Recipe, Profile, Allergy


class Command(BaseCommand):
    help = 'Generate random recipes'

    def handle(self, *args, **options):
        num_recipes = options.get('num_recipes', 10)

        # create a profile object with ProfileFactory
        profile = ProfileFactory()

        # generate an allergy for the profile with AllergyFactory
        allergy = AllergyFactory()
        profile.allergies.add(allergy)
        profile.save()

        # Output success message for allergy
        self.stdout.write(self.style.SUCCESS(
            f'Allergy: "{allergy.allergy_name}" added to profile "{profile.profile_first_name}" successfully.'
        ))

        # generate favorite recipes for profile
        favorites = ProfileFactory.favorite_recipes(profile)

        # create recipes with RecipeFactory and pass the profile object
        for i in range(num_recipes):
            recipe = RecipeFactory.create_recipe(profile)
            self.stdout.write(self.style.SUCCESS(
                f'Recipe: "{recipe.recipe_name}" created successfully for profile {profile.profile_first_name}'
            ))

        # Set the favorite_recipes field on the profile instance
        profile.favorite_recipes.set(favorites)
        profile.save()

        # Output success message for each favorite recipe
        for favorite in favorites:
            self.stdout.write(self.style.SUCCESS(
                f'Favorite Recipe: "{favorite.recipe_name}" added by "{favorite.profile.profile_first_name}" was '
                f'successfully added to {profile.profile_first_name}s Favorites'
            ))
