import datetime
from xlwt import Workbook

from django.core.management import BaseCommand

from crossdocking.models import *
from receiving.models import *


# Função Principal para envio dos emails
# Utilizar o task scheduler do windows, e nas acçoes colocar:
# Program/script: cmd
# Add arguments (optional): /c batch_updateDia1.bat
# Start in(optional): C:\visteon\shippers\management\commands
class Command(BaseCommand):
    def handle(self, *args, **options):
        prodline = ProdlineTableHistory.objects
        lineRequest = LineRequestFinished.objects

        firstDayPrevMonth = (
            datetime.datetime.today().replace(day=1) - datetime.timedelta(days=10)
        ).replace(day=1)
        prev2MonthName = (
            datetime.datetime.today().replace(day=1) - datetime.timedelta(days=32)
        ).strftime("%B")
        prev2MonthYear = (
            datetime.datetime.today().replace(day=1) - datetime.timedelta(days=32)
        ).strftime("%Y")

        wbProduction = Workbook()
        sheetProduction = wbProduction.add_sheet("Sheet 1")

        row = 0
        col = 0

        sheetProduction.write(row, col, "Line")
        sheetProduction.write(row, col + 1, "Site")
        sheetProduction.write(row, col + 2, "Due Date")
        sheetProduction.write(row, col + 3, "Item Number")
        sheetProduction.write(row, col + 4, "Description")
        sheetProduction.write(row, col + 5, "To Complete")
        sheetProduction.write(row, col + 6, "Receiving")
        sheetProduction.write(row, col + 7, "Submit Receiving")
        sheetProduction.write(row, col + 8, "Comentario Receiving")
        sheetProduction.write(row, col + 9, "Shipping")
        sheetProduction.write(row, col + 10, "Submit Shipping")
        sheetProduction.write(row, col + 11, "Comentario Shipping")

        row += 1

        for elem in prodline.all():
            datetime2 = datetime.datetime.strptime(elem.day, "%d-%m-%Y")
            if datetime2 < firstDayPrevMonth:
                eleme = ProdlineHistoryAllTime(
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
                eleme.save()

                sheetProduction.write(row, col, elem.line)
                sheetProduction.write(row, col + 1, elem.site)
                sheetProduction.write(row, col + 2, elem.due_date)
                sheetProduction.write(row, col + 3, elem.item_number)
                sheetProduction.write(row, col + 4, elem.description)
                sheetProduction.write(row, col + 5, elem.to_complete)
                sheetProduction.write(row, col + 6, elem.receiving)
                sheetProduction.write(row, col + 7, elem.allOkReceiving)
                sheetProduction.write(row, col + 8, elem.comentarioReceiving)
                sheetProduction.write(row, col + 9, elem.shipping)
                sheetProduction.write(row, col + 10, elem.allOkShipping)
                sheetProduction.write(row, col + 11, elem.comentarioShipping)
                row += 1

                # elem.delete()
        wbProduction.save(
            "W:\\sharedir\\MP&L\\Warehouse\\PWMS\\History\\Production\\workbook_"
            + prev2MonthName
            + prev2MonthYear
            + ".xls"
        )

        wbLineRequest = Workbook()
        sheetLineRequest = wbLineRequest.add_sheet("Sheet 1")

        row2 = 0
        col2 = 0

        sheetLineRequest.write(row2, col2, "Request Date")
        sheetLineRequest.write(row2, col2 + 1, "Part-Number")
        sheetLineRequest.write(row2, col2 + 2, "Line")
        sheetLineRequest.write(row2, col2 + 3, "Require")
        sheetLineRequest.write(row2, col2 + 4, "Receiver")
        sheetLineRequest.write(row2, col2 + 5, "Request Justification")
        sheetLineRequest.write(row2, col2 + 6, "Comment")

        row2 += 1

        for elem in lineRequest.all():
            datetime2 = datetime.datetime.strptime(elem.horaPedido, "%Y-%m-%d %H:%M:%S")
            if datetime2 < firstDayPrevMonth:
                novoRequest = LineRequestFinishedHistory(
                    None,
                    elem.horaPedido,
                    elem.partNumber,
                    elem.linha,
                    elem.requisitante,
                    elem.receiver,
                    elem.justificacao,
                    elem.comentario,
                )
                novoRequest.save()

                sheetLineRequest.write(row2, col2, elem.horaPedido)
                sheetLineRequest.write(row2, col2 + 1, elem.partNumber)
                sheetLineRequest.write(row2, col2 + 2, elem.linha)
                sheetLineRequest.write(row2, col2 + 3, elem.requisitante)
                sheetLineRequest.write(row2, col2 + 4, elem.receiver)
                sheetLineRequest.write(row2, col2 + 5, elem.justificacao)
                sheetLineRequest.write(row2, col2 + 6, elem.comentario)

                row2 += 1

                # elem.delete()
        wbLineRequest.save(
            "W:\\sharedir\\MP&L\\Warehouse\\PWMS\\History\\Line_Request\\workbook_"
            + prev2MonthName
            + prev2MonthYear
            + ".xls"
        )
