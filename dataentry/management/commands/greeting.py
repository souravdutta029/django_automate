from django.core.management.base import BaseCommand

# Proposed command = python manage.py greeting Name
# Proposed Output = Hi {name}, Good Morning
class Command(BaseCommand):
    help = 'Greets the User'
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of the User')
    
    def handle(self, *args, **kwargs):
        name = kwargs['name']
        greeting = f'Hi {name}, Good Morning!'
        # self.stdout.write(greeting)
        self.stdout.write(self.style.SUCCESS(greeting))