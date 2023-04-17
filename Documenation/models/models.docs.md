# CartBuilder: Models Documentation

This Django application provides a platform for users to manage their recipes, 
taking into account personal preferences, allergies, and favorites. 
The following models are used to store and manage the data:

## Models:

___
### SimpleRecipe Model
***SimpleRecipe***: This model represents a simple recipe with only two fields:

>***recipeKey***: An integer field that serves as the primary key for the model.

>***recipeName***: A character field that contains the name of the recipe. The maximum length is set to 60 characters.

___

### SimpleIngredient Model
***SimpleIngredient***: This model represents a simple ingredient with the following fields:

>***Ingredients_ID***: An integer field that serves as the primary key for the model.

>***Ingredients_Name***:  A character field that contains the name of the ingredient. The maximum length is set to 60 characters.

___

### SimpleNERIngredient Model
***SimpleNERIngredient***: This model represents a Named Entity Recognition (NER) ingredient:

>***recipeKey***: An integer field that connects the NER ingredient to the corresponding recipe.

>***NER_Name***: A character field that contains the named entity recognized ingredient. The maximum length is set to 60 characters.

___

### SimpleRecipeIngredientBlurb Model
***SimpleRecipeIngredientBlurb***: This model represents a recipe ingredient blurb:

>***recipeKey***: An integer field that connects the ingredient blurb to the corresponding recipe.

>***ingredients***: A text field that contains the full list of ingredients for the recipe.

---

### SimpleRecipeDirection Model
***SimpleRecipeDirection***: This model represents a recipe direction:

>***recipeKey***: An integer field that connects the direction to the corresponding recipe.

>***directions***: A text field that contains the full list of directions for the recipe.

---

### SimpleMaster Model
***SimpleMaster***: This model serves as a master model that consolidates all the information for a recipe:

>***recipeKey***: recipeKey: An integer field that serves as a unique identifier for the SimpleMaster model and establishes a connection to related models.

>***recipeTitle***: A text field that contains the title of the recipe.

>***recipeIngredients***: A text field that contains the full list of ingredients for the recipe

>***recipeDirections***: A text field that contains the full list of directions for the recipe.

>***recipeNER***: A text field that contains the Named Entity Recognition (NER) processed ingredients for the recipe.

>***recipeImage***: An optional image field that contains an image of the recipe. It is set to accept null values and can be left blank.
---

## Core Contributors:

Ryan Fagen

Yassine Ben Addi

Robert Daniels

Thomas Whitworth
