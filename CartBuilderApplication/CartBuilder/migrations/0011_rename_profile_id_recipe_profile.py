# Generated by Django 4.1.7 on 2023-03-08 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CartBuilder', '0010_alter_profile_profile_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='profile_id',
            new_name='profile',
        ),
    ]
