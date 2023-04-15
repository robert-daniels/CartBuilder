# CartBuilder: Views Documentation

This document provides an overview of the views.py file in the CartBuilder Django web application. 
The views handle the logic and rendering of the different pages within the application.

## Views:

___
### home View
Handles the logic and rendering for the home page.

>Selects a random recipe from the ***SimpleMaster*** model for display in the "Food for Thought" card.

>Picks a random review from a hard-coded list of reviews for display in the "Review Cards" section.

>Retrieves the latest three recipes for the "Top Recipe Card" section.

>Renders the home.html template with the selected recipe, review, and latest recipes.
___

### about View
>Renders the ***about.html*** template for the About page.

___

### recipes View
>Retrieves all recipes from the ***SimpleMaster*** model

>Renders the ***recipes.html*** template with the full list of recipes.

___

### recipe View

>Retrieves a specific recipe from the ***SimpleMaster*** model based on the ***requestedRecipeKey*** parameter

>Renders the ***recipe.html*** template with the selected recipe.

---

### search View (search_by_ingredient)

>Searches the ***SimpleMaster*** model for recipes containing the user's search term in the ***recipeNER*** field.

>Renders the ***search.html*** template with the search results and the search query.

---

### search_by_recipe View

>Searches the ***SimpleMaster*** model for recipes containing the user's search term in the ***recipeTitle*** field.

>Renders the ***search.html*** template with the search results and the search query.

---

### add_recipe View

>Handles the logic for adding a new recipe to the ***SimpleMaster*** model.

>When the user submits a form with the recipe information, a new instance of the ***SimpleMaster*** model is created and saved.

>A success message is displayed, and the user is redirected to the ***/cartbuilder*** URL. 
 
>Renders the ***add_recipe.html*** template for the Add Recipe form.

---

### ingredients View
>Renders the ***ingredients.html*** template for the Ingredients page.

---

### allergies View
>Renders the ***allergies.html*** template for the Allergies page.

---

### login View
>Renders the ***login.html*** template for the Login page.

---

### registration View
>Renders the ***registration.html*** template for the Login page.

## Core Contributors:

Ryan Fagen

Yassine Ben Addi

Robert Daniels

Thomas Whitworth
