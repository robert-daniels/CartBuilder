# Generated by Django 4.1.7 on 2023-02-19 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CartBuilder', '0005_mockcookinginstruction_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='description',
        ),
        migrations.AlterField(
            model_name='mockcookinginstruction',
            name='m_cooking_instruction',
            field=models.CharField(max_length=50),
        ),
    ]
