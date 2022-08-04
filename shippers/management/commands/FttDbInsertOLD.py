from django.core.management.base import BaseCommand, CommandError
from vreport.models import *
from vboard.models import *
from datetime import date, datetime, timedelta
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


# Função que preenche a base de dados com os dados de FTT da Hora Actual (DEVE CORRER AS xxH 59Minutos)
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

        intDiaSemana = str(data_dia_semana)
        getDiaSemanaHoje = Semana.objects.get(descricao=intDiaSemana)

        if True:
            if RelatorioProdFttJS.objects.filter(
                Q(data=data_actual) & Q(hora=hora_actual)
            ).exists():
                apagarObjecto = RelatorioProdFttJS.objects.filter(
                    Q(data=data_actual) & Q(hora=hora_actual)
                )
                apagarObjecto.delete()

            linhasProd = OperacaoLinhaJS.objects.filter(
                Q(activo=True) & (Q(ftt=True) | Q(prod=True))
            )
            for x in linhasProd:

                refHora = None
                prodHora = None
                prodDia = None
                passedFtt = None
                failedFtt = None
                t1Ftt = None
                t2Ftt = None
                t3Ftt = None
                save = True
                horaFtt = None

                if True:
                    try:
                        url_js = (
                            "http://10.216.180.225/Termite/Service.svc/OpFTT/"
                            + x.linha_id
                            + "/"
                            + x.operacao_id
                        )
                        respostaJson = urllib.request.urlopen(url_js)
                        objecto = json.load(respostaJson, strict=False)

                    except urllib.error.HTTPError as exception:
                        logger.info(f"erro: {exception}, {x} ")

                    else:
                        horaFtt = round(
                            Decimal(objecto[0]["FTT"]), 2
                        )  # FTT DA HORA ACTUAL
                        failedFtt = int(objecto[0]["VirginFail"])  # PEÇAS COM FALHA
                        passedFtt = int(objecto[0]["VirginPass"])  # PEÇAS FEITAS
                        if (
                            (horaFtt == 0)
                            and (failedFtt == 0)
                            and (passedFtt == 0)
                            and (x.ftt == True)
                            and (x.prod == False)
                        ):
                            save = False
                            logger.info(f"NAO GUARDAR ESTE OBJECTO: {objecto}{url_js}")
                            continue

                        if (
                            (x.alertaFTT < horaFtt)
                            and (x.ftt == True)
                            and (x.prod == False)
                        ):
                            save = False
                            continue

                if (
                    not save
                ):  # se o save nao for TRUE, o programa salta para o proximo ciclo for.
                    continue

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

                if True:
                    try:
                        url_js = (
                            "http://10.216.180.225/Termite/Service.svc/OpProdCount/"
                            + x.linha_id
                            + "/"
                            + x.operacao_id
                        )  # link da resposta json
                        respostaJson = urllib.request.urlopen(
                            url_js
                        )  # fazer o pedido ao link
                        objecto = json.load(
                            respostaJson, strict=False
                        )  # carregar o json para um objecto

                    except urllib.error.HTTPError as exception:  # caso exista um erro httperror, tratar como excecpcao
                        logger.info(
                            f"erro: {exception}, {x} "
                        )  # escrever dados no log file

                    else:  # escrever dados do objecto captado no log file
                        objAux = objecto[hora_actual]  # aceder ao dado
                        objAux.pop("hour")
                        objAux.pop("target")
                        prodHora = sum(objAux.values())  # PRODUCAO DA HORA ATUAL
                        hora_prodCountString = str(objAux)
                        hora_prodCountString = hora_prodCountString[1:]
                        refHora = hora_prodCountString[
                            :-1
                        ]  # REF CODES DA HORA ATUAL LIMPOS

                if True:
                    try:
                        url_js = (
                            "http://10.216.180.225/Termite/Service.svc/Shift/"
                            + x.linha_id
                            + "/"
                            + x.operacao_id
                        )
                        respostaJson = urllib.request.urlopen(url_js)
                        objecto = json.load(respostaJson, strict=False)

                    except urllib.error.HTTPError as exception:
                        logger.info(f"erro: {exception}, {x} ")

                    else:
                        t1Ftt = round(
                            Decimal(objecto[1]["data"][0]["FTT"]), 2
                        )  # FTT DO TURNO 1
                        t2Ftt = round(Decimal(objecto[2]["data"][0]["FTT"]), 2)
                        t3Ftt = round(Decimal(objecto[1]["data"][0]["FTT"]), 2)

                if horaFtt:
                    if (x.prod == True) and (x.ftt == False):
                        codigo = 1
                    elif (
                        (x.prod == True)
                        and (x.ftt == True)
                        and (horaFtt <= x.alertaFTT)
                    ):
                        codigo = 2
                    elif (
                        (x.prod == False)
                        and (x.ftt == True)
                        and (horaFtt <= x.alertaFTT)
                    ):
                        codigo = 3
                    else:
                        codigo = 0
                else:
                    if (x.prod == True) and (x.ftt == False):
                        codigo = 1
                    elif (x.prod == True) and (x.ftt == True):
                        codigo = 2
                    elif (x.prod == False) and (x.ftt == True):
                        codigo = 3
                    else:
                        codigo = 0

                # apagar os dados anteriores e escrever por cima!
                if codigo > 0:
                    criarObjecto = RelatorioProdFttJS.objects.create(
                        linha=x.linha,
                        data=data_actual,
                        hora=hora_actual,
                        operacao=x.operacao,
                        ref_hora=(f":{refHora}"),
                        total_hora=prodHora,
                        total_dia=prodDia,
                        ftt=horaFtt,
                        passed=passedFtt,
                        failed=failedFtt,
                        t1_ftt=t1Ftt,
                        t2_ftt=t2Ftt,
                        t3_ftt=t3Ftt,
                        auxiliar=codigo,
                    )
                    criarObjecto.save()
        else:
            logger.info(f"Este Dia Esta OFF na tabela de Semana")

        if Schedule_Diaria.objects.filter(
            pk_schedule_global=data_actual
        ).exists():  # EXISTE SCHEDULE HOJE?
            lista_ProdLine = (
                Schedule_Diaria.objects.filter(pk_schedule_global=data_actual)
                .order_by()
                .values("pk_prod_line")
                .distinct()
            )  # Listar todas as entradas do prod line.

            for prodline in lista_ProdLine:  # para cada um dos prod lines de hoje
                if Report_Config_ProdLine.objects.filter(
                    fk_prod_line=prodline["pk_prod_line"]
                ).exists():  # O prod line existe na tabela de configuracao
                    lista_reportProd = Report_Config_ProdLine.objects.filter(
                        fk_prod_line=prodline["pk_prod_line"]
                    )  # lista de todas as entradas referente aquele prod_line

                    for x in lista_reportProd:  # TODOS AS ENTRADAS DESTE PROD LINE
                        relatorioprodlineglobal_prodline = prodline["pk_prod_line"]
                        if (
                            True
                        ):  # SE FOR PROD PRETENDEMOS CONTABILIZAR OS ERROS PERDA/GANHO
                            relatorioprodlinehora_prod = True
                            prodDia = 0
                            prodHora = 0
                            refHora = "P/N"
                            if (
                                LinhaJS.objects.filter(codigo=x.url_line.codigo)
                            ).exists():
                                linha = LinhaJS.objects.get(codigo=x.url_line.codigo)
                                linedesc = linha

                            try:  # TENTATIVA DE ACEDER AO URL
                                url_js = (
                                    x.url_server
                                    + "/OpProdCount/"
                                    + x.url_line.codigo
                                    + "/"
                                    + x.url_operation.codigo
                                )  # link
                                respostaJson = urllib.request.urlopen(
                                    url_js
                                )  # faz um pedido ao link
                                objecto = json.load(
                                    respostaJson, strict=False
                                )  # guarda

                            except urllib.error.HTTPError as exception:  # CASO EXISTA FALHA NA RESPOSTA DO SERVIDOR
                                logger.info(
                                    f"erro: {exception}, {x} "
                                )  # coloca o erro exception no ficheiro log

                            else:  # CASO NAO EXISTA QQ FALHA NA RESPOSTA DO SERVIDOR
                                objAux = objecto[
                                    hora_actual
                                ]  # acede ao campo hora_anterior
                                objAux.pop("hour")
                                objAux.pop("target")
                                prodHora = sum(
                                    objAux.values()
                                )  # PRODUCAO DA HORA ATUAL
                                hora_prodCountString = str(
                                    objAux
                                )  # transforma em string
                                hora_prodCountString = hora_prodCountString[1:]
                                refHora = hora_prodCountString[
                                    :-1
                                ]  # REF CODES DA HORA ATUAL LIMPOS

                            try:
                                url_js = (
                                    x.url_server
                                    + "/LnProdCount/"
                                    + x.url_line.codigo
                                    + "/"
                                    + x.url_operation.codigo
                                )  # link
                                respostaJson = urllib.request.urlopen(url_js)
                                objecto = json.load(respostaJson, strict=False)

                            except urllib.error.HTTPError as exception:
                                logger.info(f"erro: {exception}, {x} ")

                            else:
                                prodDia = int(
                                    objecto[0]["ProdCount"]
                                )  # TOTAL DE PRODUCAO DIARIA

                            fttday = 0

                            # try:
                            #     url_js = x.url_server + "/LnOverview/" + x.url_line.codigo + "/" + x.url_operation.codigo #link
                            #     respostaJson = urllib.request.urlopen(url_js)
                            #     objecto = json.load(respostaJson, strict=False)
                            #
                            # except urllib.error.HTTPError as exception:
                            #     logger.info(f'erro: {exception}, {x} ')
                            #
                            # else:
                            #     linedescr = objecto[0]['LineDesc']  # TOTAL DE PRODUCAO DIARIA
                            #     modeltype =(objecto[0]['ModelType'])
                            #     fttday = float(objecto[0]['FTT_Day'])
                            #     ftthour = float(objecto[0]['FTT_Hour'])

                            # QUANTIDADE QUE TEMOS EM SCHEDULE DESTE PARTNUMBER
                            sched_count = Schedule_Diaria.objects.filter(
                                pk_schedule_global=data_actual
                            ).filter(pk_prod_line=prodline["pk_prod_line"])
                            prod_qty_sched = 0

                            for y in sched_count:
                                prod_qty_sched = (
                                    prod_qty_sched + y.qty_dia
                                )  # quantidade na schedule

                            prod_qty_sched = prod_qty_sched / y.pk_prod_line.num_linhas
                            guardar_dados = True
                            horaZero_manual = False

                            if (
                                (x.turno1 == False)
                                and (x.turno2 == False)
                                and (x.turno3 == False)
                            ):
                                hora_inicio = 0
                                hora_fim = 0
                                tempo_falta = 0
                                tempo_decorrido = 0
                            elif (
                                (x.turno1 == False)
                                and (x.turno2 == False)
                                and (x.turno3 == True)
                            ):
                                hora_inicio = 1
                                hora_fim = 8
                                if hora_actual == 0:
                                    tempo_falta = 0
                                    tempo_decorrido = 0
                                elif hora_actual == 1:
                                    tempo_falta = 7
                                    tempo_decorrido = 0
                                elif hora_actual == 2:
                                    tempo_falta = 6
                                    tempo_decorrido = 1
                                elif hora_actual == 3:
                                    tempo_falta = 5
                                    tempo_decorrido = 2
                                elif hora_actual == 4:
                                    tempo_falta = 4
                                    tempo_decorrido = 3
                                elif hora_actual == 5:
                                    tempo_falta = 3
                                    tempo_decorrido = 4
                                elif hora_actual == 6:
                                    tempo_falta = 2
                                    tempo_decorrido = 5
                                elif hora_actual == 7:
                                    tempo_falta = 1
                                    tempo_decorrido = 6
                                elif hora_actual == 8:
                                    tempo_falta = 0
                                    tempo_decorrido = 7
                                else:
                                    tempo_falta = 0
                                    tempo_decorrido = 7
                            elif (
                                (x.turno1 == False)
                                and (x.turno2 == True)
                                and (x.turno3 == False)
                            ):
                                hora_inicio = 17
                                hora_fim = 1
                                if hora_actual == 0:
                                    tempo_falta = 1
                                    tempo_decorrido = 7.5
                                elif hora_actual == 17:
                                    tempo_falta = 8
                                    tempo_decorrido = 0.5
                                elif hora_actual == 18:
                                    tempo_falta = 7
                                    tempo_decorrido = 1.5
                                elif hora_actual == 19:
                                    tempo_falta = 6
                                    tempo_decorrido = 2.5
                                elif hora_actual == 20:
                                    tempo_falta = 5
                                    tempo_decorrido = 3.5
                                elif hora_actual == 21:
                                    tempo_falta = 4
                                    tempo_decorrido = 4.5
                                elif hora_actual == 22:
                                    tempo_falta = 3
                                    tempo_decorrido = 5.5
                                elif hora_actual == 23:
                                    tempo_falta = 2
                                    tempo_decorrido = 6.5
                                else:
                                    tempo_falta = 0
                                    tempo_decorrido = 0
                            elif (
                                (x.turno1 == False)
                                and (x.turno2 == True)
                                and (x.turno3 == True)
                            ):
                                hora_inicio = 17
                                hora_fim = 8
                                if hora_actual == 17:
                                    tempo_falta = 8
                                    tempo_decorrido = 0.5
                                elif hora_actual == 18:
                                    tempo_falta = 7
                                    tempo_decorrido = 1.5
                                elif hora_actual == 19:
                                    tempo_falta = 6
                                    tempo_decorrido = 2.5
                                elif hora_actual == 20:
                                    tempo_falta = 5
                                    tempo_decorrido = 3.5
                                elif hora_actual == 21:
                                    tempo_falta = 4
                                    tempo_decorrido = 4.5
                                elif hora_actual == 22:
                                    tempo_falta = 3
                                    tempo_decorrido = 5.5
                                elif hora_actual == 23:
                                    tempo_falta = 2
                                    tempo_decorrido = 6.5
                                elif hora_actual == 0:
                                    tempo_falta = 1
                                    tempo_decorrido = 7.5
                                elif hora_actual == 1:
                                    tempo_falta = 7
                                    tempo_decorrido = 0
                                elif hora_actual == 2:
                                    tempo_falta = 6
                                    tempo_decorrido = 1
                                elif hora_actual == 3:
                                    tempo_falta = 5
                                    tempo_decorrido = 2
                                elif hora_actual == 4:
                                    tempo_falta = 4
                                    tempo_decorrido = 3
                                elif hora_actual == 5:
                                    tempo_falta = 3
                                    tempo_decorrido = 4
                                elif hora_actual == 6:
                                    tempo_falta = 2
                                    tempo_decorrido = 5
                                elif hora_actual == 7:
                                    tempo_falta = 1
                                    tempo_decorrido = 6
                                elif hora_actual == 8:
                                    tempo_falta = 0
                                    tempo_decorrido = 7
                                else:
                                    tempo_falta = 0
                            elif (
                                (x.turno1 == True)
                                and (x.turno2 == False)
                                and (x.turno3 == False)
                            ):
                                hora_inicio = 8
                                hora_fim = 17
                                horaZero_manual = True

                                if hora_actual == 8:
                                    tempo_falta = 7.5
                                    tempo_decorrido = 1
                                    guardar_dados = False
                                elif hora_actual == 9:
                                    tempo_falta = 6.5
                                    tempo_decorrido = 2
                                    guardar_dados = True
                                elif hora_actual == 10:
                                    tempo_falta = 5.5
                                    tempo_decorrido = 3
                                    guardar_dados = True
                                elif hora_actual == 11:
                                    tempo_falta = 4.5
                                    tempo_decorrido = 4
                                    guardar_dados = True
                                elif hora_actual == 12:
                                    tempo_falta = 3.5
                                    tempo_decorrido = 5
                                elif hora_actual == 13:
                                    tempo_falta = 2.5
                                    tempo_decorrido = 6
                                    guardar_dados = True
                                elif hora_actual == 14:
                                    tempo_falta = 1.5
                                    tempo_decorrido = 7
                                    guardar_dados = True
                                elif hora_actual == 15:
                                    tempo_falta = 0.5
                                    tempo_decorrido = 8
                                    guardar_dados = True
                                elif hora_actual == 16:
                                    tempo_falta = 0
                                    tempo_decorrido = 8.5
                                    guardar_dados = True
                                elif hora_actual == 17:
                                    tempo_falta = 0
                                    tempo_decorrido = 8.5
                                    guardar_dados = True
                                else:
                                    tempo_falta = 0
                                    tempo_decorrido = 8.5
                                    guardar_dados = False
                            elif (
                                (x.turno1 == True)
                                and (x.turno2 == False)
                                and (x.turno3 == True)
                            ):
                                hora_inicio = 1
                                hora_fim = 17
                                horaZero_manual = True
                                if hora_actual == 1:
                                    tempo_falta = 14.5
                                    tempo_decorrido = 1
                                    guardar_dados = True
                                elif hora_actual == 2:
                                    tempo_falta = 13.5
                                    tempo_decorrido = 2
                                    guardar_dados = True
                                elif hora_actual == 3:
                                    tempo_falta = 12.5
                                    tempo_decorrido = 3
                                    guardar_dados = True
                                elif hora_actual == 4:
                                    tempo_falta = 11.5
                                    tempo_decorrido = 4
                                    guardar_dados = True
                                elif hora_actual == 5:
                                    tempo_falta = 10.5
                                    tempo_decorrido = 5
                                    guardar_dados = True
                                elif hora_actual == 6:
                                    tempo_falta = 9.5
                                    tempo_decorrido = 6
                                    guardar_dados = True
                                elif hora_actual == 7:
                                    tempo_falta = 8.5
                                    tempo_decorrido = 7
                                    guardar_dados = True
                                elif hora_actual == 8:
                                    tempo_falta = 7.5
                                    tempo_decorrido = 8
                                    guardar_dados = True
                                elif hora_actual == 9:
                                    tempo_falta = 6.5
                                    tempo_decorrido = 9
                                    guardar_dados = True
                                elif hora_actual == 10:
                                    tempo_falta = 5.5
                                    tempo_decorrido = 10
                                    guardar_dados = True
                                elif hora_actual == 11:
                                    tempo_falta = 4.5
                                    tempo_decorrido = 11
                                    guardar_dados = True
                                elif hora_actual == 12:
                                    tempo_falta = 3.5
                                    tempo_decorrido = 12
                                    guardar_dados = True
                                elif hora_actual == 13:
                                    tempo_falta = 2.5
                                    tempo_decorrido = 13
                                    guardar_dados = True
                                elif hora_actual == 14:
                                    tempo_falta = 1.5
                                    tempo_decorrido = 14
                                    guardar_dados = True
                                elif hora_actual == 15:
                                    tempo_falta = 0.5
                                    tempo_decorrido = 15
                                    guardar_dados = True
                                elif hora_actual == 16:
                                    tempo_falta = 0
                                    tempo_decorrido = 15.5
                                    guardar_dados = True
                                else:
                                    tempo_falta = 0
                                    tempo_decorrido = 15.5
                                    guardar_dados = False
                            elif (
                                (x.turno1 == True)
                                and (x.turno2 == True)
                                and (x.turno3 == False)
                            ):
                                hora_inicio = 8
                                hora_fim = 1
                                horaZero_manual = False
                                if hora_actual == 8:
                                    tempo_falta = 15
                                    tempo_decorrido = 2
                                    guardar_dados = True
                                elif hora_actual == 9:
                                    tempo_falta = 14
                                    tempo_decorrido = 3
                                    guardar_dados = True
                                elif hora_actual == 10:
                                    tempo_falta = 13
                                    tempo_decorrido = 4
                                    guardar_dados = True
                                elif hora_actual == 11:
                                    tempo_falta = 12
                                    tempo_decorrido = 5
                                    guardar_dados = True
                                elif hora_actual == 12:
                                    tempo_falta = 11
                                    tempo_decorrido = 6
                                    guardar_dados = True
                                elif hora_actual == 13:
                                    tempo_falta = 10
                                    tempo_decorrido = 7
                                    guardar_dados = True
                                elif hora_actual == 14:
                                    tempo_falta = 9
                                    tempo_decorrido = 8
                                    guardar_dados = True
                                elif hora_actual == 15:
                                    tempo_falta = 8
                                    tempo_decorrido = 9
                                    guardar_dados = True
                                elif hora_actual == 16:
                                    tempo_falta = 7
                                    tempo_decorrido = 10
                                    guardar_dados = True
                                elif hora_actual == 17:
                                    tempo_falta = 6
                                    tempo_decorrido = 11
                                    guardar_dados = True
                                elif hora_actual == 18:
                                    tempo_falta = 5
                                    tempo_decorrido = 12
                                    guardar_dados = True
                                elif hora_actual == 19:
                                    tempo_falta = 4
                                    tempo_decorrido = 13
                                    guardar_dados = True
                                elif hora_actual == 20:
                                    tempo_falta = 3
                                    tempo_decorrido = 14
                                    guardar_dados = True
                                elif hora_actual == 21:
                                    tempo_falta = 2
                                    tempo_decorrido = 15
                                    guardar_dados = True
                                elif hora_actual == 22:
                                    tempo_falta = 1
                                    tempo_decorrido = 16
                                    guardar_dados = True
                                elif hora_actual == 23:
                                    tempo_falta = 0
                                    tempo_decorrido = 17
                                    guardar_dados = True
                                elif hora_actual == 0:
                                    tempo_falta = 16
                                    tempo_decorrido = 1
                                    guardar_dados = True
                                else:
                                    tempo_falta = 0
                                    tempo_decorrido = 16
                                    guardar_dados = False
                            elif (
                                (x.turno1 == True)
                                and (x.turno2 == True)
                                and (x.turno3 == True)
                            ):
                                hora_inicio = 0
                                hora_fim = 0
                                guardar_dados = True
                                horaZero_manual = False

                                if hora_actual == 0:
                                    tempo_falta = 23
                                    tempo_decorrido = 1
                                elif hora_actual == 1:
                                    tempo_falta = 22
                                    tempo_decorrido = 2
                                elif hora_actual == 2:
                                    tempo_falta = 21
                                    tempo_decorrido = 3
                                elif hora_actual == 3:
                                    tempo_falta = 20
                                    tempo_decorrido = 4
                                elif hora_actual == 4:
                                    tempo_falta = 19
                                    tempo_decorrido = 5
                                elif hora_actual == 5:
                                    tempo_falta = 18
                                    tempo_decorrido = 6
                                elif hora_actual == 6:
                                    tempo_falta = 17
                                    tempo_decorrido = 7
                                elif hora_actual == 7:
                                    tempo_falta = 16
                                    tempo_decorrido = 8
                                elif hora_actual == 8:
                                    tempo_falta = 15
                                    tempo_decorrido = 9
                                elif hora_actual == 9:
                                    tempo_falta = 14
                                    tempo_decorrido = 10
                                elif hora_actual == 10:
                                    tempo_falta = 13
                                    tempo_decorrido = 11
                                elif hora_actual == 11:
                                    tempo_falta = 12
                                    tempo_decorrido = 12
                                elif hora_actual == 12:
                                    tempo_falta = 11
                                    tempo_decorrido = 13
                                elif hora_actual == 13:
                                    tempo_falta = 10
                                    tempo_decorrido = 14
                                elif hora_actual == 14:
                                    tempo_falta = 9
                                    tempo_decorrido = 15
                                elif hora_actual == 15:
                                    tempo_falta = 8
                                    tempo_decorrido = 16
                                elif hora_actual == 16:
                                    tempo_falta = 7
                                    tempo_decorrido = 17
                                elif hora_actual == 17:
                                    tempo_falta = 6
                                    tempo_decorrido = 18
                                elif hora_actual == 18:
                                    tempo_falta = 5
                                    tempo_decorrido = 19
                                elif hora_actual == 19:
                                    tempo_falta = 4
                                    tempo_decorrido = 20
                                elif hora_actual == 20:
                                    tempo_falta = 3
                                    tempo_decorrido = 21
                                elif hora_actual == 21:
                                    tempo_falta = 2
                                    tempo_decorrido = 22
                                elif hora_actual == 22:
                                    tempo_falta = 1
                                    tempo_decorrido = 23
                                elif hora_actual == 23:
                                    tempo_falta = 0
                                    tempo_decorrido = 24

                            # SE NAO EXISTIR O RELATORIOPRODLINE_GLOBAL CRIAR:
                            if (
                                RelatorioProdLine_Global.objects.filter(
                                    pk_schedule_global_id=data_actual,
                                    pk_prod_line_id=prodline["pk_prod_line"],
                                    nome_linha=linedesc,
                                ).exists()
                            ) and guardar_dados:
                                b = RelatorioProdLine_Global.objects.get(
                                    pk_schedule_global_id=data_actual,
                                    pk_prod_line_id=prodline["pk_prod_line"],
                                    nome_linha=linedesc,
                                )
                                b.qty_total_prod_line = prod_qty_sched
                                b.ftt_day = fttday
                                b.active = x.prod
                                b.last_hour = prodHora
                                b.save()

                            elif guardar_dados:
                                b = RelatorioProdLine_Global.objects.create(
                                    pk_schedule_global_id=data_actual,
                                    pk_prod_line_id=prodline["pk_prod_line"],
                                    nome_linha=linedesc,
                                    qty_total_prod_line=prod_qty_sched,
                                    ftt_day=fttday,
                                    active=x.prod,
                                    horaZero_manual=horaZero_manual,
                                    last_hour=prodHora,
                                )

                            if RelatorioProdLine_Hora.objects.filter(
                                pk_relatorioprodLine_global=b, hora=hora_actual
                            ).exists():  # UPDATE HORA ANTERIOR
                                d = RelatorioProdLine_Hora.objects.get(
                                    pk_relatorioprodLine_global=b, hora=hora_actual
                                )
                                d.prod_hora = prodHora
                                d.ref_codes_hora = refHora
                                d.save()
                            else:  # CRIAR ENTRADA NA HORA ANTERIOR
                                d = RelatorioProdLine_Hora.objects.create(
                                    pk_relatorioprodLine_global=b,
                                    hora=hora_actual,
                                    prod_hora=prodHora,
                                    ref_codes_hora=refHora,
                                    prod_failed=0,
                                    prod_passed=0,
                                    ftt_hora=0,
                                )

                            if RelatorioProdLine_Hora.objects.filter(
                                pk_relatorioprodLine_global=b, hora=0
                            ).exists():  # SE EXISTIR HORA ZERO IR BUSCAR ESSE VALOR!
                                c = RelatorioProdLine_Hora.objects.get(
                                    pk_relatorioprodLine_global=b, hora=0
                                )
                                horaZero = c.prod_hora
                            else:
                                horaZero = 0

                            b.qty_prod_dia = prodDia + horaZero
                            qtyFaltaProduzir = b.qty_total_prod_line - b.qty_prod_dia
                            b.qty_falta = qtyFaltaProduzir
                            b.save()

                            # calculo da perda estimada:
                            # OLD mediaProduzida = b.qty_prod_dia / tempo_decorrido
                            mediaProduzida = x.output_estimado
                            if tempo_falta > 0:
                                necessarioProduzir = qtyFaltaProduzir / tempo_falta
                            else:
                                necessarioProduzir = 0

                            estimativaProduzir = mediaProduzida * tempo_falta
                            percaProducao = qtyFaltaProduzir - estimativaProduzir

                            b.total_perda_estimada = int(percaProducao)
                            b.total_dia_garantido = int(estimativaProduzir)
                            if tempo_falta > 0:
                                b.qty_hora_cumprir_schedule = int(
                                    qtyFaltaProduzir / tempo_falta
                                )
                            b.save()

                        else:  # se nao for prod, vamos verificar os dados de ftt da hora
                            flag_perdaHora = False

                else:  # nao existe na tabela de configuracao de prod line
                    continue

        else:
            print("Teste")
