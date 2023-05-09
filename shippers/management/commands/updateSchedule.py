import datetime

import openpyxl
from django.core.management import BaseCommand

from crossdocking.models import *


# Função Principal para envio dos emails
# Utilizar o task scheduler do windows, e nas acçoes colocar:
# Program/script: cmd
# Add arguments (optional): /c batch_vproject_email.bat
# Start in(optional): C:\visteon\shippers\management\commands
class Command(BaseCommand):
    def handle(self, *args, **options):
        prodline = Prodlines.objects

        day = datetime.datetime.today()

        if day.strftime("%A") != "Saturday" and day.strftime("%A") != "Sunday":
            mes = day.strftime("%m")
            if mes == "01":
                mes = "Janeiro"
            if mes == "02":
                mes = "Fevereiro"
            if mes == "03":
                mes = "Março"
            if mes == "04":
                mes = "Abril"
            if mes == "05":
                mes = "Maio"
            if mes == "06":
                mes = "Junho"
            if mes == "07":
                mes = "Julho"
            if mes == "08":
                mes = "Agosto"
            if mes == "09":
                mes = "Setembro"
            if mes == "10":
                mes = "Outubro"
            if mes == "11":
                mes = "Novembro"
            if mes == "12":
                mes = "Dezembro"
                
            #BUG FILESYS Substituir por tabela da base de dados
            textPath = (    
                "//PAVPD002/E_Proj/sharedir/MP&L/Schedule/"
                + day.strftime("%Y")
                + "/"
                + mes
                + " "
                + day.strftime("%Y")
                + "/Daily_Schedule_"
                + day.strftime("%d.%m.%Y")
                + ".xlsx"
            )

            # textPath = '//PAVPD002/E_Proj/sharedir/MP&L/Schedule/2021/Novembro 2021/Daily_Schedule_03.11.2021.xlsx'

            # guarda elementos do dia anterior na tabela histórico
            elementosDiaAnterior = ProdlineTable.objects
            for elem in elementosDiaAnterior.all():
                novoElem = ProdlineTableHistory(
                    None,
                    elem.day,
                    elem.line,
                    elem.site,
                    elem.due_date,
                    elem.item_number,
                    elem.description,
                    elem.to_complete,
                    elem.receiving,
                    elem.allOkReceiving,
                    elem.comentarioReceiving,
                    elem.shipping,
                    elem.allOkShipping,
                    elem.comentarioShipping,
                )
                novoElem.save()

            # limpa a tabela provisória
            ProdlineTable.objects.filter().delete()

            workbook = openpyxl.load_workbook(textPath)
            try:
                worksheet = workbook["Schedule Data"]
                for element in worksheet:
                    for prod in prodline.all():
                        if prod.nome == element[0].value:
                            novo = ProdlineTable(
                                None,
                                day.strftime("%d-%m-%Y"),
                                element[0].value,
                                element[1].value,
                                str(element[2].value),
                                element[3].value,
                                element[4].value,
                                str(element[5].value),
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                            )
                            novo.save()
            except:
                worksheet = workbook["Sheet1"]
                for element in worksheet:
                    for prod in prodline.all():
                        if prod.nome == element[0].value:
                            novo = ProdlineTable(
                                None,
                                day.strftime("%d-%m-%Y"),
                                element[0].value,
                                element[1].value,
                                str(element[2].value),
                                element[3].value,
                                element[4].value,
                                str(element[5].value),
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                            )
                            novo.save()
