import random
from typing import List
from django.db.models import QuerySet
from django.core.management.base import BaseCommand
from ...factory import ProfileFactory, AllergyFactory, RecipeFactory
from ...models import MockRecipe, RecipeFavorite, RecipePersonal, Recipe, Profile, Allergy


class Command(BaseCommand):
    help: str = 'Command for Generating Users with real data'

    def handle(self, *args: str, **options: str) -> None:
        # Create a new Profile object with add_allergies keyword argument
        profile: Profile = ProfileFactory.create()

        # Generate allergy(s) for new Profile
        allergies: List[Allergy] = AllergyFactory.create_batch(3)
        profile.allergies.set(allergies)
        profile.save()

        # Generate personal recipes for profile
        personal_recipes: List[Recipe] = []
        for i in range(random.randint(2, 5)):
            recipe: Recipe = RecipeFactory.create()
            recipe.profile = profile  # Set the profile field of the Recipe instance
            recipe.save()
            personal_recipes.append(recipe)
            RecipePersonal.objects.create(profile=profile, recipe=recipe)
        profile.personal_recipes.set(personal_recipes)
        profile.save()

        # Select other profile's recipes as favorites
        favorite_recipes: QuerySet[Recipe] = Recipe.objects.exclude(
            profile=profile
        ).order_by('?')[:random.randint(1, 5)]
        profile.favorite_recipes.set(favorite_recipes)
        profile.save()

        # Create RecipeFavorite objects for personal and favorite recipes
        for recipe in personal_recipes:
            RecipeFavorite.objects.create(profile=profile, recipe=recipe)
        for recipe in favorite_recipes:
            RecipeFavorite.objects.create(profile=profile, recipe=recipe)
