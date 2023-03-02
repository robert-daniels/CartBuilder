from django.core.management.base import BaseCommand
from ...models import MockRecipe, MockIngredient, MockAllergicIngredient
from ...models import Ingredient, Recipe, Allergy, Profile, RecipeIngredient


class Command(BaseCommand):
    help = 'Imports recipe data from a CSV file'

    def handle(self, *args, **options):
        pass
