from django.core.management.base import BaseCommand
from dataentry.models import Student


class Command(BaseCommand):
    help = 'Insert data to database'
    
    def handle(self, *args, **kwargs):
        # Logic here
        # add one data first
        # mutiple data
        dataset = [
            {'roll_no': '1002', 'name': 'Sourav', 'age': 36},
            {'roll_no': '1003', 'name': 'Subhra', 'age': 30},
            {'roll_no': '1004', 'name': 'Gourav', 'age': 30},
            {'roll_no': '1005', 'name': 'Neelam', 'age': 30},
            {'roll_no': '1006', 'name': 'Rashmi', 'age': 38},
            {'roll_no': '1007', 'name': 'Shashwat', 'age': 43},
            {'roll_no': '1006', 'name': 'Hirabati', 'age': 58},
        ]
        
        for data in dataset:
            roll_no=data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()
            
            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll_no {roll_no} already exists'))
        self.stdout.write(self.style.SUCCESS('Successfully inserted data'))