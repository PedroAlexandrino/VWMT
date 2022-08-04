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
from vreport.models import *
from django.shortcuts import render, redirect, get_object_or_404
from vproject.models import *
from django.db.models import Q, Sum
from vlock.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import ListView, DetailView
from datetime import date, datetime, timedelta
from django.http import JsonResponse
from django.views.generic import TemplateView, View, DeleteView
from crispy_forms.helper import FormHelper
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render
import json
import time
import urllib
import urllib.request
from django.utils.safestring import SafeString
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import logging, traceback
from urllib import error
from tablib import Dataset
from vboard.models import *
from collections import defaultdict
from vboard.forms import *
from django.db.models import Max
from vboard.resources import *
from pathlib import Path
import os, io
import pyexcel as p
import pandas as pd
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

# Função Principal para envio dos emails
# Utilizar o task scheduler do windows, e nas acçoes colocar:
# Program/script: cmd         Add arguments (optional): /c batch_vreport_clopes4.bat         Start in(optional): C:\visteon\vreport\management\commands


class Command(BaseCommand):
    def handle(self, *args, **options):
        tomorrow = date.today() + timedelta(days=1)
        tomorrow_schedule = Schedule_Diaria.objects.filter(
            pk_schedule_global__dia=tomorrow
        )
        if len(tomorrow_schedule) > 0:
            print("Já existe schedule de amanhã")
        else:
            data = dict()
            boards = {}
            sch_global = Schedule_Global.objects.all()
            dataset = Dataset()
            data_folder = Path("W:\mnfg\Final_Assy\Produção\Dashboard Schedule")
            current_year = tomorrow.year
            if tomorrow.day < 10:
                day = "0" + str(tomorrow.day)
            else:
                day = str(tomorrow.day)
            if tomorrow.month < 10:
                month = "0" + str(tomorrow.month)
            else:
                month = str(tomorrow.month)
            data_folder_xls = data_folder / str(
                "Schedule_Dashboard_"
                + day
                + ""
                + month
                + ""
                + str(current_year)[-2:]
                + ".xls"
            )
            # data_folder_xlsx = data_folder / str(
            #    "Schedule_Dashboard_" + day + "" + month + "" + str(current_year)[-2:] + ".xlsx"
            # )
            # p.save_book_as(file_name=data_folder_xls, dest_file_name=data_folder_xlsx)
            output = io.BytesIO()
            try:
                df = pd.read_excel(data_folder_xls, header=None)
            except Exception as e:
                print(e)
                return False

            writer = pd.ExcelWriter(output, engine="xlsxwriter")
            df.to_excel(writer, sheet_name="Sheet1")
            writer.save()
            xlsx_data = output.getvalue()
            imported_data = dataset.load(xlsx_data, format="xlsx")
            nr_entradas = 0  # variavel para guardar o numero de linhas de schedule
            qty_total = 0  # variavel para guardar a quantidade total
            for idata in imported_data:  # CODIGO PARA CRIAR A SCHEDULE GLOBAL
                if (
                    str(idata[1]) == "Plant"
                    or str(idata[2]) == "Date"
                    or str(idata[3]) == "Local Update"
                    or str(idata[4]) == "Line"
                    or str(idata[5]) == "Part Number"
                    or str(idata[6]) == "Part Description"
                    or "Schedule" in str(idata[7])
                    or str(idata[8]) == "IFS OEM Group"
                    or str(idata[9]) == "IFS Product"
                    or str(idata[10]) == "IFS Part Desc."
                ):
                    continue
                # verifica se a data ja existe, se existir da erro e sai
                datafloat = idata[2]
                if (
                    type(datafloat) == float
                ):  # se o ficheiro for xls vem com a data como numerico
                    datafloat_conversao = (datafloat - 25569) * 86400.0
                    dataStr = datetime.utcfromtimestamp(datafloat_conversao)
                    dataXLSX = dataStr.strftime("%Y-%m-%d")
                elif (
                    type(datafloat) == datetime
                ):  # se o ficheiro for xlsx vem com a data como datetime
                    dataXLSX = datafloat.strftime("%Y-%m-%d")
                else:
                    break  # cheguei ao fim do xls

                partnumber = idata[5]
                if (
                    (partnumber == "Sub Total")
                    or (partnumber == "")
                    or (partnumber == None)
                ):
                    continue  # esta linha não é para contar no numero de entradas

                if not ((idata[1]) == "PALMELA"):
                    continue

                nr_entradas = nr_entradas + 1
                qty_total = qty_total + idata[7]

            Schedule_Global.objects.create(
                dia=dataXLSX, nr_entradas=nr_entradas, qty_dia=int(qty_total)
            )  # trocar so para create
            sequencia = 0

            for idata in imported_data:  # CODIGO PARA CRIAR A SCHEDULE DAILY
                if (
                    str(idata[1]) == "Plant"
                    or str(idata[2]) == "Date"
                    or str(idata[3]) == "Local Update"
                    or str(idata[4]) == "Line"
                    or str(idata[5]) == "Part Number"
                    or str(idata[6]) == "Part Description"
                    or "Schedule" in str(idata[7])
                    or str(idata[8]) == "IFS OEM Group"
                    or str(idata[9]) == "IFS Product"
                    or str(idata[10]) == "IFS Part Desc."
                ):
                    continue
                if (
                    (idata[5] == "Sub Total") or (idata[5] == "") or idata[5] == None
                ):  # se o partnumber for sub total ou clean seguir para o proximo
                    continue
                if (
                    (idata[4] == "Sub Total") or (idata[4] == "") or idata[5] == None
                ):  # se o prodline for sub total ou clean seguir para o proximo
                    continue

                xls_partnumber = idata[5]
                xls_descricao = idata[6]
                xls_prodline = idata[4]
                xls_qty_to_complete = idata[7]
                xls_state = "Espera"

                if not (
                    Prod_Line.objects.filter(codigo=xls_prodline).exists()
                ):  # CASO NAO EXISTE ESTE PRODLINE AINDA
                    Prod_Line.objects.create(
                        codigo=xls_prodline,
                        descricao="NOT_ASSIGNED",
                        fk_workcenter_id="NOT_ASSIGNED",
                    )
                    xls_state = "Prodline"

                if not (
                    Part_Numb.objects.filter(codigo=xls_partnumber).exists()
                ):  # CASO NAO EXISTE ESTE PARTNUMBER AINDA
                    if ModelType_Aux.objects.filter(
                        partnumber=xls_partnumber
                    ).exists():  # CASO EXISTA NA TABELA DE MODELTYPE
                        mt = ModelType_Aux.objects.filter(
                            partnumber=xls_partnumber
                        ).last()
                        Part_Numb.objects.create(
                            codigo=xls_partnumber,
                            descricao=mt.description,
                            activo=1,
                            fk_prod_line_id=xls_prodline,
                            ref_code=mt.model,
                            product=mt.product,
                        )
                        xls_state = "Espera"
                    else:  # CASO NAO EXISTA CRIAR NA BD
                        Part_Numb.objects.create(
                            codigo=xls_partnumber,
                            descricao=xls_descricao,
                            activo=1,
                            fk_prod_line_id=xls_prodline,
                            ref_code="NOT_ASSIGNED",
                            product="NOT_ASSIGNED",
                        )
                        xls_state = "Board"

                boardsClean = "NO_BOARD"
                # CODIGO PARA COLOCAR AS PLACAS E A QUANTIDADE NO QTY_COMPLETED:
                if ModelLinha_Config.objects.filter(partnumber=xls_partnumber).exists():
                    mlc = ModelLinha_Config.objects.filter(
                        partnumber=xls_partnumber
                    ).last()
                    modelLinha = ModelLinha_Config.objects.filter(end_item=mlc.end_item)
                    for x in modelLinha:
                        boards[x.board] = 0

                    boardsClean = boards
                    boardsClean = str(boardsClean)[1:-1]
                    boards.clear()

                # CARREGAR A BOM E VER SE TEM FALTA DE PLACA!
                sequencia = sequencia + 1
                obj = Schedule_Diaria.objects.create(
                    pk_schedule_global_id=dataXLSX,
                    pk_prod_line_id=xls_prodline,
                    pk_part_number_id=xls_partnumber,
                    qty_dia=xls_qty_to_complete,
                    qty_concluida=boardsClean,
                    order_sequence=sequencia,
                    state=xls_state,
                )
                obj.order_sequence = obj.pk
                obj.save()

            Schedule_Global.objects.filter(dia=dataXLSX).update(
                nr_entradas=nr_entradas, qty_dia=int(qty_total)
            )
