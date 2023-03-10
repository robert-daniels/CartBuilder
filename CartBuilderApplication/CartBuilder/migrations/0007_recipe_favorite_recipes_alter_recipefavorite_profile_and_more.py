# Generated by Django 4.1.7 on 2023-03-03 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CartBuilder', '0006_remove_recipe_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='favorite_recipes',
            field=models.ManyToManyField(related_name='favorited_recipes', through='CartBuilder.RecipeFavorite', to='CartBuilder.profile'),
        ),
        migrations.AlterField(
            model_name='recipefavorite',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_recipes_profile', to='CartBuilder.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='recipefavorite',
            unique_together={('profile', 'recipe')},
        ),
    ]
