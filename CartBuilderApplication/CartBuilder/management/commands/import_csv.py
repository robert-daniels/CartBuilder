import csv
import os
from django.core.management.base import BaseCommand
from ...models import MockRecipe, MockIngredient, MockAllergicIngredient


class Command(BaseCommand):
    help = 'Imports recipe data from a CSV file'

    def handle(self, *args, **options):
        csv_file = os.path.join(os.getcwd(), 'recipe_ingredients.csv')
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip header row
            for row in reader:
                print('-----')

                # strip newline characters, double quotes, and brackets from csv
                row = [cell.replace('\n', '').replace('[', '').replace(']', '').replace('"', '') for cell in row]
                print('\n')

                recipe_name = row[1]
                print("Recipe Name: ", recipe_name)

                # Create a new recipe object
                recipe = MockRecipe.objects.create(m_recipe_name=recipe_name)

                ingredient_names = row[2].split(', ')

                for ingredient_name in ingredient_names:
                    ingredient, created = MockIngredient.objects.get_or_create(
                        m_ingredient_name=ingredient_name
                    )
                    recipe.m_ingredients.add(ingredient)

                    print("Ingredient: ", ingredient_name)

                print('\n')

                allergic_ingredient_names = row[6].split(', ')
                for allergic_ingredient_name in allergic_ingredient_names:
                    allergic_ingredient, created = MockAllergicIngredient.objects.get_or_create(
                        m_allergic_ingredient=allergic_ingredient_name
                    )
                    recipe.m_allergic_ingredients.add(allergic_ingredient)

                    print(allergic_ingredient_name)

                # save recipe to db:
                recipe.save()

                print('\n')
