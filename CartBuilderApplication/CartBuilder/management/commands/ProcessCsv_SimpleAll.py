# to run, in CLI python manage.py ProcessCsv



import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from CartBuilder.models import SimpleMaster

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR / 'SimpleAll.csv'), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                SimpleMaster.objects.create(
                    recipeKey = row[0],
                    recipeTitle = row[1],
                    recipeIngredients = row[2],
                    recipeDirections = row[3],
                    recipeNER = row[4]
                )