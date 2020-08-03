from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


class Util:
    @staticmethod
    def send_email(data):
        # email = EmailMessage(subject=data['email_subject'],
        #                      body=data['email_body'],
        #                      to=[data['email_id']])
        # email.send()
        if data['flag'] == 0:
            html_content = render_to_string("googlecalender.html", {
                'email_body': data['email_body'],
            })
        else:
            html_content = render_to_string("recommendation.html", {
                'email_body': data['email_body'],
            })
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(data['email_subject'], text_content,
                                       settings.EMAIL_HOST_USER,
                                       [data['email_id']])
        email.attach_alternative(html_content, "text/html")
        email.send()
