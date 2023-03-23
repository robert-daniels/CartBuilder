# to run, in CLI python manage.py ProcessCsv



import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from CartBuilder.models import SimpleRecipe

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR / 'RecipeName_List.csv'), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                SimpleRecipe.objects.create(recipeKey=row[0], recipeName=row[1])