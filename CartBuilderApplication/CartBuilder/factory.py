import factory
import random
from .models import Ingredient, Recipe, Allergy, Profile, RecipeIngredient
from .models import MockRecipe, MockIngredient


class AllergyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Allergy


class IngredientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ingredient


class RecipeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Recipe

    recipe_name = factory.Faker('word')
    date_created = factory.Faker('date_this_year')

    @factory.post_generation
    def ingredients(self, create, extracted, **kwargs):
        if not create:
            # do nothing.
            return

        if extracted:
            for ingredient in extracted:
                self.ingredients.add(ingredient)
        else:
            ingredients = [IngredientFactory() for i in range(random.randint(1, 5))]
            for ingredient in ingredients:
                self.ingredients.add(ingredient)


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    profile_first_name = factory.Faker('first_name')
    profile_last_name = factory.Faker('last_name')

    @factory.post_generation
    def allergies(self, create, extracted, **kwargs):
        if not create:
            # do nothing.
            return

        if extracted:
            for allergy in extracted:
                self.allergies.add(allergy)
        else:
            allergies = [AllergyFactory() for i in range(random.randint(0, 3))]
            for allergy in allergies:
                self.allergies.add(allergy)

    @factory.post_generation
    def personal_recipes(self, create, extracted, **kwargs):
        if not create:
            # do nothing.
            return

        if extracted:
            for recipe in extracted:
                self.personal_recipes.add(recipe)
        else:
            recipes = [RecipeFactory(profile=self) for i in range(random.randint(1, 3))]
            for recipe in recipes:
                recipe_ingredients = RecipeIngredient.objects.select_related('ingredient').filter(recipe=recipe)
                ingredients = [ri.ingredient for ri in recipe_ingredients]
                recipe.ingredients.set(ingredients)
                recipe.save()
                self.personal_recipes.add(recipe)

