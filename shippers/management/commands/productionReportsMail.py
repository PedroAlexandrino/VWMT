from django.core.mail import EmailMultiAlternatives
from django.core.management.base import BaseCommand
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Função Principal para envio dos emails
class Command(BaseCommand):
    def handle(self, *args, **options):

        try:
            server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server_ssl.ehlo()  # optional
        except:
            print("Something went wrong...")
