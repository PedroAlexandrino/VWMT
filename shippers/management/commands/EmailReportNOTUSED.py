from django.core.management.base import BaseCommand, CommandError
from django.core.mail import EmailMultiAlternatives
from django.core.management.base import BaseCommand
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from vreport.models import *
from django.shortcuts import render, redirect, get_object_or_404
from vproject.models import *
from django.db.models import Q, Sum
from vlock.models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import ListView, DetailView
import datetime
from django.http import JsonResponse
from datetime import date
from django.views.generic import TemplateView, View, DeleteView
from crispy_forms.helper import FormHelper
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from vproject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from email.message import EmailMessage
from decimal import Decimal
import json
import time
import urllib.request
from django.utils.safestring import SafeString
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Função Principal para envio dos emails
# Utilizar o task scheduler do windows, e nas acçoes colocar:
# Program/script: cmd         Add arguments (optional): /c batch_vreport_clopes4.bat         Start in(optional): C:\visteon\vreport\management\commands


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_actual = date.today().strftime("%Y-%m-%d")
        data_anterior = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(
            "%Y-%m-%d"
        )
        hora_actual = int(datetime.datetime.now().strftime("%H"))
        hora_anterior = int(
            (datetime.datetime.now() - datetime.timedelta(hours=1)).strftime("%H")
        )
        hora_auxiliar = int(
            (datetime.datetime.now() - datetime.timedelta(hours=2)).strftime("%H")
        )  # MENOS DUAS HORAS PARA O CALCULO DO TOTAL PROD.

        smtpServer = "vistsmtp.visteon.com"
        msg = EmailMessage()
        msg[
            "Subject"
        ] = f"NEW vReport {hora_anterior}H, dia {data_actual}"  # colocar a hora at data
        msg["From"] = "noreply@visteon.com"
        msg["To"] = ["clopes4@visteon.com"]  # utilizar os emails.

        json_response = RelatorioProdFttJS.objects.filter(
            Q(data=data_actual) & Q(hora=hora_anterior) & Q(auxiliar == 2)
        ).order_by("linha")
        context = {"contextMaterial": json_response}
        html_message = render_to_string("vreport/emailReport.html", context)
        msg.add_alternative(html_message, subtype="html")

        # Send the message via our own SMTP server.
        s = smtplib.SMTP("vistsmtp.visteon.com", 25)
        s.send_message(msg)
        s.quit()
