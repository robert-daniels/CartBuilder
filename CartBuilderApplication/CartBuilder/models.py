from django.db import models
from django.db.models import Count


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RecipePersonal(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='personal_recipe_relations')
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='profiles_with_personal_recipe')


class RecipeFavorite(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='favorite_recipes_profile')
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='profiles_with_favorite_recipe')
    date_favorited = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('profile', 'recipe')


class AllergicIngredient(models.Model):
    ingredient_name = models.CharField(max_length=50)


class Instruction(models.Model):
    instruction = models.CharField(max_length=120)

    def __str__(self):
        return self.instruction


class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='recipes_owned')
    recipe_name = models.CharField(max_length=100)
    date_created = models.DateField()
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    allergic_ingredients = models.ManyToManyField(AllergicIngredient)
    instructions = models.ManyToManyField(Instruction)
    favorite_recipes = models.ManyToManyField('Profile', through='RecipeFavorite', related_name='recipes_favorited')

    def __str__(self):
        _ingredients = [self.ingredients.name for _ingredient in self.ingredients.all()]
        ingredients_list = ", ".join(_ingredients)
        return f"{self.recipe_name}: ({ingredients_list})"

    def add_allergic_ingredients(self):
        # Get the MockAllergicIngredient instances for the current recipe
        mock_recipe = MockRecipe.objects.filter(m_recipe_name=self.recipe_name).first()
        mock_allergic_ingredients = mock_recipe.m_allergic_ingredients.all()

        # Create new AllergicIngredient instances from the MockAllergicIngredient instances
        allergic_ingredients = []
        for mock_allergic_ingredient in mock_allergic_ingredients:
            allergic_ingredient, created = AllergicIngredient.objects.get_or_create(
                ingredient_name=mock_allergic_ingredient.m_allergic_ingredient
            )
            allergic_ingredients.append(allergic_ingredient)

        # Associate the AllergicIngredient instances with the current recipe
        self.allergic_ingredients.add(*allergic_ingredients)

    @classmethod
    def get_popular_recipes(cls, num_recipes=10):
        """
            Retrieve a list of the most popular recipes, based on the number of times they appear
            in users' favorite recipes list.

            Parameters:
            num_recipes (int, optional): The maximum number of popular recipes to retrieve.
                Defaults to 10.

            Returns:
            A QuerySet of Recipe objects, ordered by popularity (i.e., number of users who have
            favorited the recipe), with a maximum length of `num_recipes`.
        """
        return cls.objects.annotate(num_favorites=Count('fav')).order_by('-num_favorites')[:num_recipes]


class Allergy(models.Model):
    allergy_id = models.AutoField(primary_key=True)
    allergy_name = models.CharField(max_length=50)

    def __str__(self):
        return self.allergy_name


class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    profile_first_name = models.CharField(max_length=50)
    profile_last_name = models.CharField(max_length=50)
    allergies = models.ManyToManyField(Allergy, related_name='profiles')
    personal_recipes = models.ManyToManyField(Recipe, related_name='personal_recipes_for')
    favorite_recipes = models.ManyToManyField(Recipe, through=RecipeFavorite, related_name='fav')

    def add_allergy(self, allergy):
        self.allergies.add(allergy)

    def delete_allergy(self, allergy):
        self.allergies.remove(allergy)

    def get_all_allergies(self):
        return self.allergies.all()

    def is_allergic(self, allergy):
        return self.allergies.filter(pk=allergy.pk).exists()

    def delete_own_recipe(self, recipe):
        self.personal_recipes.remove(recipe)

    def get_all_personal_recipes(self):
        return self.personal_recipes.all()

    def get_all_favorite_recipes(self):
        return self.favorite_recipes.all()

    def has_allergy_to(self, allergy):
        return allergy.id in self.allergies.values_list('allergy_id', flat=True)

    def get_allergy_names(self):
        return list(self.allergies.values_list('allergy_name', flat=True))


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    @classmethod
    def find_recipes_with_a_certain_ingredient(cls, recipe, ingredient):
        """
        Finds all recipes that contain the specified ingredient.

        Parameters:
            recipe (Recipe): The recipe to search for.
            ingredient (Ingredient): The ingredient to search for.

        Returns:
            A list of Recipe objects that contain the specified ingredient.
            If no recipes are found, an empty list is returned.
        """
        recipe_ingredients = cls.objects.filter(recipe=recipe, ingredient=ingredient)
        if recipe_ingredients:
            return [r.recipe for r in recipe_ingredients]
        else:
            return []

    @classmethod
    def find_by_recipe(cls, recipe):
        """
        Retrieve all RecipeIngredient objects for a given recipe.

        Parameters:
        recipe (Recipe): The recipe to find RecipeIngredient objects for.

        Returns:
        A QuerySet of RecipeIngredient objects that are associated with the given recipe.

        """
        recipe_ingredients = cls.objects.filter(recipe=recipe)
        if recipe_ingredients:
            return recipe_ingredients
        else:
            return []


class MockIngredient(models.Model):
    m_ingredient_name = models.CharField(max_length=50)

    def __str__(self):
        return self.m_ingredient_name


class MockInstruction(models.Model):
    m_instruction = models.CharField(max_length=120)


class MockAllergicIngredient(models.Model):
    m_allergic_ingredient = models.CharField(max_length=50)

    def __str__(self):
        return self.m_allergic_ingredient


class MockRecipe(models.Model):
    m_recipe_name = models.CharField(max_length=50)
    m_allergic_ingredients = models.ManyToManyField(MockAllergicIngredient)
    m_ingredients = models.ManyToManyField(MockIngredient)
    m_instructions = models.ManyToManyField(MockInstruction)

    def get_mock_recipe_name(self):
        return self.m_recipe_name

    def get_mock_allergies_for_recipe(self):
        return self.m_allergic_ingredients.all()

    def get_mock_ingredients(self):
        return self.m_ingredients.all()


class TopTenMockAllergicIngredients(models.Model):
    allergic_ingredient = models.CharField(max_length=50)
    count = models.IntegerField()
    rank = models.IntegerField()

    def __str__(self):
        return f"{self.allergic_ingredient}: {self.count}"


class SimpleRecipe(models.Model):
    recipeKey = models.IntegerField(primary_key=True)
    recipeName = models.CharField(max_length=60)

class SimpleIngredient(models.Model):
    Ingredients_ID = models.IntegerField(primary_key=True)
    Ingredients_Name = models.CharField(max_length=60)

class SimpleNERIngredient(models.Model):
    recipeKey = models.IntegerField()
    NER_Name = models.CharField(max_length=60)

class SimpleRecipeIngredientBlurb(models.Model):
    recipeKey = models.IntegerField()
    ingredients = models.TextField()
class SimpleRecipeDirection(models.Model):
    recipeKey = models.IntegerField()
    directions = models.TextField()