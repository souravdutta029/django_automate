from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmailForm
from .models import Subscriber
from .tasks import send_email_task

def send_email(request):
    if request.method == 'POST':
        email_form = EmailForm(request.POST, request.FILES)
        if email_form.is_valid():
            email_form = email_form.save()
            
            # send email
            mail_subject = request.POST.get('subject')
            message = request.POST.get('body')
            email_list = request.POST.get('email_list')
            
            # Access the selected email list
            email_list = email_form.email_list
            
            # Extract email addresses from the Subscriber model
            subscribers = Subscriber.objects.filter(email_list=email_list)
            to_email = [email.email_address for email in subscribers]
            
            if email_form.attachment:
                attachment = email_form.attachment.path
            else:
                attachment = None
            
            # Handover email sending to Celery 
            send_email_task.delay(mail_subject, message, to_email, attachment)

            # show success message 
            messages.success(request, 'Email sent successfully!')
            return redirect('send_email')
    else:
        email_form = EmailForm()
        context = {
            'email_form': email_form
        }
        return render(request, 'emails/send_email.html', context)
