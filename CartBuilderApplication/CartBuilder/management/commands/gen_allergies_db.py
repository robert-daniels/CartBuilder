from django.core.management.base import BaseCommand
from collections import Counter
from ...models import MockRecipe, MockAllergicIngredient, TopTenMockAllergicIngredients


class Command(BaseCommand):
    help = 'Generates Mock db with Top 10 Allergies from all MockIngredients'

    def handle(self, *args, **options):
        # Get all recipe ingredients (could be more optimized but hey... it's running once)
        all_recipes = MockRecipe.objects.all()

        # Get count (cumulative) of each ingredient in all recipes
        ingredient_counts = Counter()
        for recipe in all_recipes:
            for ingredient in recipe.m_allergic_ingredients.all():
                if ingredient.m_allergic_ingredient not in ['water', 'salt', 'flour']:
                    ingredient_counts[ingredient] += 1

        # Get top 10 allergic ingredients from Mock db
        top_allergic_ingredients = ingredient_counts.most_common(10)

        # Save to TopTenMockAllergicIngredients db
        for i, (ingredient_name, count) in enumerate(top_allergic_ingredients, start=1):
            # Check if the record already exists in the database
            top_allergic_ingredient, created = TopTenMockAllergicIngredients.objects.get_or_create(
                allergic_ingredient=ingredient_name,
                defaults={
                    'rank': i,
                    'count': count,
                }
            )

            print(f"Allergic Ingredient: {top_allergic_ingredient.allergic_ingredient}")
            print(f"\tRank: #rank={top_allergic_ingredient.rank}")
            print(f"\tCount: count={top_allergic_ingredient.count}")

            if not created:
                top_allergic_ingredient.count = count
                top_allergic_ingredient.save()
