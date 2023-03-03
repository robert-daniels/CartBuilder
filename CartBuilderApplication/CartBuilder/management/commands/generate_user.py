from django.core.management.base import BaseCommand
from ...factory import ProfileFactory

class Command(BaseCommand):
    help = 'Imports recipe data from a CSV file'

    def handle(self, *args, **options):
        # create a new profile with random information
        profile = ProfileFactory()
