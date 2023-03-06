import random
import factory
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .models import MockRecipe, MockIngredient, MockAllergicIngredient, TopTenMockAllergicIngredients
from .models import Ingredient, Recipe, Allergy, Profile, RecipeIngredient, RecipeFavorite, MockRecipe


class AllergyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Allergy

    @factory.lazy_attribute
    def allergy_name(self):
        top_ten_allergic_ingredients = TopTenMockAllergicIngredients.objects.all()
        if top_ten_allergic_ingredients:
            random_allergic_ingredient = random.choice(top_ten_allergic_ingredients)
            return random_allergic_ingredient.allergic_ingredient.m_allergic_ingredient


class RecipeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Recipe

    date_created = factory.Faker('date_this_year')

    @factory.lazy_attribute
    def recipe_name(self):
        mock_recipe = MockRecipe.objects.order_by('?').first()  # get a random MockRecipe
        return mock_recipe.m_recipe_name

    @factory.post_generation
    def ingredients(self, create, extracted):
        if not create:
            return

        if extracted:
            for ingredient in extracted:
                self.ingredients.add(ingredient)
        else:
            mock_recipe = MockRecipe.objects.order_by('?').first()  # get a random MockRecipe
            for ingredient in mock_recipe.m_ingredients.all():
                self.ingredients.add(ingredient)

    @factory.post_generation
    def allergic_ingredients(self, create, extracted):
        if not create:
            return

        if extracted:
            for allergic_ingredient in extracted:
                self.allergic_ingredients.add(allergic_ingredient)
        else:
            allergic_ingredients = MockAllergicIngredient.objects.order_by('?')[:3]  # Get 3 random allergic ingredients
            for allergic_ingredient in allergic_ingredients:
                self.allergic_ingredients.add(allergic_ingredient)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        # Override the default _create method to create the RecipeIngredient objects
        recipe = super()._create(model_class, *args, **kwargs)

        mock_recipe = MockRecipe.objects.order_by('?').first()  # get a random MockRecipe
        recipe_ingredients = [RecipeIngredient(recipe=recipe, ingredient=ing) for ing in
                              mock_recipe.m_ingredients.all()]
        RecipeIngredient.objects.bulk_create(recipe_ingredients)

        # Add allergic ingredients to the recipe
        recipe.add_allergic_ingredients()

        return recipe


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    random.seed(random.random())  # Set random seed for deterministic results

    profile_first_name = factory.Faker('first_name')
    profile_last_name = factory.Faker('last_name')

    @factory.post_generation
    def allergies(self, create, extracted):
        if not create:
            return

        if extracted:
            allergies = list(set(extracted))  # Remove duplicates
        elif random.random() > 0.1:
            allergies = [AllergyFactory() for _ in range(3)]
        else:
            allergies = []

        for allergy in allergies:
            if allergy not in self.allergies.all():
                self.allergies.add(allergy)

    @factory.post_generation
    def personal_recipes(self, create, extracted):
        if not create:
            # do nothing.
            return

        if extracted:
            for recipe in extracted:
                self.personal_recipes.add(recipe)
        else:
            recipes = [RecipeFactory(profile=self) for _ in range(random.randint(2, 5))]
            for recipe in recipes:
                recipe_ingredients = MockRecipe.objects.filter(
                    m_recipe_name=recipe.recipe_name).first().m_ingredients.all()
                ingredients = [ri.ingredient for ri in recipe_ingredients]
                recipe.ingredients.set(ingredients)
                try:
                    recipe.save()
                    self.personal_recipes.add(recipe)
                except ValidationError as e:
                    # Handle the validation error gracefully
                    print(f"Error saving recipe: {e}")

    @classmethod
    def favorite_recipes(cls, profile, create=True, num_people=100, max_favorites=3):
        if not create:
            return []

        if not profile.id:
            profile.save()

        # Choose a random set of profiles
        profiles = Profile.objects.exclude(id=profile.id).order_by('?')[:num_people]

        # Choose a random set of favorite recipes for each profile
        favorites = []
        for p in profiles:
            recipes = Recipe.objects.filter(profile_id=p).order_by('?')[:max_favorites]
            favorites += [RecipeFavorite(profile=profile, recipe=r) for r in recipes]

        return favorites
