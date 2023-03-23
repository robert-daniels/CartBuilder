import random
import factory
from faker import Faker
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .models import MockRecipe, MockIngredient, MockAllergicIngredient, TopTenMockAllergicIngredients, MockInstruction
from .models import Ingredient, Recipe, Allergy, Profile, RecipeIngredient, RecipeFavorite, MockRecipe, \
    AllergicIngredient, Instruction


class InstructionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Instruction


class AllergyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Allergy

    @factory.lazy_attribute
    def allergy_name(self):
        top_ten_allergic_ingredients = TopTenMockAllergicIngredients.objects.all()
        if top_ten_allergic_ingredients:
            random_allergic_ingredient = random.choice(top_ten_allergic_ingredients)
            return random_allergic_ingredient.allergic_ingredient


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
            pass
        elif random.random() > 0.1:
            allergies = [AllergyFactory() for _ in range(3)]

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
                    m_recipe_name=recipe.recipe_name
                ).first().m_ingredients.all()
                ingredients = []
                for ri in recipe_ingredients:
                    ingredient, created = Ingredient.objects.get_or_create(name=ri.m_ingredient_name)
                    ingredients.append(ingredient)
                    RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient)
                recipe.ingredients.set(ingredients)
                try:
                    recipe.save()
                    self.personal_recipes.add(recipe)
                except ValidationError as e:
                    # Handle the validation error gracefully
                    print(f"Error saving recipe: {e}")

    @classmethod
    def favorite_recipes(cls, profile, create=True, num_people=10, max_favorites=3):
        if not create:
            return []

        # Choose a random set of profiles
        profiles = Profile.objects.exclude(pk=profile.pk).order_by('?')[:num_people]

        # Choose a random set of favorite recipes for each profile
        favorites = []
        for p in profiles:
            recipes = Recipe.objects.filter(profile=p).order_by('?')[:max_favorites]
            for recipe in recipes:
                if recipe not in favorites:
                    favorites.append(recipe)

        return favorites


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
            for mock_ingredient in mock_recipe.m_ingredients.all():
                ingredient, _ = Ingredient.objects.get_or_create(name=mock_ingredient.m_ingredient_name)
                RecipeIngredient.objects.create(recipe=self, ingredient=ingredient)
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
                allergic_ingredient_instance, created = AllergicIngredient.objects.get_or_create(
                    ingredient_name=allergic_ingredient.m_allergic_ingredient
                )
                self.allergic_ingredients.add(allergic_ingredient_instance)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        # Override the default _create method to create the RecipeIngredient objects
        recipe = super()._create(model_class, *args, **kwargs)

        # Set the profile ID for the recipe
        profile = kwargs.pop('profile', None)
        if profile:
            recipe.profile = profile

        # Add ingredients to the recipe
        mock_recipe = MockRecipe.objects.order_by('?').first()  # get a random MockRecipe
        recipe_ingredients = []
        for mock_ingredient in mock_recipe.m_ingredients.all():
            ingredient, created = Ingredient.objects.get_or_create(name=mock_ingredient.m_ingredient_name)
            recipe_ingredient = RecipeIngredient(recipe=recipe, ingredient=ingredient)
            recipe_ingredients.append(recipe_ingredient)

        RecipeIngredient.objects.bulk_create(recipe_ingredients)
        recipe.ingredients.set([ri.ingredient for ri in recipe_ingredients])

        # Add instructions to the recipe
        cls.add_instructions(recipe, mock_recipe)

        for mock_instruction in mock_recipe.m_instructions.all():
            instruction = Instruction(instruction=mock_instruction, recipe=recipe)
            instruction.save()

        # Add allergic ingredients to the recipe
        recipe.add_allergic_ingredients()

        return recipe

    @classmethod
    def add_instructions(cls, recipe, mock_recipe):
        for mock_instruction in mock_recipe.m_instructions.all():
            instruction = InstructionFactory(recipe=recipe, instruction=mock_instruction.m_instruction)
            instruction.save()

    @classmethod
    def create_recipe(cls, profile):
        mock_recipe = MockRecipe.objects.order_by('?').first()
        fake = Faker()

        recipe = Recipe.objects.create(
            profile=profile,
            recipe_name=mock_recipe.m_recipe_name,
            date_created=fake.date(),
        )

        for mock_ingredient in mock_recipe.m_ingredients.all():
            ingredient, _ = Ingredient.objects.get_or_create(
                name=mock_ingredient.m_ingredient_name
            )
            RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient)
            recipe.ingredients.add(ingredient)

        for allergic_ingredient in mock_recipe.m_allergic_ingredients.all():
            allergic_ingredient, _ = AllergicIngredient.objects.get_or_create(
                ingredient_name=allergic_ingredient.m_allergic_ingredient
            )
            recipe.allergic_ingredients.add(allergic_ingredient)

        return recipe
