import csv
import os
from django.core.management.base import BaseCommand
from CartBuilderApplication.CartBuilder.models import MockIngredient, MockRecipe


class Command(BaseCommand):
    help = 'Imports recipe data from a CSV file'

    def handle(self, *args, **options):
        csv_file = os.path.join(os.getcwd(), 'recipe_ingredients.csv')
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip header row
            for row in reader:
                print('-----')

                # strip newline characters, double quotes ,and brackets from csv
                row = [cell.replace('\n', '').replace('[', '').replace(']', '').replace('"', '') for cell in row]
                print('\n')

                recipe_name = row[1]
                print("Recipe Name: ", recipe_name)

                # Create a new recipe object
                recipe = MockRecipe.objects.create(m_recipe_name=recipe_name)

                ingredient_list = row[2].split(', ')

                for ingredient in ingredient_list:
                    # Check if the ingredient already exists in the database
                    _ingredient, created = MockIngredient.objects.get_or_create(m_ingredient_name=ingredient)

                    # Add the ingredient to the recipe
                    recipe.m_ingredients.add(_ingredient)

                    print("Ingredient: ", ingredient)

                print('\n')

                allergic_ingredients = row[6].split(', ')
                for allergic_ingredient in allergic_ingredients:

                    # Check if the ingredient already exists in the database
                    _allergic_ingredient, _ = MockIngredient.objects.get_or_create(
                        m_allergic_ingredient=allergic_ingredient
                    )

                    # Add each allergic_ingredient to the recipe
                    recipe.m_ingredients.add(allergic_ingredient)

                    print(allergic_ingredient)

                # save m_recipe_name & m_ingredients to db:
                recipe.save()

                print('\n')
