# Generated by Django 4.1.7 on 2023-03-07 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CartBuilder', '0009_alter_recipefavorite_recipe_recipepersonal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
