import smtplib
import datetime

from django.core.mail import EmailMessage, EmailMultiAlternatives
from email.message import EmailMessage
from django.core.management import BaseCommand
from datetime import date, datetime, timedelta


# Função Principal para envio dos emails
# Utilizar o task scheduler do windows, e nas acçoes colocar:
# Program/script: cmd         Add arguments (optional): /c batch_vproject_email.bat         Start in(optional): C:\visteon\vproject\management\commands
from django.template.loader import render_to_string


class Command(BaseCommand):
    def handle(self, *args, **options):

        subject, from_email, to = 'Report', 'noreply@visteon.com', ['aroque1@visteon.com']
        text_content = 'This is an important message.'
        html_content = render_to_string("accounts/schedule_mail.html")
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        # try:
        #     data_actual = date.today().strftime("%Y-%m-%d")
        #     data_ontem = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        #     data_actual_date = date.today()
        #     data_ontem_date = date.today() - timedelta(days=1)
        #     data_anterior = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(
        #         "%Y-%m-%d"
        #     )
        #     hora_actual = int(datetime.datetime.now().strftime("%H"))
        #     hora_anterior = int(
        #         (datetime.datetime.now() - datetime.timedelta(hours=1)).strftime("%H")
        #     )
        #     minuto_actual = int(datetime.datetime.now().strftime("%M"))
        #     data_dia_semana = datetime.datetime.today().weekday() + 1
        #     data_zero = datetime.datetime(
        #         data_actual_date.year, data_actual_date.month, data_actual_date.day, 0, 5, 1
        #     )
        #     data_agora = datetime.datetime.now()
        #     if (
        #         data_agora < data_zero
        #     ):  # SE FOR ANTES DAS 0h5minutos eu vou olhar para o dia anterior
        #         data_actual = data_ontem
        #         data_actual_date = data_ontem_date
        #         smtpServer = "vistsmtp.visteon.com"
        #     msg = EmailMessage()
        #     msg[
        #         "Subject"
        #     ] = f"{hora_anterior}h59, Estimativa Produção do dia {data_actual}"  # colocar a hora at data
        #     msg["From"] = "noreply@visteon.com"
        #     msg["To"] = [
        #         "aroque1@visteon.com",
        #         "andre.roque@outlook.pt",
        #     ]  # utilizar os emails.
        #             # # colocar aqui os dados caso o email seja as 0h10min
        #     # json_responseProdGlobal = (
        #     #     RelatorioProdLine_Global.objects.filter(
        #     #         pk_schedule_global=data_actual_date
        #     #     )
        #     #         .filter(active=True)
        #     #         .order_by("nome_linha__descricao")
        #     # )
        #     # context = {
        #     #     "contextMaterialProd": json_responseProdGlobal,
        #     # }
        #     html_message = render_to_string("accounts/schedule_mail.html")
        #     msg.add_alternative(html_message, subtype="html")
        #             # Send the message via our own SMTP server.
        #     s = smtplib.SMTP("vistsmtp.visteon.com", 25)
        #     s.send_message(msg)
        #     s.quit()
        # except:
        #     print("Something went wrong...")