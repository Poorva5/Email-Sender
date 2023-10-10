from django.contrib import admin
from .models import EmailTemplate, EmailAttachement, EmailLog, Recipient


class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ['subject', 'body']

admin.site.register(EmailTemplate, EmailTemplateAdmin)


class EmailAttachementAdmin(admin.ModelAdmin):
    list_display = ['file']

admin.site.register(EmailAttachement, EmailAttachementAdmin)


class EmailLogAdmin(admin.ModelAdmin):
    list_display = ['template', 'send_at', 'send_by']

admin.site.register(EmailLog, EmailLogAdmin)


class RecipientAdmin(admin.ModelAdmin):
    list_display = ['email']

admin.site.register(Recipient, RecipientAdmin)

