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

        # create recipes with RecipeFactory and pass the profile object
        for i in range(num_recipes):
            recipe = RecipeFactory.create_recipe(profile)
            self.stdout.write(self.style.SUCCESS(f'Recipe "{recipe.recipe_name}" created successfully.'))

