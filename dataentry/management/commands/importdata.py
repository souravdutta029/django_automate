from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv
from django.db import DataError
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
        
        # get the field names of the model that we found
        model_fields = [field.name for field in model._meta.fields if field.name != 'id']
        
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            csv_headers = reader.fieldnames
            # compare csv header with model field names
            if csv_headers != model_fields:
                raise DataError(f"CSV header does not match with the {model_name} model fields")
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Successfully imported from CSV to database'))    