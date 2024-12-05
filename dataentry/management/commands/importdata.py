from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv
from django.db import DataError
from dataentry.utils import check_csv_errors
# from dataentry.models import Student


# proposed command = python manage.py importdata filepath model_name

class Command(BaseCommand):
    help = 'Imports data from csv file to database'
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to csv file')
        parser.add_argument('model_name', type=str, help='Name of the model to import data to')
    
    def handle(self, *args, **kwargs):
        # Logic here
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()
        
        model = check_csv_errors(file_path, model_name)
        
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
    
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Successfully imported from CSV to database'))    