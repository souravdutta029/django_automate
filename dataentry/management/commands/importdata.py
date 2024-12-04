from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv
# from dataentry.models import Student


# proposed command = python manage.py importdata filepath model_name

class Command(BaseCommand):
    help = 'Imports data from csv file to database'
    
    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str, help='Path to csv file')
        parser.add_argument('model_name', type=str, help='Name of the model to import data to')
    
    def handle(self, *args, **kwargs):
        # Logic here
        filepath = kwargs['filepath']
        model_name = kwargs['model_name'].capitalize()
        
        # Search for all models across all installed apps
        model = None
        for app_config in apps.get_app_configs():
            # Try to search for the model
            try:
                model = apps.get_model(app_config.label, model_name)
                break # Found the model
            except LookupError:
                continue # Model not found in this app, try the next one
            
        if not model:
            raise CommandError(f"Model '{model_name}' not found in any installed app")
        
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Successfully imported from CSV to database'))    