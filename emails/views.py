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

        try:
            send_mail(subject, message_body, from_email, recipients_emails)
            return Response({'message': 'Email sent successfully!'}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'message': 'Something Went Wrong'}, status=status.HTTP_400_BAD_REQUEST)


