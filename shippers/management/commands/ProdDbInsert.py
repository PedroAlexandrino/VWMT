from django.core.management.base import BaseCommand, CommandError
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
from django.conf import settings
from decimal import Decimal
import json
import time
import urllib.request
from django.utils.safestring import SafeString
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import logging, traceback
from urllib import error

logger = logging.getLogger("vReport")  # escreve no ficheiro log

# Função Principal para preencher base de dados com o PROD da Hora Anterior. (CORRER AS xxHoras 01Minutos )
# Utilizar o task scheduler do windows, e nas acçoes colocar:
# Program/script: cmd         Add arguments (optional): /c batch_vreport_clopes4.bat         Start in(optional): C:\visteon\vreport\management\commands


class Command(BaseCommand):

    # Objectivo é colocar todas as informaçoes de ftts na base de dados.
    # Verificar na base de dados todos os items que estejam activos.
    def handle(self, *args, **options):
        data_actual = date.today().strftime("%Y-%m-%d")
        data_anterior = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(
            "%Y-%m-%d"
        )
        hora_actual = int(datetime.datetime.now().strftime("%H"))
        hora_anterior = int(
            (datetime.datetime.now() - datetime.timedelta(hours=1)).strftime("%H")
        )
        minuto_actual = int(datetime.datetime.now().strftime("%M"))
        data_dia_semana = datetime.datetime.today().weekday() + 1

        # se a hora for zero horas, entao a hora anterior é 23h.
        if (hora_actual == 0) and (minuto_actual < 11):
            hora_anterior = 23
            data_actual = data_anterior
            data_dia_semana = datetime.datetime.today().weekday()

        intDiaSemana = str(data_dia_semana)
        getDiaSemanaHoje = Semana.objects.get(descricao=intDiaSemana)

        if True:
            linhasProd = RelatorioProdFttJS.objects.filter(
                Q(data=data_actual)
                & Q(hora=hora_anterior)
                & (Q(auxiliar="1") | Q(auxiliar="2"))
            )
            for x in linhasProd:

                refHora = None
                prodHora = None
                prodDia = None

                if True:
                    try:  # TENTATIVA DE ACEDER AO URL
                        url_js = (
                            "http://10.216.180.225/Termite/Service.svc/OpProdCount/"
                            + x.linha_id
                            + "/"
                            + x.operacao_id
                        )  # link
                        respostaJson = urllib.request.urlopen(
                            url_js
                        )  # faz um pedido ao link
                        objecto = json.load(respostaJson, strict=False)  # guarda

                    except urllib.error.HTTPError as exception:  # CASO EXISTA FALHA NA RESPOSTA DO SERVIDOR
                        logger.info(
                            f"erro: {exception}, {x} "
                        )  # coloca o erro exception no ficheiro log

                    else:  # CASO NAO EXISTA QQ FALHA NA RESPOSTA DO SERVIDOR
                        objAux = objecto[hora_anterior]  # acede ao campo hora_anterior
                        objAux.pop("hour")
                        objAux.pop("target")
                        prodHora = sum(objAux.values())  # PRODUCAO DA HORA ATUAL
                        hora_prodCountString = str(objAux)  # transforma em string
                        hora_prodCountString = hora_prodCountString[1:]
                        refHora = hora_prodCountString[
                            :-1
                        ]  # REF CODES DA HORA ATUAL LIMPOS

                if True:  # existe o lnProd
                    try:
                        url_js = (
                            "http://10.216.180.225/Termite/Service.svc/LnProdCount/"
                            + x.linha_id
                            + "/"
                            + x.operacao_id
                        )
                        respostaJson = urllib.request.urlopen(url_js)
                        objecto = json.load(respostaJson, strict=False)

                    except urllib.error.HTTPError as exception:
                        logger.info(f"erro: {exception}, {x} ")

                    else:
                        prodDia = int(
                            objecto[0]["ProdCount"]
                        )  # TOTAL DE PRODUCAO DIARIA

                linhasProd.filter(pk=x.pk).update(
                    ref_hora=refHora, total_hora=prodHora, total_dia=prodDia
                )
        else:
            logger.info(f"Este Dia Esta OFF na tabela de Semana")
