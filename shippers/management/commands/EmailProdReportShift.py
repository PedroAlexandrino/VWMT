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
from datetime import date, datetime, timedelta
import datetime
from django.http import JsonResponse
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
        data_ontem = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        data_actual_date = date.today()
        data_ontem_date = date.today() - timedelta(days=1)
        data_anterior = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(
            "%Y-%m-%d"
        )
        hora_actual = int(datetime.datetime.now().strftime("%H"))
        hora_anterior = int(
            (datetime.datetime.now() - datetime.timedelta(hours=1)).strftime("%H")
        )
        minuto_actual = int(datetime.datetime.now().strftime("%M"))
        data_dia_semana = datetime.datetime.today().weekday() + 1
        lista_users_email_activo = []
        todos_os_users = Empregado_Utilizador.objects.all()
        data_zero = datetime.datetime(
            data_actual_date.year, data_actual_date.month, data_actual_date.day, 0, 5, 1
        )
        data_agora = datetime.datetime.now()

        if (
            data_agora < data_zero
        ):  # SE FOR ANTES DAS 0h5minutos eu vou olhar para o dia anterior
            data_actual = data_ontem
            data_actual_date = data_ontem_date

        for x in todos_os_users:
            if x.vreport_email:
                lista_users_email_activo.append(x.utilizador.email)

        sd_hoje = Schedule_Diaria.objects.filter(
            pk_schedule_global=data_actual
        )  # se existir schedule, entao enviamos o email
        if sd_hoje.exists():  # EXISTE SCHEDULE HOJE?
            smtpServer = "vistsmtp.visteon.com"
            msg = EmailMessage()
            msg[
                "Subject"
            ] = f"{hora_anterior}h59m de {data_actual}. Estimativa Produção"  # colocar a hora at data
            msg["From"] = "noreply@visteon.com"
            msg["To"] = ["clopes4@visteon.com", "rui.nascimento@visteon.com"]

            # colocar aqui os dados caso o email seja as 0h10min
            json_responseProdGlobal = (
                RelatorioProdLine_Global.objects.filter(
                    pk_schedule_global=data_actual_date
                )
                .filter(active=True)
                .order_by("nome_linha__descricao")
            )
            context = {
                "contextMaterialProd": json_responseProdGlobal,
            }
            html_message = render_to_string("vreport/emailReportGlobal.html", context)
            msg.add_alternative(html_message, subtype="html")

            # Send the message via our own SMTP server.
            s = smtplib.SMTP("vistsmtp.visteon.com", 25)
            s.send_message(msg)
            s.quit()
