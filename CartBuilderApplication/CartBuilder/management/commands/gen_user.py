import random
from django.core.management.base import BaseCommand
from ...models import MockRecipe, RecipeFavorite, RecipePersonal, Recipe
from ...factory import ProfileFactory, AllergyFactory, RecipeFactory


class Command(BaseCommand):
    help = 'Imports recipe data from a CSV file'

    def handle(self, *args, **options):
        # Create a new Profile object with add_allergies keyword argument
        profile = ProfileFactory.create()

        # Generate allergy(s) for new Profile
        allergies = AllergyFactory.create_batch(3)
        profile.allergies.set(allergies)
        profile.save()

        # Generate personal recipes for profile
        personal_recipes = []
        for i in range(random.randint(2, 5)):
            recipe = RecipeFactory.create()
            personal_recipes.append(recipe)
            RecipePersonal.objects.create(profile=profile, recipe=recipe)
        profile.personal_recipes.set(personal_recipes)
        profile.save()

        # Select other profile's recipes as favorites
        favorite_recipes = Recipe.objects.exclude(profile=profile).order_by('?')[:random.randint(1, 5)]
        profile.favorite_recipes.set(favorite_recipes)
        profile.save()

        # Create RecipeFavorite objects for personal and favorite recipes
        for recipe in personal_recipes:
            RecipeFavorite.objects.create(profile=profile, recipe=recipe)
        for recipe in favorite_recipes:
            RecipeFavorite.objects.create(profile=profile, recipe=recipe)

