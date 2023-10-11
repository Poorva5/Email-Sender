from django.urls import path
from .views import SendEmailView, SendTemplateEmail

urlpatterns = [
    path('send-email/', SendEmailView.as_view(), name='send_email'),
    path('send-email-template/', SendTemplateEmail.as_view(), name="send_template_enmail")
]