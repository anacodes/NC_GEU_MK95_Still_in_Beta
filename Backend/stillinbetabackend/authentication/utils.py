from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data['email_subject'],
                             body=data['email_body'],
                             to=[data['email_id']])
        email.send()