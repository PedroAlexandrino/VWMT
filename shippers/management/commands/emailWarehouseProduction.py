import datetime

import openpyxl
from django.core.mail import EmailMultiAlternatives
from django.core.management import BaseCommand

from crossdocking.models import *


# Função Principal para envio dos emails
# Utilizar o task scheduler do windows, e nas acçoes colocar:
# Program/script: cmd
# Add arguments (optional): /c batch_vproject_email.bat
# Start in(optional): C:\visteon\vproject\management\commands
from qad_ee.models import WoMstr


class Command(BaseCommand):
    def handle(self, *args, **options):
        timeNow = datetime.datetime.now()
        timeEnd = timeNow.replace(hour=8, minute=10)
        timeBefore = timeNow.replace(hour=7, minute=55)
        timeEnd2 = timeNow.replace(hour=16, minute=10)
        timeBefore2 = timeNow.replace(hour=15, minute=55)
        timeEnd3 = timeNow.replace(hour=22, minute=10)
        timeBefore3 = timeNow.replace(hour=21, minute=55)

        dadosQAD = WoMstr.objects.values(
            "wo_due_date", "wo_part", "wo_qty_exp_complete", "wo_qty_comp"
        )

        prodline = Prodlines.objects
        elementosDiaSeguinte = ProdlineTable.objects
        actualDay = datetime.datetime.today()
        nextDay = datetime.datetime.today() + datetime.timedelta(days=1)
        if nextDay.strftime("%A") == "Saturday":
            nextDay = datetime.datetime.today() + datetime.timedelta(days=3)
        if nextDay.strftime("%A") == "Sunday":
            nextDay = datetime.datetime.today() + datetime.timedelta(days=2)
        mes = nextDay.strftime("%m")
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
        mensagem = ""
        textPath = (
            "//PAVPD002/E_Proj/sharedir/MP&L/Schedule/"
            + nextDay.strftime("%Y")
            + "/"
            + mes
            + " "
            + nextDay.strftime("%Y")
            + "/Daily_Schedule_"
            + nextDay.strftime("%d.%m.%Y")
            + ".xlsx"
        )

        # textPath = '//PAVPD002/E_Proj/sharedir/MP&L/Schedule/2021/Novembro 2021/Daily_Schedule_03.11.2021.xlsx'

        table = '</br><table class="display"><thead style="background-color: lightgray"><tr><th>Line</th><th>Site</th><th>Due Date</th><th>Item Number</th><th>Description</th><th>To Complete</th><th>Receiving</th><th>Comentário Receiving</th><th>Shipping</th><th>Comentário Shipping</th></tr></thead><tbody>'

        if (
            (timeNow < timeEnd and timeNow > timeBefore)
            and (actualDay.strftime("%A") != "Saturday")
            and (actualDay.strftime("%A") != "Sunday")
        ):
            table = '</br><table class="display"><thead style="background-color: lightgray"><tr><th>Line</th><th>Site</th><th>Due Date</th><th>Item Number</th><th>Description</th><th>To Complete</th></tr></thead><tbody>'
            try:
                workbook = openpyxl.load_workbook(textPath)
                try:
                    worksheet = workbook["Schedule Data"]
                    for element in worksheet:
                        for prod in prodline.all():
                            if prod.nome == element[0].value:
                                table += (
                                    '<tr><td style="padding:0 15px 0 15px;">'
                                    + element[0].value
                                    + '</td><td style="padding:0 15px 0 15px;">'
                                    + element[1].value
                                    + '</td><td style="padding:0 15px 0 15px;">'
                                    + str(element[2].value)
                                    + '</td><td style="padding:0 15px 0 15px;">'
                                    + element[3].value
                                    + '</td><td style="padding:0 15px 0 15px;">'
                                    + element[4].value
                                    + '</td><td style="padding:0 15px 0 15px;">'
                                    + str(element[5].value)
                                    + "</td></tr>"
                                )

                    table += "</tbody></table>"
                    table += "</br></br><b>Prodlines</b></br>"
                    for prod in prodline.all():
                        table += prod.nome + "</br>"

                    table += (
                        "</b></b></br><b>Ficheiro diário de Schedule em: </b>"
                        + textPath
                    )

                    subject, from_email, to = (
                        "Wh Production " + nextDay.strftime("%d-%m-%Y"),
                        "noreply@visteon.com",
                        [
                            "npires2@visteon.com",
                            "abrandao@visteon.com",
                            "aroque1@visteon.com",
                            "sanasta1@visteon.com",
                            "rsalgue2@visteon.com",
                            "nlopes8@visteon.com",
                            "abilro1@visteon.com",
                            "jrodri80@visteon.com",
                            "evenanc1@visteon.com",
                        ],
                    )
                    msg = EmailMultiAlternatives(subject, table, from_email, to)
                    msg.attach_alternative(table, "text/html")
                    msg.send()
                except:
                    try:
                        worksheet = workbook["Sheet1"]
                        for element in worksheet:
                            for prod in prodline.all():
                                if prod.nome == element[0].value:
                                    table += (
                                        '<tr><td style="padding:0 15px 0 15px;">'
                                        + element[0].value
                                        + '</td><td style="padding:0 15px 0 15px;">'
                                        + element[1].value
                                        + '</td><td style="padding:0 15px 0 15px;">'
                                        + str(element[2].value)
                                        + '</td><td style="padding:0 15px 0 15px;">'
                                        + element[3].value
                                        + '</td><td style="padding:0 15px 0 15px;">'
                                        + element[4].value
                                        + '</td><td style="padding:0 15px 0 15px;">'
                                        + str(element[5].value)
                                        + "</td></tr>"
                                    )

                        table += "</tbody></table>"
                        table += "</br></br><b>Prodlines</b></br>"
                        for prod in prodline.all():
                            table += prod.nome + "</br>"

                        table += (
                            "</b></b></br><b>Ficheiro diário de Schedule em: </b>"
                            + textPath
                        )

                        subject, from_email, to = (
                            "Wh Production " + nextDay.strftime("%d-%m-%Y"),
                            "noreply@visteon.com",
                            [
                                "npires2@visteon.com",
                                "abrandao@visteon.com",
                                "aroque1@visteon.com",
                                "sanasta1@visteon.com",
                                "rsalgue2@visteon.com",
                                "nlopes8@visteon.com",
                                "abilro1@visteon.com",
                                "jrodri80@visteon.com",
                                "evenanc1@visteon.com",
                            ],
                        )
                        msg = EmailMultiAlternatives(subject, table, from_email, to)
                        msg.attach_alternative(table, "text/html")
                        msg.send()
                    except KeyError:
                        mensagem = (
                            "</br>Worksheet name not found. Should be: Schedule Data or Sheet1 </br>"
                            + textPath
                            + ""
                        )
                        subject, from_email, to = (
                            "Wh Production " + nextDay.strftime("%d-%m-%Y"),
                            "noreply@visteon.com",
                            [
                                "npires2@visteon.com",
                                "abrandao@visteon.com",
                                "aroque1@visteon.com",
                                "sanasta1@visteon.com",
                                "rsalgue2@visteon.com",
                                "nlopes8@visteon.com",
                                "abilro1@visteon.com",
                                "jrodri80@visteon.com",
                                "evenanc1@visteon.com",
                            ],
                        )
                        msg = EmailMultiAlternatives(subject, mensagem, from_email, to)
                        msg.attach_alternative(mensagem, "text/html")
                        msg.send()
            except FileNotFoundError:
                mensagem = "</br> File not found. </br></br>" + textPath + ""
                subject, from_email, to = (
                    "Wh Production " + nextDay.strftime("%d-%m-%Y"),
                    "noreply@visteon.com",
                    [
                        "npires2@visteon.com",
                        "abrandao@visteon.com",
                        "aroque1@visteon.com",
                        "sanasta1@visteon.com",
                        "rsalgue2@visteon.com",
                        "nlopes8@visteon.com",
                        "abilro1@visteon.com",
                        "jrodri80@visteon.com",
                        "evenanc1@visteon.com",
                    ],
                )
                msg = EmailMultiAlternatives(subject, mensagem, from_email, to)
                msg.attach_alternative(mensagem, "text/html")
                msg.send()

        elif (
            (timeNow < timeEnd2 and timeNow > timeBefore2)
            and (not ProdlineTable.objects.filter(allOkReceiving=True).exists())
            and (actualDay.strftime("%A") != "Saturday")
            and (actualDay.strftime("%A") != "Sunday")
            and (elementosDiaSeguinte.count() > 0)
        ):

            valueSubmitReceiving = ""
            valueSubmitShipping = ""

            textPath = (
                "//PAVPD002/E_Proj/sharedir/MP&L/Schedule/"
                + actualDay.strftime("%Y")
                + "/"
                + mes
                + " "
                + actualDay.strftime("%Y")
                + "/Daily_Schedule_"
                + actualDay.strftime("%d.%m.%Y")
                + ".xlsx"
            )

            for elem in elementosDiaSeguinte.all():
                valueReceiving = ""
                valueShipping = ""

                if elem.comentarioShipping == None:
                    elem.comentarioShipping = " "
                if elem.comentarioReceiving == None:
                    elem.comentarioReceiving = " "
                if elem.shipping == True:
                    valueShipping = "X"
                if elem.receiving == True:
                    valueReceiving = "X"
                if elem.allOkShipping == True:
                    valueSubmitShipping = "X"
                if elem.allOkReceiving == True:
                    valueSubmitReceiving = "X"
                table += (
                    '<tr style="background-color: red"><td style="padding:0 15px 0 15px; background-color: red">'
                    + elem.line
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.site
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.due_date
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.item_number
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.description
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.to_complete
                    + '</td><td style="text-align: center; padding:0 15px 0 15px;">'
                    + valueReceiving
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + str(elem.comentarioReceiving)
                    + '</td><td style="text-align: center; padding:0 15px 0 15px;">'
                    + valueShipping
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + str(elem.comentarioShipping)
                    + "</td></tr>"
                )

            table += (
                '<tr><td colspan="6" style="text-align: right"><b>Submit</b></td><td style="text-align: center; padding:0 15px 0 15px;">'
                + valueSubmitReceiving
                + '</td><td style="text-align: right"><b>Submit</b></td><td style="text-align: center; padding:0 15px 0 15px;">'
                + valueSubmitShipping
                + "</td><td></td></tr>"
            )
            table += "</tbody></table>"
            table += "</br></br><b>Prodlines</b></br>"
            for prod in prodline.all():
                table += prod.nome + "</br>"

            table += "</b></b></br><b>Ficheiro diário de Schedule em: </b>" + textPath

            subject, from_email, to = (
                "Wh Production " + actualDay.strftime("%d-%m-%Y"),
                "noreply@visteon.com",
                [
                    "npires2@visteon.com",
                    "abrandao@visteon.com",
                    "aroque1@visteon.com",
                    "sanasta1@visteon.com",
                    "rsalgue2@visteon.com",
                    "nlopes8@visteon.com",
                    "abilro1@visteon.com",
                    "jrodri80@visteon.com",
                    "evenanc1@visteon.com",
                ],
            )
            msg = EmailMultiAlternatives(subject, table, from_email, to)
            msg.attach_alternative(table, "text/html")
            msg.send()

        elif (
            (timeNow < timeEnd3 and timeNow > timeBefore3)
            and (
                not ProdlineTable.objects.filter(allOkReceiving=True).exists()
                or not ProdlineTable.objects.filter(allOkShipping=True).exists()
            )
            and (actualDay.strftime("%A") != "Saturday")
            and (actualDay.strftime("%A") != "Sunday")
            and (elementosDiaSeguinte.count() > 0)
        ):

            valueSubmitReceiving = ""
            valueSubmitShipping = ""

            textPath = (
                "//PAVPD002/E_Proj/sharedir/MP&L/Schedule/"
                + actualDay.strftime("%Y")
                + "/"
                + mes
                + " "
                + actualDay.strftime("%Y")
                + "/Daily_Schedule_"
                + actualDay.strftime("%d.%m.%Y")
                + ".xlsx"
            )

            for elem in elementosDiaSeguinte.all():
                valueReceiving = ""
                valueShipping = ""

                if elem.comentarioShipping == None:
                    elem.comentarioShipping = " "
                if elem.comentarioReceiving == None:
                    elem.comentarioReceiving = " "
                if elem.shipping == True:
                    valueShipping = "X"
                if elem.receiving == True:
                    valueReceiving = "X"
                if elem.allOkShipping == True:
                    valueSubmitShipping = "X"
                if elem.allOkReceiving == True:
                    valueSubmitReceiving = "X"
                table += (
                    '<tr style="background-color: red"><td style="padding:0 15px 0 15px; background-color: red">'
                    + elem.line
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.site
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.due_date
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.item_number
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.description
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.to_complete
                    + '</td><td style="text-align: center; padding:0 15px 0 15px;">'
                    + valueReceiving
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + str(elem.comentarioReceiving)
                    + '</td><td style="text-align: center; padding:0 15px 0 15px;">'
                    + valueShipping
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + str(elem.comentarioShipping)
                    + "</td></tr>"
                )

            table += (
                '<tr><td colspan="6" style="text-align: right"><b>Submit</b></td><td style="text-align: center; padding:0 15px 0 15px;">'
                + valueSubmitReceiving
                + '</td><td style="text-align: right"><b>Submit</b></td><td style="text-align: center; padding:0 15px 0 15px;">'
                + valueSubmitShipping
                + "</td><td></td></tr>"
            )
            table += "</tbody></table>"

            table += '</b></br></br><table class="display"><thead style="background-color: lightgray"><tr><th>Line</th><th>Site</th><th>Due Date</th><th>Item Number</th><th>Qty to Complete</th><th>Actual Qty Completed</th></tr></thead><tbody>'

            for elem3 in elementosDiaSeguinte.all():
                elem2 = dadosQAD.filter(
                    wo_due_date=elem3.due_date, wo_part=elem3.item_number
                )
                for elem1 in elem2.all():
                    if (
                        str(elem1["wo_qty_exp_complete"])[:-11]
                        != str(elem1["wo_qty_comp"])[:-11]
                    ):
                        table += (
                            '<tr style="background-color: red">'
                            '<td style="padding:0 15px 0 15px;">'
                            + elem3.line
                            + '</td><td style="padding:0 15px 0 15px;">'
                            + elem3.site
                            + '</td><td style="padding:0 15px 0 15px;">'
                            + str(elem1["wo_due_date"])
                            + '</td><td style="padding:0 15px 0 15px;">'
                            + elem1["wo_part"]
                            + '</td><td style="padding:0 15px 0 15px;">'
                            + str(elem1["wo_qty_exp_complete"])[:-11]
                            + '</td><td style="padding:0 15px 0 15px;">'
                            + str(elem1["wo_qty_comp"])[:-11]
                            + "</td></tr>"
                        )
                    else:
                        table += (
                            '<tr style="background-color: whitesmoke">'
                            '<td style="padding:0 15px 0 15px;">'
                            + elem3.line
                            + '</td><td style="padding:0 15px 0 15px;">'
                            + elem3.site
                            + '</td><td style="padding:0 15px 0 15px;">'
                            + str(elem1["wo_due_date"])
                            + '</td><td style="padding:0 15px 0 15px;">'
                            + elem1["wo_part"]
                            + '</td><td style="padding:0 15px 0 15px;">'
                            + str(elem1["wo_qty_exp_complete"])[:-11]
                            + '</td><td style="padding:0 15px 0 15px;">'
                            + str(elem1["wo_qty_comp"])[:-11]
                            + "</td></tr>"
                        )

            table += "</tbody></table>"

            table += "</br></br><b>Prodlines</b></br>"
            for prod in prodline.all():
                table += prod.nome + "</br>"

            table += "</b></b></br><b>Ficheiro diário de Schedule em: </b>" + textPath

            subject, from_email, to = (
                "Wh Production " + actualDay.strftime("%d-%m-%Y"),
                "noreply@visteon.com",
                [
                    "npires2@visteon.com",
                    "abrandao@visteon.com",
                    "aroque1@visteon.com",
                    "sanasta1@visteon.com",
                    "rsalgue2@visteon.com",
                    "nlopes8@visteon.com",
                    "abilro1@visteon.com",
                    "jrodri80@visteon.com",
                    "evenanc1@visteon.com",
                ],
            )
            msg = EmailMultiAlternatives(subject, table, from_email, to)
            msg.attach_alternative(table, "text/html")
            msg.send()
