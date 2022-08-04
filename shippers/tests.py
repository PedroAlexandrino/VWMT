from django.core.mail import EmailMultiAlternatives
from django.test import TestCase
from django.core import mail


# Create your tests here.


def testEmail(self, elemento=None):
    print("Inicio do Test")
    table = '</br><table class="display"><thead style="background-color: lightgray"><tr><th>DATA/HORA CHEGADA</th><th>CONDUTOR</th><th>ID</th><th>CONTACTO</th><th>EMPRESA</th><th>1ª MATRICULA</th><th>2ª MATRICULA</th><th>CARGA/DESCARGA</th><th>DOCA</th><th>DESTINO CARGA</th><th>TIPO VIATURA</th><th>DATA/HORA ENTRADA</th><th>ABANDONO</th><th>COMENTARIOS ENTRADA</th><th>DATA/HORA SAIDA</th><th>COMENTARIOS SAIDA</th></tr></thead><tbody>'

    table += (
        '<tr style="background-color: red">'
        + '<td style="padding:0 15px 0 15px;">'
        + elemento.dataHoraChegada
        + "</td>"
        + '<td style="padding:0 15px 0 15px;">'
        + elemento.condutor
        + "</td>"
        + '<td style="padding:0 15px 0 15px;">'
        + elemento.ident
        + "</td>"
        + '<td style="padding:0 15px 0 15px;">'
        + elemento.contacto
        + "</td>"
        + '<td style="padding:0 15px 0 15px;">'
        + elemento.empresa
        + "</td>"
        + '<td style="padding:0 15px 0 15px;">'
        + elemento.primeiraMatricula
        + "</td>"
        + '<td style="padding:0 15px 0 15px;">'
        + elemento.segundaMatricula
        + "</td>"
        + '<td style="padding:0 15px 0 15px;">'
        + elemento.cargaDescarga
        + "</td>"
        + '<td style="padding:0 15px 0 15px;">'
        + elemento.doca
        + "</td>"
        + '<td style="padding:0 15px 0 15px;">'
        + elemento.destinoCarga
        + "</td>"
        + '<td style="padding:0 15px 0 15px;">'
        + elemento.tipoViatura
        + "</td>"
        + '<td style="padding:0 15px 0 15px; text-align: center">'
        + elemento.dataHoraEntrada
        + "</td>"
        + '<td style="padding:0 15px 0 15px; text-align: center">'
        + "X"
        + "</td>"
        + '<td style="padding:0 15px 0 15px; text-align: center">'
        + elemento.comentEntrada
        + "</td>"
        + '<td style="padding:0 15px 0 15px;">'
        + elemento.dataHoraSaida
        + "</td>"
        + '<td style="padding:0 15px 0 15px;">'
        + elemento.comentEntrada
        + "</td></tr>"
    )
    table += '<tr style="background-color: lightgray"><td colspan="18"> </td></tr>'
    table += "</tbody></table>"

    subject, from_email, to = (
        "Alteração em Shipping - Portaria",
        "noreply@visteon.com",
        ["pmarti30@visteon.com"],
    )
    msg = EmailMultiAlternatives(subject, table, from_email, to)
    msg.attach_alternative(table, "text/html")
    print("Fim do teste")
    msg.send()
