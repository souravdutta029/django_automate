from django.contrib import admin
from .models import List, Subscriber, Email, EmailTracking, Sent


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email_address', 'email_list')
    

class EmailTarackingAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscriber', 'opened_at', 'clicked_at')
    

class EmailAdmin(admin.ModelAdmin):
    list_display = ('email_list', 'subject', 'body', 'attachment', 'sent_at')

admin.site.register(List)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(EmailTracking, EmailTarackingAdmin)
admin.site.register(Sent)
