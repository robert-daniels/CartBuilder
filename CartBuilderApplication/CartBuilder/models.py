from django.db.models import Count
from django.db import models


# Create your models here.
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


class SimpleMaster(models.Model):
    recipeKey = models.IntegerField()
    recipeTitle = models.TextField()
    recipeIngredients = models.TextField()
    recipeDirections = models.TextField()
    recipeNER = models.TextField()
    recipeImage = models.ImageField(upload_to='recipe_images/', null=True, blank=True)


