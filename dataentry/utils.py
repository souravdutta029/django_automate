from django.apps import apps
from django.core.management.base import CommandError
import csv
from django.db import DataError
from django.core.mail import EmailMessage
from django.conf import settings


def get_all_custom_models():
    default_models = ['ContentType', 'Session', 'LogEntry', 'Group', 'Permission', 'User', 'Upload']
    # try to get all the apps
    custom_models = []
    for model in apps.get_models():
       if model.__name__ not in default_models:
           custom_models.append(model.__name__)
    return custom_models


def check_csv_errors(file_path, model_name):
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
    
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            csv_headers = reader.fieldnames
            # compare csv header with model field names
            if csv_headers != model_fields:
                raise DataError(f"CSV header does not match with the {model_name} model fields")
    except Exception as e:
        raise e
    
    return model


def send_email_notification(mail_subject, message, to_email):
    try:
        from_email = settings.DEFAULT_FROM_EMAIL
        mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
        mail.send()
    except Exception as e:
        raise e