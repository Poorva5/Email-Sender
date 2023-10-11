from django.db import models
from django.contrib.auth.models import User


class EmailAttachement(models.Model):
    file = models.FileField(upload_to='email_attachments/')

class EmailTemplate(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    attachements = models.ManyToManyField('EmailAttachement', blank=True, null=True)
    
class Recipient(models.Model):
    email = models.EmailField()
    
class EmailLog(models.Model):
    template = models.ForeignKey('EmailTemplate', on_delete=models.CASCADE)
    recipient = models.ForeignKey('Recipient', on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
