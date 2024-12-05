from awd_main.celery import app
from django.core.management import call_command
from dataentry.utils import send_email_notification



@app.task
def send_email_task(subject, message, to_email, attachment=None):
    send_email_notification(subject, message, to_email, attachment)
    return 'Email sending task executed successfully.'