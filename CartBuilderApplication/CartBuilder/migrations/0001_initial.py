# Generated by Django 4.1.7 on 2023-03-02 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('allergy_id', models.AutoField(primary_key=True, serialize=False)),
                ('allergy_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MockAllergicIngredient',
            fields=[
                ('m_allergic_ingredient_id', models.AutoField(primary_key=True, serialize=False)),
                ('m_allergic_ingredient', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MockIngredient',
            fields=[
                ('m_ingredient_id', models.AutoField(primary_key=True, serialize=False)),
                ('m_ingredient_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_id', models.IntegerField(primary_key=True, serialize=False)),
                ('profile_first_name', models.CharField(max_length=50)),
                ('profile_last_name', models.CharField(max_length=50)),
                ('allergies', models.ManyToManyField(related_name='profiles', to='CartBuilder.allergy')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipe_id', models.AutoField(primary_key=True, serialize=False)),
                ('recipe_name', models.CharField(max_length=100)),
                ('date_created', models.DateField()),
                ('cooking_instruction', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CartBuilder.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CartBuilder.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_favorited', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CartBuilder.profile')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CartBuilder.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='favorites',
            field=models.ManyToManyField(related_name='favorite_recipes_for', through='CartBuilder.RecipeFavorite', to='CartBuilder.profile'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='CartBuilder.RecipeIngredient', to='CartBuilder.ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='profile_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes_owned', to='CartBuilder.profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='favorite_recipes',
            field=models.ManyToManyField(related_name='fav', through='CartBuilder.RecipeFavorite', to='CartBuilder.recipe'),
        ),
        migrations.AddField(
            model_name='profile',
            name='personal_recipes',
            field=models.ManyToManyField(related_name='personal_recipes_for', to='CartBuilder.recipe'),
        ),
        migrations.CreateModel(
            name='MockRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_recipe_name', models.CharField(max_length=50)),
                ('m_allergic_ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CartBuilder.mockallergicingredient')),
                ('m_ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CartBuilder.mockingredient')),
            ],
        ),
    ]
