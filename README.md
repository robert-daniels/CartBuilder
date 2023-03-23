# Cart Builder

This Django application provides a platform for users to manage their recipes, 
taking into account personal preferences, allergies, and favorites. 
The following models are used to store and manage the data:

## Tables:

___
### Ingredient Model
***Ingredient***: Represents an ingredient used in a recipe.

The Ingredient model has a single field:

>***name***: The name of the ingredient.

___
### Profile Model


***Profile***: Represents a user's profile, including their allergies, personal recipes, and favorite recipes.

>***profile_id***: An auto-incrementing primary key.

>***profile_first_name***: The first name of the user.

>***profile_last_name***: The last name of the user.

>***allergies***: A many-to-many relationship with the Allergy model.

>***personal_recipes***: A many-to-many relationship with the Recipe model for personal recipes.

>***favorite_recipes***: A many-to-many relationship with the Recipe model through the RecipeFavorite model for favorite recipes.

The Profile model also includes several ***methods*** to manage allergies, personal recipes, and favorite recipes:

>***add_allergy()***: Adds an allergy to the profile.

>***delete_allergy()***: Removes an allergy from the profile.

>***get_all_allergies()***: Retrieves all allergies associated with the profile.

>***is_allergic()***: Checks if the profile has a specific allergy.

>***delete_own_recipe()***: Removes a personal recipe from the profile.

>***get_all_personal_recipes()***: Retrieves all personal recipes associated with the profile.

>***get_all_favorite_recipes()***: Retrieves all favorite recipes associated with the profile.

>***has_allergy_to()***: Checks if the profile has an allergy to a specific ingredient.

>***get_allergy_names()***: Retrieves a list of all allergy names associated with the profile.
___

### Recipe Model
***Recipe***: Represents a recipe, including its ingredients and any allergic ingredients.

>***recipe_id***: An auto-incrementing primary key.

>***profile***: A foreign key to the Profile model.

>***recipe_name***: The name of the recipe.

>***date_created***: The date the recipe was created.

>***ingredients***: A many-to-many relationship with the Ingredient model through the RecipeIngredient model.

>***allergic_ingredients***: A many-to-many relationship with the AllergicIngredient model.

>***favorite_recipes***: A many-to-many relationship with the Profile model through the RecipeFavorite model.

***Methods*** for Recipe Model:

>***add_allergic_ingredients()***: method is used to associate allergic ingredients with a recipe.

>The class method ***get_popular_recipes()***: returns a list of the most popular recipes based on the number of times they appear in users' favorite recipes list.

---

### Allergy Model
***Allergy***: Represents an allergy. It has two fields:

>***allergy_id***: An auto-incrementing primary key.

>***allergy_name***: The name of the allergy.

---

### RecipeIngredient Model
***RecipeIngredient***: Represents a many-to-many relationship between a Recipe and an Ingredient.
It has two foreign keys fields:

>***recipe***: A foreign key to the Recipe model.

>***ingredient***: A foreign key to the Ingredient model.

The model also includes two class methods:

>***find_recipes_with_a_certain_ingredient()***: Finds all recipes that contain the specified ingredient.

>***find_by_recipe()***: Retrieves all RecipeIngredient objects for a given recipe.

---

### AllergicIngredient Model
***AllergicIngredient***: Represents an ingredient that causes an allergic reaction.
It has a single field:

>***ingredient_name***: Stores the name of the allergic ingredient.

---

### RecipePersonal Model
***RecipePersonal***: Represents a many-to-many relationship between a Profile and a Recipe to store personal recipes.
It has two foreign key fields:

>***profile***: A foreign key to the Profile model.

>***recipe***: A foreign key to the Recipe model.

---

***RecipeFavorite***: Represents a many-to-many relationship between a Profile and a Recipe to store favorite recipes.
It has three fields:

>***profile***: A foreign key to the Profile model.

>***recipe***: A foreign key to the Recipe model.

>***date_favorited***: A date-time field to store when the recipe was added to the favorites.

The Meta class is used to ensure that a Profile and a Recipe can only be associated once.

---

## Mock Tables:

---

The following mock models are used to hold the data from [recipe_ingredients.csv](https://github.com/robert-daniels/CartBuilder/blob/main/CartBuilderApplication/recipe_ingredients.csv)

---



### MockIngredient Model
***MockIngredient***: Simulates an Ingredient instance with a single field:
A MockIngredient belongs to a MockRecipe, and MockRecipe can have multiple MockIngredients. 

>***m_ingredient_name***: The name of the mock ingredient.

---

### MockRecipe
***MockRecipe***: A mock model for simulating Recipe instances during development.
With three fields:

>***m_recipe_name***: The name of the mock recipe.

>***m_allergic_ingredients***: A many-to-many relationship with the MockAllergicIngredient model.

>***m_ingredients***: A many-to-many relationship with the MockIngredient model.

The ***MockRecipe*** model also includes three methods:

>***get_mock_recipe_name()***: Retrieves the name of the mock recipe.

>***get_mock_allergies_for_recipe()***: Retrieves all mock allergic ingredients associated with the mock recipe.

>***get_mock_ingredients()***: Retrieves all mock ingredients associated with the mock recipe.

---

### MockAllergicIngredient Model
***MockAllergicIngredient***: A mock model for simulating AllergicIngredient instances during development.

>***m_ingredient_name***: Simulates a AllergicIngredient instance

---

### TopTenMockAllergicIngredients Model
***TopTenMockAllergicIngredients***: A model to store the top ten most common allergic ingredients.
It has three fields:

>***allergic_ingredient***: The name of the allergic ingredient.

>***count***: The number of occurrences of the allergic ingredient.

>***rank***: The rank of the allergic ingredient in the top ten list.


---



## Core Contributors:

Ryan Fagen

Yassine Ben Addi

Robert Daniels

Thomas Whitworth

