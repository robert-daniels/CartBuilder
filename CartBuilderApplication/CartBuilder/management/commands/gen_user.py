import random
from django.core.management.base import BaseCommand
from ...models import MockRecipe
from ...factory import ProfileFactory, AllergyFactory, RecipeFactory


class Command(BaseCommand):
    help = 'Imports recipe data from a CSV file'

    def handle(self, *args, **options):
        # Create a new Profile object
        profile = ProfileFactory.create()

        # Generate allergy(s) for new Profile
        allergies = profile.allergies(profile, create=True)
        profile.allergies.set(allergies)

        # Generate personal recipes for profile
        profile.personal_recipes = ProfileFactory.personal_recipes(profile, create=True)

        # Select other profile's recipes as favorites
        profile.favorite_recipes = ProfileFactory.favorite_recipes(profile, create=True)