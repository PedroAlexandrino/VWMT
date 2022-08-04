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
        data_ontem = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        hora_actual = int(datetime.datetime.now().strftime("%H"))
        hora_anterior = int(
            (datetime.datetime.now() - datetime.timedelta(hours=1)).strftime("%H")
        )
        data_actual_date = date.today()
        hora_actual = int(datetime.datetime.now().strftime("%H"))
        hora_actual_datetime = datetime.datetime.now()
        data_hora_query = hora_actual_datetime - timedelta(hours=0, minutes=25)
        data_zero = datetime.datetime(
            data_actual_date.year, data_actual_date.month, data_actual_date.day, 0, 5, 1
        )
        data_agora = datetime.datetime.now()

        if (
            data_agora < data_zero
        ):  # SE FOR ANTES DAS 0h5minutos eu vou olhar para o dia anterior
            data_actual = data_ontem

        # 1) Ir a schedule e buscar os prod lines disponiveis
        sd_hoje = Schedule_Diaria.objects.filter(pk_schedule_global=data_actual)
        if sd_hoje.exists():  # EXISTE SCHEDULE HOJE?
            todosReportProdLine = (
                Report_Config_ProdLine.objects.all()
            )  # todas as linhas da configuracao do sistema
            for x1 in todosReportProdLine:
                if not x1.prod:  # se tiver off
                    continue

                sd_hoje_prodline = sd_hoje.filter(
                    pk_prod_line=x1.fk_prod_line
                )  # Listar todas as entradas do prod line.
                if sd_hoje_prodline:  # se existir entradas no prodline
                    # vou buscar a db do CimpleInfo
                    ci = CimpleInfo.objects.filter(
                        line=x1.url_line, operacao=x1.url_operation
                    ).last()
                    if not ci:
                        continue

                    qty_sched_prodline = 0
                    for (
                        prodline
                    ) in (
                        sd_hoje_prodline
                    ):  # para cada um dos partnumbers deste prodline
                        qty_sched_prodline = qty_sched_prodline + prodline.qty_dia

                    qty_prodline = (
                        qty_sched_prodline / x1.fk_prod_line.num_linhas
                    )  # VAR QTY SCHEDULE DA LINHA

                    # calculo do tempo que falta: ATENCAO NAO ESTA CONTEMPLADO AINDA QUANDO O TURNO 1 É FALSE
                    if (
                        (x1.turno1 == True)
                        and (x1.turno2 == False)
                        and (x1.turno3 == False)
                    ):
                        data_inicio = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            8,
                            0,
                            0,
                        )
                        data_fim = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            16,
                            29,
                            59,
                        )
                        if (
                            ci.data_hora < data_inicio
                        ):  # se a hora actual for menor que a hora de inicio: exemplo:
                            time_elapsed = data_actual_date - data_actual_date
                            time_remaining = data_fim - data_inicio
                        elif ci.data_hora > data_fim:  # 16h59.50 > 16h
                            time_elapsed = data_fim - data_inicio
                            time_remaining = data_actual_date - data_actual_date
                        else:
                            time_elapsed = ci.data_hora - data_inicio
                            time_remaining = data_fim - ci.data_hora

                    elif (
                        (x1.turno1 == True)
                        and (x1.turno2 == False)
                        and (x1.turno3 == True)
                    ):
                        data_inicio = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            1,
                            0,
                            0,
                        )
                        data_fim = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            16,
                            29,
                            59,
                        )
                        if (
                            ci.data_hora < data_inicio
                        ):  # se a hora actual for menor que a hora de inicio:
                            time_elapsed = data_actual_date - data_actual_date
                            time_remaining = data_fim - data_inicio
                        elif ci.data_hora > data_fim:
                            time_elapsed = data_fim - data_inicio
                            time_remaining = data_actual_date - data_actual_date
                        else:
                            time_elapsed = ci.data_hora - data_inicio
                            time_remaining = data_fim - ci.data_hora

                    elif (
                        (x1.turno1 == True)
                        and (x1.turno2 == True)
                        and (x1.turno3 == False)
                    ):
                        # INICIA AS 0H, ACABA AS 1H.
                        data_zero = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            0,
                            5,
                            1,
                        )
                        data_zero_inicio = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            0,
                            0,
                            0,
                        )
                        data_zero_fim = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            0,
                            59,
                            59,
                        )
                        data_inicio = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            8,
                            0,
                            0,
                        )
                        data_fim = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            23,
                            59,
                            59,
                        )
                        # verificar se estamos entre a hora zero:

                        if (
                            data_agora < data_zero
                        ):  # a data actual é 0h02m e este valor é inferior a dataZero
                            # entao eu pretendo os dados do dia anterior!
                            time_elapsed = data_fim - data_inicio
                            time_remaining = (
                                data_fim - data_fim
                            )  # vai dizer que faltam 16h

                        elif data_zero_inicio <= ci.data_hora <= data_zero_fim:
                            # neste caso sei que tenho uma entrada as 0h59
                            time_elapsed = ci.data_hora - data_zero_inicio
                            time_remaining = (
                                data_fim - data_inicio
                            )  # vai dizer que faltam 16h
                        elif (
                            ci.data_hora < data_inicio
                        ):  # se a hora actual for menor que a hora de inicio:
                            time_elapsed = data_zero_fim - data_zero_inicio
                            time_remaining = data_fim - data_inicio
                        else:  # estou dentro das 8h as 24h
                            time_elapsed = (data_zero_fim - data_zero_inicio) + (
                                ci.data_hora - data_inicio
                            )
                            time_remaining = data_fim - ci.data_hora

                    elif (
                        (x1.turno1 == True)
                        and (x1.turno2 == True)
                        and (x1.turno3 == True)
                    ):
                        data_inicio = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            0,
                            0,
                            0,
                        )
                        data_fim = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            23,
                            59,
                            59,
                        )
                        if (
                            ci.data_hora < data_inicio
                        ):  # se a hora actual for menor que a hora de inicio:
                            time_elapsed = data_actual_date - data_actual_date
                            time_remaining = data_fim - data_inicio
                        elif ci.data_hora > data_fim:
                            time_elapsed = data_fim - data_inicio
                            time_remaining = data_actual_date - data_actual_date
                        else:
                            time_elapsed = ci.data_hora - data_inicio
                            time_remaining = data_fim - ci.data_hora

                    elif (
                        (x1.turno1 == False)
                        and (x1.turno2 == False)
                        and (x1.turno3 == False)
                    ):
                        data_inicio = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            8,
                            0,
                            0,
                        )
                        data_fim = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            23,
                            59,
                            59,
                        )
                        time_elapsed = data_fim - data_fim
                        time_remaining = data_fim - data_fim

                    elif (
                        (x1.turno1 == False)
                        and (x1.turno2 == False)
                        and (x1.turno3 == True)
                    ):
                        data_inicio = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            1,
                            0,
                            0,
                        )
                        data_fim = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            7,
                            59,
                            59,
                        )
                        if (
                            ci.data_hora < data_inicio
                        ):  # se a hora actual for menor que a hora de inicio:
                            time_elapsed = data_actual_date - data_actual_date
                            time_remaining = data_fim - data_inicio
                        elif ci.data_hora > data_fim:
                            time_elapsed = data_fim - data_inicio
                            time_remaining = data_actual_date - data_actual_date
                        else:
                            time_elapsed = ci.data_hora - data_inicio
                            time_remaining = data_fim - ci.data_hora

                    elif (
                        (x1.turno1 == False)
                        and (x1.turno2 == True)
                        and (x1.turno3 == False)
                    ):
                        data_zero = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            0,
                            5,
                            1,
                        )
                        data_zero_inicio = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            0,
                            0,
                            0,
                        )
                        data_zero_fim = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            0,
                            59,
                            59,
                        )
                        data_inicio = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            16,
                            30,
                            0,
                        )
                        data_fim = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            23,
                            59,
                            59,
                        )
                        # verificar se estamos entre a hora zero:

                        if (
                            data_agora < data_zero
                        ):  # a data actual é 0h02m e este valor é inferior a dataZero
                            # entao eu pretendo os dados do dia anterior!
                            time_elapsed = data_fim - data_inicio
                            time_remaining = (
                                data_fim - data_fim
                            )  # vai dizer que faltam 16h

                        elif (
                            ci.data_hora < data_zero_fim
                        ):  # A data ci é 0h59 e a data fim é 1h
                            # neste caso sei que tenho uma entrada as 0h59
                            time_elapsed = ci.data_hora - data_zero_inicio
                            time_remaining = (
                                data_fim - data_inicio
                            )  # vai dizer que faltam 16h

                        elif ci.data_hora < data_inicio:
                            time_elapsed = data_zero_fim - data_zero_inicio
                            time_remaining = data_fim - data_inicio

                        else:
                            time_elapsed = (data_zero_fim - data_zero_inicio) + (
                                ci.data_hora - data_inicio
                            )
                            time_remaining = data_fim - ci.data_hora

                    elif (
                        (x1.turno1 == False)
                        and (x1.turno2 == True)
                        and (x1.turno3 == True)
                    ):
                        data_zero = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            0,
                            5,
                            1,
                        )
                        data_zero_inicio = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            0,
                            0,
                            0,
                        )
                        data_zero_fim = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            7,
                            59,
                            59,
                        )
                        data_inicio = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            16,
                            30,
                            0,
                        )
                        data_fim = datetime.datetime(
                            data_actual_date.year,
                            data_actual_date.month,
                            data_actual_date.day,
                            23,
                            59,
                            59,
                        )
                        # verificar se estamos entre a hora zero:

                        if (
                            data_agora < data_zero
                        ):  # a data actual é 0h02m e este valor é inferior a dataZero
                            # entao eu pretendo os dados do dia anterior!
                            time_elapsed = data_fim - data_inicio
                            time_remaining = (
                                data_fim - data_fim
                            )  # vai dizer que faltam 16h

                        elif (
                            ci.data_hora < data_zero_fim
                        ):  # A data ci é 0h59 e a data fim é 1h
                            # neste caso sei que tenho uma entrada as 0h59
                            time_elapsed = ci.data_hora - data_zero_inicio
                            time_remaining = (
                                data_fim - data_inicio
                            )  # vai dizer que faltam 16h

                        elif ci.data_hora < data_inicio:
                            time_elapsed = data_zero_fim - data_zero_inicio
                            time_remaining = data_fim - data_inicio

                        else:
                            time_elapsed = (data_zero_fim - data_zero_inicio) + (
                                ci.data_hora - data_inicio
                            )
                            time_remaining = data_fim - ci.data_hora

                    RelProdGlobal = RelatorioProdLine_Global.objects.filter(
                        pk_schedule_global_id=data_actual,
                        pk_prod_line_id=x1.fk_prod_line,
                        nome_linha=x1.url_line,
                    )
                    if RelProdGlobal.exists():
                        RelProdGlobal = RelatorioProdLine_Global.objects.filter(
                            pk_schedule_global_id=data_actual,
                            pk_prod_line_id=x1.fk_prod_line,
                            nome_linha=x1.url_line,
                        ).last()
                        RelProdHoraAnterior = RelatorioProdLine_Hora.objects.filter(
                            pk_relatorioprodLine_global=RelProdGlobal,
                            hora=hora_anterior,
                        )
                        if not RelProdHoraAnterior.exists():
                            RelatorioProdLine_Hora.objects.create(
                                pk_relatorioprodLine_global=RelProdGlobal,
                                hora=hora_anterior,
                                ref_codes_hora=ci.refHora,
                                prod_hora=ci.prodHora,
                            )

                        RelProdHoraActualZero = RelatorioProdLine_Hora.objects.filter(
                            pk_relatorioprodLine_global=RelProdGlobal, hora=0
                        )
                        if (
                            RelProdHoraActualZero.exists()
                        ):  # caso exista a hora zero, temos que ter em consideraçao esta hora nas contas
                            prodHoraZero = RelProdHoraActualZero.prod_hora
                        else:
                            prodHoraZero = 0

                        # qty da schedule em falta:   qty_falta
                        QTY_FALTA_PRODLINE = qty_prodline - prodHoraZero - ci.prodDia
                        # qty por hora para cumprir a schedule:   qty_hora_cumprir_schedule
                        if time_remaining.seconds == 0:
                            QTY_HORA_PARA_SCHEDULE = 0
                            ESTIMATIVA_PRODUCAO = 0
                        elif QTY_FALTA_PRODLINE < 0:
                            QTY_HORA_PARA_SCHEDULE = 0
                            ESTIMATIVA_PRODUCAO = 0
                        else:
                            QTY_HORA_PARA_SCHEDULE = (
                                QTY_FALTA_PRODLINE * 3600
                            ) / time_remaining.seconds
                            ESTIMATIVA_PRODUCAO = (
                                x1.output_estimado * time_remaining.seconds
                            ) / 3600

                        PERDA = QTY_FALTA_PRODLINE - ESTIMATIVA_PRODUCAO
                        if PERDA < 0:
                            PERDA = 0

                        RelatorioProdLine_Global.objects.filter(
                            pk_schedule_global_id=data_actual,
                            pk_prod_line_id=x1.fk_prod_line,
                            nome_linha=x1.url_line,
                        ).update(
                            qty_total_prod_line=qty_prodline,
                            qty_prod_dia=ci.prodDia,
                            qty_falta=QTY_FALTA_PRODLINE,
                            total_perda_estimada=PERDA,
                            total_dia_garantido=ESTIMATIVA_PRODUCAO,
                            qty_hora_cumprir_schedule=QTY_HORA_PARA_SCHEDULE,
                            last_hour=ci.prodHora,
                            active=True,
                        )

                    else:  # ainda nao existe esta entrada na base de dados do REL PROD GLOBAL
                        prodHoraZero = 0
                        # qty da schedule em falta:
                        QTY_FALTA_PRODLINE = qty_prodline - prodHoraZero - ci.prodDia

                        # qty por hora para cumprir a schedule:   qty_hora_cumprir_schedule
                        if time_remaining.seconds == 0:
                            QTY_HORA_PARA_SCHEDULE = 0
                            ESTIMATIVA_PRODUCAO = 0
                        elif QTY_FALTA_PRODLINE < 0:
                            QTY_HORA_PARA_SCHEDULE = 0
                            ESTIMATIVA_PRODUCAO = 0
                        else:
                            QTY_HORA_PARA_SCHEDULE = round(
                                (QTY_FALTA_PRODLINE * 3600) / time_remaining.seconds
                            )
                            ESTIMATIVA_PRODUCAO = round(
                                (x1.output_estimado * 3600) / time_remaining.seconds
                            )

                        PERDA = round(QTY_FALTA_PRODLINE - ESTIMATIVA_PRODUCAO)
                        if PERDA < 0:
                            PERDA = 0

                        RelProdGlobal1 = RelatorioProdLine_Global.objects.create(
                            pk_schedule_global_id=data_actual,
                            pk_prod_line=x1.fk_prod_line,
                            nome_linha=x1.url_line,
                            qty_total_prod_line=qty_prodline,
                            qty_prod_dia=ci.prodDia,
                            qty_falta=QTY_FALTA_PRODLINE,
                            total_perda_estimada=PERDA,
                            total_dia_garantido=ESTIMATIVA_PRODUCAO,
                            qty_hora_cumprir_schedule=QTY_HORA_PARA_SCHEDULE,
                            last_hour=ci.prodHora,
                            active=True,
                        )
                        RelatorioProdLine_Hora.objects.create(
                            pk_relatorioprodLine_global=RelProdGlobal1,
                            hora=hora_anterior,
                            ref_codes_hora=ci.refHora,
                            prod_hora=ci.prodHora,
                        )
                else:
                    continue
