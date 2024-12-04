from django.core.management.base import BaseCommand, CommandError
import csv
# from dataentry.models import Student
from django.apps import apps
import datetime


# proposed command = python manage.py exportdata model_name

class Command(BaseCommand):
    help = "Export data from any model to csv file"
    
    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Name of the model to export data from')
    
    def handle(self, *args, **kwargs):
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
            self.stderr.write(self.style.ERROR(f"Model '{model_name}' not found in any installed app"))
            return
        
        # Get all the objects of the model
        # fetch the data from database
        data = model.objects.all()
        
        # Generate the timestamp
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        
        # define the csv file path/name
        file_path = f'exported_{model_name}_data_{timestamp}.csv'
        
        # open the csv file and write the data
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            
            # Write the csv header
            writer.writerow([field.name for field in model._meta.fields])
            
            # write the data
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])
        self.stdout.write(self.style.SUCCESS('Successfully exported data'))