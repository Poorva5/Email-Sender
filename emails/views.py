from django.shortcuts import render
from rest_framework.views import APIView
from .models import EmailTemplate, EmailLog
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.conf import settings


class SendEmailView(APIView):
    
    def post(self, request):
    
        subject = request.data.get('subject')
        message_body = request.data.get('body')
        recipients_emails= request.data.get('recipients')
        if not isinstance(recipients_emails, (list, tuple)):
            recipients_emails = [recipients_emails]

        from_email = settings.EMAIL_HOST_USER

        for recipient_email in recipients_emails:
            send_mail(subject, message_body, from_email, [recipient_email])

        return Response({'message': 'Email sent successfully!'}, status=status.HTTP_200_OK)
    


class SendTemplateEmail(APIView):

    def post(self, request):

        template_id = request.data.get('template_id')
        email_template = EmailTemplate.objects.get(pk=template_id)
        email_subject = email_template.subject
        email_body = email_template.body

        recipients_emails= request.data.get('recipients')
        if not isinstance(recipients_emails, (list, tuple)):
            recipients_emails = [recipients_emails]

        from_email = settings.EMAIL_HOST_USER
        for recipient_email in recipients_emails:
            send_mail(
                email_subject,
                email_body,
                from_email,
                [recipient_email]
            )

            email_log = EmailLog.objects.create(
                template=email_template,
                sent_by=request.user,
            )
            email_log.recipients.add(recipient_email)

        return Response({'message': 'Emails sent successfully'}, status=status.HTTP_200_OK)






        



