from django.core.management.base import BaseCommand, CommandError
from vreport.models import *
from vboard.models import *
from datetime import date, datetime, timedelta
import datetime
from decimal import Decimal
import json
import urllib.request
from urllib import error


# Função que preenche a base de dados com os dados de FTT da Hora Actual (DEVE CORRER AS xxH 59Minutos)
# Utilizar o task scheduler do windows, e nas acçoes colocar:
# Program/script: cmd         Add arguments (optional): /c batch_vreport_clopes4.bat         Start in(optional): C:\visteon\vreport\management\commands


class Command(BaseCommand):

    # Objectivo é colocar todas as informaçoes de ftts na base de dados.
    # Verificar na base de dados todos os items que estejam activos.

    def handle(self, *args, **options):

        if True:
            hora_actual = int(datetime.datetime.now().strftime("%H"))
            hora_actual_datetime = datetime.datetime.now()

            queryReportConfig = Report_Config_ProdLine.objects.filter(prod=True)
            for x in queryReportConfig:

                if True:
                    try:
                        url_js = (
                            "http://10.216.180.225/Termite/Service.svc/OpFTT/"
                            + x.url_line_id
                            + "/"
                            + x.url_operation_id
                        )
                        respostaJson = urllib.request.urlopen(url_js)
                        objecto = json.load(respostaJson, strict=False)

                    except urllib.error.HTTPError as exception:
                        horaFtt = 0
                        failedFtt = 0
                        passedFtt = 0

                    else:
                        horaFtt = round(
                            Decimal(objecto[0]["FTT"]), 2
                        )  # FTT DA HORA ACTUAL
                        failedFtt = int(objecto[0]["VirginFail"])  # PEÇAS COM FALHA
                        passedFtt = int(objecto[0]["VirginPass"])  # PEÇAS FEITAS

                if True:  # existe o lnProd
                    try:
                        url_js = (
                            "http://10.216.180.225/Termite/Service.svc/LnProdCount/"
                            + x.url_line_id
                            + "/"
                            + x.url_operation_id
                        )
                        respostaJson = urllib.request.urlopen(url_js)
                        objecto = json.load(respostaJson, strict=False)
                    except urllib.error.HTTPError as exception:
                        prodDia = 0
                    else:
                        prodDia = int(
                            objecto[0]["ProdCount"]
                        )  # TOTAL DE PRODUCAO DIARIA

                if True:
                    try:
                        url_js = (
                            "http://10.216.180.225/Termite/Service.svc/OpProdCount/"
                            + x.url_line_id
                            + "/"
                            + x.url_operation_id
                        )  # link da resposta json
                        respostaJson = urllib.request.urlopen(
                            url_js
                        )  # fazer o pedido ao link
                        objecto = json.load(
                            respostaJson, strict=False
                        )  # carregar o json para um objecto

                    except urllib.error.HTTPError as exception:  # caso exista um erro httperror, tratar como excecpcao
                        refHora = "FAILED: EXCECPT ERROR"
                        prodHora = 0

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

                # if False:  # nao pretendo os dados dos turnos
                #     try:
                #         url_js = "http://10.216.180.225/Termite/Service.svc/Shift/" + x.url_line_id + "/" + x.url_operation_id
                #         respostaJson = urllib.request.urlopen(url_js)
                #         objecto = json.load(respostaJson, strict=False)
                #     except urllib.error.HTTPError as exception:
                #         logger.info(f'erro: {exception}, {x} ')
                #     else:
                #         t1Ftt = round(Decimal(objecto[1]['data'][0]['FTT']), 2)  # FTT DO TURNO 1
                #         t2Ftt = round(Decimal(objecto[2]['data'][0]['FTT']), 2)
                #         t3Ftt = round(Decimal(objecto[1]['data'][0]['FTT']), 2)

                CimpleInfo.objects.create(
                    data_hora=datetime.datetime.now(),
                    line=x.url_line,
                    operacao=x.url_operation,
                    prodHora=prodHora,
                    refHora=refHora,
                    prodDia=prodDia,
                )
