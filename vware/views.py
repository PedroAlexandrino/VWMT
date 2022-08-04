import os
import comtypes.client

from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
    user_passes_test,
)

from .forms import FileModelForm, FileModelFormReceiving, FileModelFormProcedimentos
from .models import (
    ArmazemChecklistQPS,
    LinksShippingOperations,
    ShippingOperation,
    ReceivingOperation,
    Procedimentos,
    Others,
    Crossdocking,
)
from django.core.exceptions import ObjectDoesNotExist
from .decorators import route, allowed_users

from qad_ee.models import *

import shutil

from vproject import settings
from vware.models import ArmazemChecklistQPS


@route("", name="armazem")
def armazem(request):
    User = get_user_model()
    users = User.objects.all()

    dadosBD = ArmazemChecklistQPS.objects
    return render(
        request, "vware/armazemTabela.html", {"dadosBD": dadosBD, "users": users}
    )
    # return render(request, 'vware/armazem.html')


@route("armazem/tabelaParent", name="armazem_tabelaParent")
def armazem_tabelaParent(request):
    data = dict()
    lista = []
    tabelaArmazem = ArmazemChecklistQPS.objects.all()
    # tabelaArmazem = ArmazemChecklistQPS.objects

    # return render(request, 'vware/armazemTabela.html', {'tabelaArmazem', tabelaArmazem})
    # colocar todas as linhas da schedule
    # onclick="printJS({printable:'{{ object.adminUpload.url }}', type:'pdf'})"
    for x in tabelaArmazem:
        # vai buscar localizacao checklist para imprimir
        checklist = "printJS({printable:'" + x.checklist.url + "', type:'pdf'})"
        # vai buscar localizacao powerpoint QPS
        # check_qps = "modalQPS/" + str(x.pk) + "/"
        # butoes de imprimir checklist e visualizar powerpoint
        # accoes_user = '<button type="button" class="btn btn-outline-primary" onclick="'+checklist+'"><i type="button" class="fas fa-print"></i>CheckList</button><span> </span><button class="show-form-modal btn btn-outline-danger" data-url="' + check_qps + '"><i class="fas fa-file-powerpoint"></i>QPS</button></div>',

        row = {
            "oem": x.oem,
            "qpsShipping": '<a class="text-dark" href="'
            + x.qpsShipping.url
            + '" target="_blank" class="link-primary">QPS_Shipping</a>',
            "qpsManufatura": '<a class="text-dark" href="'
            + x.qpsManufatura.url
            + '" target="_blank" class="link-primary">QPS_Manufatura</a>',
            "checklist": '<button type="button" class="btn btn-outline-dark" onclick="'
            + checklist
            + '"><i type="button" class="fas fa-print"></i>CheckList</button>',
            "inspecaoDedicada": '<a class="text-dark" href="'
            + x.inspecaoDedicada.url
            + '" target="_blank" class="link-primary">Inspeção_Dedicada</a>',
            "crossDocking": '<a class="text-dark" href="'
            + x.crossDocking.url
            + '" target="_blank" class="link-primary">Cross_Docking</a>',
            "engenharia": '<a class="text-dark" href="'
            + x.engenharia.url
            + '" target="_blank" class="link-primary">Engenharia</a>',
            "servicos": '<a class="text-dark" href="'
            + x.servicos.url
            + '" target="_blank" class="link-primary">Serviços</a>',
            "guideLines": '<a class="text-dark" href="'
            + x.guideLines.url
            + '" target="_blank" class="link-primary">Guide_Lines</a>',
            # "produto": x.produto,
            # "descricao": x.descricao,
            # "accoes": accoes_user,
        }
        lista.append(row)

    return JsonResponse({"data": lista}, safe=False)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, "rb") as fh:
            response = HttpResponse(fh.read(), content_type="application/adminUpload")
            response["Content-Disposition"] = "filename=" + os.path.basename(file_path)
            return response

    raise Http404


@route("create/", name="create")
@login_required()
@user_passes_test(lambda u: u.groups.filter(name="oemDatabase").exists())
def create(request):
    if request.method == "POST":

        oem = request.POST["oem"]
        if oem == "Selecione uma opção":
            return render(
                request, "vware/criarProduto.html", {"erro": "Insert valid OEM"}
            )

        if len(request.FILES) == 0:
            return render(
                request, "vware/criarProduto.html", {"erro2": "No file chosen"}
            )

        try:
            tabelaArmazem = ArmazemChecklistQPS.objects.get(oem=oem)
        except ObjectDoesNotExist:
            product = ArmazemChecklistQPS()
            product.oem = oem
            if request.FILES.get("qpsShipping"):
                product.qpsShipping = request.FILES["qpsShipping"]
            if request.FILES.get("qpsPacking"):
                product.qpsPacking = request.FILES["qpsPacking"]
            if request.FILES.get("checklist"):
                product.checklist = request.FILES["checklist"]
            if request.FILES.get("inspecaoDedicada"):
                product.inspecaoDedicada = request.FILES["inspecaoDedicada"]
            if request.FILES.get("crossDocking"):
                product.crossDocking = request.FILES["crossDocking"]
            if request.FILES.get("engenharia"):
                product.engenharia = request.FILES["engenharia"]
            if request.FILES.get("servicos"):
                product.servicos = request.FILES["servicos"]
            if request.FILES.get("guideLines"):
                product.guideLines = request.FILES["guideLines"]
            product.save()
            dadosBD = ArmazemChecklistQPS.objects
            return render(request, "vware/armazemTabela.html", {"dadosBD": dadosBD})

        if len(request.FILES) != 0:
            if request.FILES.get("qpsShipping"):
                tabelaArmazem.qpsShipping = request.FILES["qpsShipping"]
                # ArmazemChecklistQPS.objects.filter(oem=oem).update(qpsShipping = request.FILES['qpsShipping'])
                # tabelaArmazem.qpsShipping.update(file = request.FILES['qpsShipping'])
                # ArmazemChecklistQPS.objects.filter(oem=oem).update(qpsShipping=request.FILES['qpsShipping'])
            if request.FILES.get("qpsPacking"):
                tabelaArmazem.qpsPacking = request.FILES["qpsPacking"]
            if request.FILES.get("checklist"):
                tabelaArmazem.checklist = request.FILES["checklist"]
            if request.FILES.get("inspecaoDedicada"):
                tabelaArmazem.inspecaoDedicada = request.FILES["inspecaoDedicada"]
            if request.FILES.get("crossDocking"):
                tabelaArmazem.crossDocking = request.FILES["crossDocking"]
            if request.FILES.get("engenharia"):
                tabelaArmazem.engenharia = request.FILES["engenharia"]
            if request.FILES.get("servicos"):
                tabelaArmazem.servicos = request.FILES["servicos"]
            if request.FILES.get("guideLines"):
                tabelaArmazem.guideLines = request.FILES["guideLines"]
            tabelaArmazem.save()
        dadosBD = ArmazemChecklistQPS.objects
        return render(request, "vware/armazemTabela.html", {"dadosBD": dadosBD})
    else:
        return render(request, "vware/criarProduto.html")


@route("tabela/", name="tabela")
def tabela(request):
    dadosBD = ArmazemChecklistQPS.objects
    return render(request, "vware/armazemTabela.html", {"dadosBD": dadosBD})


@route("operations/", name="operations")
def operations(request):
    shippingOperation = ShippingOperation.objects
    receivingOperation = ReceivingOperation.objects
    crossdocking = Crossdocking.objects
    procedimentos = Procedimentos.objects
    others = Others.objects
    return render(
        request,
        "vware/operations.html",
        {
            "shippingOperation": shippingOperation,
            "receivingOperation": receivingOperation,
            "procedimentos": procedimentos,
            "others": others,
            "crossdocking": crossdocking,
        },
    )


@route("shippingOperation/", name="shippingOperation")
@login_required()
@user_passes_test(lambda u: u.groups.filter(name="oemDatabase").exists())
def shippingOperation(request):
    shippingOperation = ShippingOperation.objects
    return render(
        request,
        "vware/shippingOperation.html",
        {"shippingOperation": shippingOperation},
    )


@route("receivingOperation/", name="receivingOperation")
@login_required()
@user_passes_test(lambda u: u.groups.filter(name="oemDatabase").exists())
def receivingOperation(request):
    receivingOperation = ReceivingOperation.objects
    return render(
        request,
        "vware/receivingOperation.html",
        {"receivingOperation": receivingOperation},
    )


@route("nonProductionOperation/", name="nonProductionOperation")
def nonProductionOperation(request):
    procedimentos = Procedimentos.objects
    others = Others.objects
    return render(
        request,
        "vware/nonProductionOperation.html",
        {"procedimentos": procedimentos, "others": others},
    )


@route("qpsPackingPage/", name="qpsPackingPage")
def qpsPackingPage(request):
    return render(request, "vware/qpsPacking.html")


@route("qpsPacking/", name="qpsPacking")
def qpsPacking(request):
    if request.method == "GET":
        oemCliente = request.GET["oemCliente"]

        caminho = (
            "//PAVPD002/E_Proj/sharedir/MP&L/PROCEDIMENTOS/Packaging/QPS EMBALAGEM/"
            + oemCliente
        )

        files = os.listdir(caminho)

        return JsonResponse({"files": files})


@route("qpsShipping/", name="qpsShipping")
def qpsShipping(request):
    if request.method == "GET":
        caminho = "//PAVPD002/E_Proj/sharedir/MP&L/PROCEDIMENTOS/Shipping/QPS Shipping"

        files = os.listdir(caminho)

        return JsonResponse({"files": files})


@route("configurationShippingOperation/", name="configurationShippingOperation")
@login_required()
@user_passes_test(lambda u: u.groups.filter(name="admin").exists())
def configurationShippingOperation(request):
    if request.method == "POST":
        file_form = FileModelForm(request.POST, request.FILES)
        one = request.FILES.getlist("one")  # field name in model
        two = request.FILES.getlist("two")
        three = request.FILES.getlist("three")
        four = request.FILES.getlist("four")
        five = request.FILES.getlist("five")
        six = request.FILES.getlist("six")
        seven = request.FILES.getlist("seven")
        eight = request.FILES.getlist("eight")
        checklist = request.FILES.getlist("checklist")
        other = request.FILES.getlist("other")
        requestShipper = request.FILES.getlist("requestShipper")

        if file_form.is_valid():
            if request.FILES.getlist("one"):
                ShippingOperation.objects.exclude(one="").delete()
                caminho = "C:/visteon/media/shipping/one"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if request.FILES.getlist("two"):
                ShippingOperation.objects.exclude(two="").delete()
                caminho = "C:/visteon/media/shipping/two"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if request.FILES.getlist("three"):
                ShippingOperation.objects.exclude(three="").delete()
                caminho = "C:/visteon/media/shipping/three"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if request.FILES.getlist("four"):
                ShippingOperation.objects.exclude(four="").delete()
                caminho = "C:/visteon/media/shipping/four"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if request.FILES.getlist("five"):
                ShippingOperation.objects.exclude(five="").delete()
                caminho = "C:/visteon/media/shipping/five"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if request.FILES.getlist("six"):
                ShippingOperation.objects.exclude(six="").delete()
                caminho = "C:/visteon/media/shipping/six"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if request.FILES.getlist("seven"):
                ShippingOperation.objects.exclude(seven="").delete()
                caminho = "C:/visteon/media/shipping/seven"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if request.FILES.getlist("eight"):
                ShippingOperation.objects.exclude(eight="").delete()
                caminho = "C:/visteon/media/shipping/eight"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if request.FILES.getlist("checklist"):
                ShippingOperation.objects.exclude(checklist="").delete()
                caminho = "C:/visteon/media/shipping/checklist"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if request.FILES.getlist("other"):
                ShippingOperation.objects.exclude(others="").delete()
                caminho = "C:/visteon/media/shipping/others"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if request.FILES.getlist("requestShipper"):
                ShippingOperation.objects.exclude(requestShippers="").delete()
                caminho = "C:/visteon/media/shipping/requestShipper"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            for f in one:
                ship = ShippingOperation()
                ship.one = f
                ship.save()
            for f in two:
                ship = ShippingOperation()
                ship.two = f
                ship.save()
            for f in three:
                ship = ShippingOperation()
                ship.three = f
                ship.save()
            for f in four:
                ship = ShippingOperation()
                ship.four = f
                ship.save()
            for f in five:
                ship = ShippingOperation()
                ship.five = f
                ship.save()
            for f in six:
                ship = ShippingOperation()
                ship.six = f
                ship.save()
            for f in seven:
                ship = ShippingOperation()
                ship.seven = f
                ship.save()
            for f in eight:
                ship = ShippingOperation()
                ship.eight = f
                ship.save()
            for f in checklist:
                ship = ShippingOperation()
                ship.checklist = f
                ship.save()
            for f in other:
                ship = ShippingOperation()
                ship.others = f
                ship.save()
            for f in requestShipper:
                ship = ShippingOperation()
                ship.requestShippers = f
                ship.save()
            return redirect("vware:operations")

    # the rest is the basic code: template_name, context, render etc.


# in your template.html <form> tag must include enctype="multipart/form-data"


@route("configurationReceivingOperation/", name="configurationReceivingOperation")
def configurationReceivingOperation(request):
    if request.method == "POST":
        file_form = FileModelFormReceiving(request.POST, request.FILES)
        one = request.FILES.getlist("one")  # field name in model
        two = request.FILES.getlist("two")
        three = request.FILES.getlist("three")
        four = request.FILES.getlist("four")
        five = request.FILES.getlist("five")
        six = request.FILES.getlist("six")
        seven = request.FILES.getlist("seven")
        eight = request.FILES.getlist("eight")
        nine = request.FILES.getlist("nine")

        if file_form.is_valid():
            if request.FILES.getlist("one"):
                ReceivingOperation.objects.exclude(one="").delete()
                caminho = "C:/visteon/media/receiving/one"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if request.FILES.getlist("two"):
                ReceivingOperation.objects.exclude(two="").delete()
                caminho = "C:/visteon/media/receiving/two"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if request.FILES.getlist("three"):
                ReceivingOperation.objects.exclude(three="").delete()
                caminho = "C:/visteon/media/receiving/three"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if request.FILES.getlist("four"):
                ReceivingOperation.objects.exclude(four="").delete()
                caminho = "C:/visteon/media/receiving/four"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if request.FILES.getlist("five"):
                ReceivingOperation.objects.exclude(five="").delete()
                caminho = "C:/visteon/media/receiving/five"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if request.FILES.getlist("six"):
                ReceivingOperation.objects.exclude(six="").delete()
                caminho = "C:/visteon/media/receiving/six"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if request.FILES.getlist("seven"):
                ReceivingOperation.objects.exclude(seven="").delete()
                caminho = "C:/visteon/media/receiving/seven"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if request.FILES.getlist("eight"):
                ReceivingOperation.objects.exclude(eight="").delete()
                caminho = "C:/visteon/media/receiving/eight"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if request.FILES.getlist("nine"):
                ReceivingOperation.objects.exclude(nine="").delete()
                caminho = "C:/visteon/media/receiving/nine"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            for f in one:
                receiver = ReceivingOperation()
                receiver.one = f
                receiver.save()
            for f in two:
                receiver = ReceivingOperation()
                receiver.two = f
                receiver.save()
            for f in three:
                receiver = ReceivingOperation()
                receiver.three = f
                receiver.save()
            for f in four:
                receiver = ReceivingOperation()
                receiver.four = f
                receiver.save()
            for f in five:
                receiver = ReceivingOperation()
                receiver.five = f
                receiver.save()
            for f in six:
                receiver = ReceivingOperation()
                receiver.six = f
                receiver.save()
            for f in seven:
                receiver = ReceivingOperation()
                receiver.seven = f
                receiver.save()
            for f in eight:
                receiver = ReceivingOperation()
                receiver.eight = f
                receiver.save()
            for f in nine:
                receiver = ReceivingOperation()
                receiver.nine = f
                receiver.save()
            return redirect("vware:operations")


@route("configurationCrossdockingOperation/", name="configurationCrossdockingOperation")
@login_required()
@user_passes_test(lambda u: u.groups.filter(name="admin").exists())
def configurationCrossdockingOperation(request):
    if request.method == "POST":
        ford = request.FILES.get("fordCrossdockingFile")  # field name in model
        psa = request.FILES.get("psaCrossdockingFile")
        scania = request.FILES.get("scaniaCrossdockingFile")
        volvo = request.FILES.get("volvoCrossdockingFile")

        if ford:
            Crossdocking.objects.exclude(ford="").delete()
            caminho = "C:/visteon/media/crossdocking/ford"
            if os.path.exists(caminho):
                for entry in os.listdir(caminho):
                    if os.path.isfile(os.path.join(caminho, entry)):
                        os.remove(caminho + "/" + entry)
            novoDoc = Crossdocking()
            novoDoc.ford = ford
            novoDoc.save()
        if psa:
            Crossdocking.objects.exclude(psa="").delete()
            caminho = "C:/visteon/media/crossdocking/psa"
            if os.path.exists(caminho):
                for entry in os.listdir(caminho):
                    if os.path.isfile(os.path.join(caminho, entry)):
                        os.remove(caminho + "/" + entry)
            novoDoc = Crossdocking()
            novoDoc.psa = psa
            novoDoc.save()
        if scania:
            Crossdocking.objects.exclude(scania="").delete()
            caminho = "C:/visteon/media/crossdocking/scania"
            if os.path.exists(caminho):
                for entry in os.listdir(caminho):
                    if os.path.isfile(os.path.join(caminho, entry)):
                        os.remove(caminho + "/" + entry)
            novoDoc = Crossdocking()
            novoDoc.scania = scania
            novoDoc.save()
        if volvo:
            Crossdocking.objects.exclude(volvo="").delete()
            caminho = "C:/visteon/media/crossdocking/volvo"
            if os.path.exists(caminho):
                for entry in os.listdir(caminho):
                    if os.path.isfile(os.path.join(caminho, entry)):
                        os.remove(caminho + "/" + entry)
            novoDoc = Crossdocking()
            novoDoc.volvo = volvo
            novoDoc.save()
        return redirect("vware:operations")


# the rest is the basic code: template_name, context, render etc.

# in your template.html <form> tag must include enctype="multipart/form-data"


@route("configurationDocumentacao/", name="configurationDocumentacao")
@login_required()
@user_passes_test(lambda u: u.groups.filter(name="admin").exists())
def configurationDocumentacao(request):
    if request.method == "POST":
        one = request.FILES.get("oneDoc")  # field name in model
        two = request.FILES.get("twoDoc")
        three = request.FILES.get("threeDoc")
        four = request.FILES.get("fourDoc")
        five = request.FILES.get("fiveDoc")
        six = request.FILES.get("sixDoc")
        seven = request.FILES.get("sevenDoc")
        eight = request.FILES.get("eightDoc")
        nine = request.FILES.get("nineDoc")

        if one:
            Procedimentos.objects.exclude(docOne="").delete()
            caminho = "C:/visteon/media/procedimentos/documentacao/one"
            if os.path.exists(caminho):
                for entry in os.listdir(caminho):
                    if os.path.isfile(os.path.join(caminho, entry)):
                        os.remove(caminho + "/" + entry)
            novoDoc = Procedimentos()
            novoDoc.docOne = one
            novoDoc.save()
        if two:
            Procedimentos.objects.exclude(docTwo="").delete()
            caminho = "C:/visteon/media/procedimentos/documentacao/two"
            if os.path.exists(caminho):
                for entry in os.listdir(caminho):
                    if os.path.isfile(os.path.join(caminho, entry)):
                        os.remove(caminho + "/" + entry)
            novoDoc = Procedimentos()
            novoDoc.docTwo = two
            novoDoc.save()
        if three:
            Procedimentos.objects.exclude(docThree="").delete()
            caminho = "C:/visteon/media/procedimentos/documentacao/three"
            if os.path.exists(caminho):
                for entry in os.listdir(caminho):
                    if os.path.isfile(os.path.join(caminho, entry)):
                        os.remove(caminho + "/" + entry)
            novoDoc = Procedimentos()
            novoDoc.docThree = three
            novoDoc.save()
        if four:
            Procedimentos.objects.exclude(docFour="").delete()
            caminho = "C:/visteon/media/procedimentos/documentacao/four"
            if os.path.exists(caminho):
                for entry in os.listdir(caminho):
                    if os.path.isfile(os.path.join(caminho, entry)):
                        os.remove(caminho + "/" + entry)
            novoDoc = Procedimentos()
            novoDoc.docFour = four
            novoDoc.save()
        if five:
            Procedimentos.objects.exclude(docFive="").delete()
            caminho = "C:/visteon/media/procedimentos/documentacao/five"
            if os.path.exists(caminho):
                for entry in os.listdir(caminho):
                    if os.path.isfile(os.path.join(caminho, entry)):
                        os.remove(caminho + "/" + entry)
            novoDoc = Procedimentos()
            novoDoc.docFive = five
            novoDoc.save()
        if six:
            Procedimentos.objects.exclude(docSix="").delete()
            caminho = "C:/visteon/media/procedimentos/documentacao/six"
            if os.path.exists(caminho):
                for entry in os.listdir(caminho):
                    if os.path.isfile(os.path.join(caminho, entry)):
                        os.remove(caminho + "/" + entry)
            novoDoc = Procedimentos()
            novoDoc.docSix = six
            novoDoc.save()
        if seven:
            Procedimentos.objects.exclude(docSeven="").delete()
            caminho = "C:/visteon/media/procedimentos/documentacao/seven"
            if os.path.exists(caminho):
                for entry in os.listdir(caminho):
                    if os.path.isfile(os.path.join(caminho, entry)):
                        os.remove(caminho + "/" + entry)
            novoDoc = Procedimentos()
            novoDoc.docSeven = seven
            novoDoc.save()
        if eight:
            Procedimentos.objects.exclude(docEight="").delete()
            caminho = "C:/visteon/media/procedimentos/documentacao/eight"
            if os.path.exists(caminho):
                for entry in os.listdir(caminho):
                    if os.path.isfile(os.path.join(caminho, entry)):
                        os.remove(caminho + "/" + entry)
            novoDoc = Procedimentos()
            novoDoc.docEight = eight
            novoDoc.save()
        if nine:
            Procedimentos.objects.exclude(docNine="").delete()
            caminho = "C:/visteon/media/procedimentos/documentacao/nine"
            if os.path.exists(caminho):
                for entry in os.listdir(caminho):
                    if os.path.isfile(os.path.join(caminho, entry)):
                        os.remove(caminho + "/" + entry)
            novoDoc = Procedimentos()
            novoDoc.docNine = nine
            novoDoc.save()
        return redirect("vware:nonProductionOperation")


# the rest is the basic code: template_name, context, render etc.

# in your template.html <form> tag must include enctype="multipart/form-data"


@route("configurationAnexos/", name="configurationAnexos")
@login_required()
@user_passes_test(lambda u: u.groups.filter(name="admin").exists())
def configurationAnexos(request):
    if request.method == "POST":
        file_form = FileModelFormProcedimentos(request.POST, request.FILES)
        one = request.FILES.getlist("oneAnexo")  # field name in model
        two = request.FILES.getlist("twoAnexo")
        three = request.FILES.getlist("threeAnexo")
        four = request.FILES.getlist("fourAnexo")
        five = request.FILES.getlist("fiveAnexo")
        six = request.FILES.getlist("sixAnexo")
        seven = request.FILES.getlist("sevenAnexo")
        eight = request.FILES.getlist("eightAnexo")
        nine = request.FILES.getlist("nineAnexo")

        if file_form.is_valid():
            if one:
                Procedimentos.objects.exclude(anexoOne="").delete()
                caminho = "C:/visteon/media/procedimentos/anexos/one"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if two:
                Procedimentos.objects.exclude(anexoTwo="").delete()
                caminho = "C:/visteon/media/procedimentos/anexos/two"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if three:
                Procedimentos.objects.exclude(anexoThree="").delete()
                caminho = "C:/visteon/media/procedimentos/anexos/three"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if four:
                Procedimentos.objects.exclude(anexoFour="").delete()
                caminho = "C:/visteon/media/procedimentos/anexos/four"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if five:
                Procedimentos.objects.exclude(anexoFive="").delete()
                caminho = "C:/visteon/media/procedimentos/anexos/five"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if six:
                Procedimentos.objects.exclude(anexoSix="").delete()
                caminho = "C:/visteon/media/procedimentos/anexos/six"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if seven:
                Procedimentos.objects.exclude(anexoSeven="").delete()
                caminho = "C:/visteon/media/procedimentos/anexos/seven"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if eight:
                Procedimentos.objects.exclude(anexoEight="").delete()
                caminho = "C:/visteon/media/procedimentos/anexos/eight"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if nine:
                Procedimentos.objects.exclude(anexoNine="").delete()
                caminho = "C:/visteon/media/procedimentos/anexos/eight"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            for f in one:
                anexo = Procedimentos()
                anexo.anexoOne = f
                anexo.save()
            for f in two:
                anexo = Procedimentos()
                anexo.anexoTwo = f
                anexo.save()
            for f in three:
                anexo = Procedimentos()
                anexo.anexoThree = f
                anexo.save()
            for f in four:
                anexo = Procedimentos()
                anexo.anexoFour = f
                anexo.save()
            for f in five:
                anexo = Procedimentos()
                anexo.anexoFive = f
                anexo.save()
            for f in six:
                anexo = Procedimentos()
                anexo.anexoSix = f
                anexo.save()
            for f in seven:
                anexo = Procedimentos()
                anexo.anexoSeven = f
                anexo.save()
            for f in eight:
                anexo = Procedimentos()
                anexo.anexoEight = f
                anexo.save()
            for f in nine:
                anexo = Procedimentos()
                anexo.anexoNine = f
                anexo.save()
            return redirect("vware:nonProductionOperation")


@route("configurationQps/", name="configurationQps")
@login_required()
@user_passes_test(lambda u: u.groups.filter(name="admin").exists())
def configurationQps(request):
    if request.method == "POST":
        file_form = FileModelFormProcedimentos(request.POST, request.FILES)
        one = request.FILES.getlist("oneQps")  # field name in model
        two = request.FILES.getlist("twoQps")
        three = request.FILES.getlist("threeQps")
        four = request.FILES.getlist("fourQps")
        five = request.FILES.getlist("fiveQps")
        six = request.FILES.getlist("sixQps")
        seven = request.FILES.getlist("sevenQps")
        eight = request.FILES.getlist("eightQps")
        nine = request.FILES.getlist("nineQps")

        if file_form.is_valid():
            if one:
                Procedimentos.objects.exclude(qpsOne="").delete()
                caminho = "C:/visteon/media/procedimentos/qps/one"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if two:
                Procedimentos.objects.exclude(qpsTwo="").delete()
                caminho = "C:/visteon/media/procedimentos/qps/two"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if three:
                Procedimentos.objects.exclude(qpsThree="").delete()
                caminho = "C:/visteon/media/procedimentos/qps/three"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if four:
                Procedimentos.objects.exclude(qpsFour="").delete()
                caminho = "C:/visteon/media/procedimentos/qps/four"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if five:
                Procedimentos.objects.exclude(qpsFive="").delete()
                caminho = "C:/visteon/media/procedimentos/qps/five"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if six:
                Procedimentos.objects.exclude(qpsSix="").delete()
                caminho = "C:/visteon/media/procedimentos/qps/six"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if seven:
                Procedimentos.objects.exclude(anexoSeven="").delete()
                caminho = "C:/visteon/media/procedimentos/qps/seven"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if eight:
                Procedimentos.objects.exclude(qpsEight="").delete()
                caminho = "C:/visteon/media/procedimentos/qps/eight"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            if nine:
                Procedimentos.objects.exclude(qpsNine="").delete()
                caminho = "C:/visteon/media/procedimentos/qps/eight"
                if os.path.exists(caminho):
                    for entry in os.listdir(caminho):
                        if os.path.isfile(os.path.join(caminho, entry)):
                            os.remove(caminho + "/" + entry)
            for f in one:
                qps = Procedimentos()
                qps.qpsOne = f
                qps.save()
            for f in two:
                qps = Procedimentos()
                qps.qpsTwo = f
                qps.save()
            for f in three:
                qps = Procedimentos()
                qps.qpsThree = f
                qps.save()
            for f in four:
                qps = Procedimentos()
                qps.qpsFour = f
                qps.save()
            for f in five:
                qps = Procedimentos()
                qps.qpsFive = f
                qps.save()
            for f in six:
                qps = Procedimentos()
                qps.qpsSix = f
                qps.save()
            for f in seven:
                qps = Procedimentos()
                qps.qpsSeven = f
                qps.save()
            for f in eight:
                qps = Procedimentos()
                qps.qpsEight = f
                qps.save()
            for f in nine:
                qps = Procedimentos()
                qps.qpsNine = f
                qps.save()
            return redirect("vware:nonProductionOperation")


@route("configurationOthers/", name="configurationOthers")
@login_required()
@user_passes_test(lambda u: u.groups.filter(name="admin").exists())
def configurationOthers(request):
    if request.method == "POST":
        one = request.FILES.get("oneOthers")  # field name in model
        two = request.FILES.get("twoOthers")
        three = request.FILES.get("threeOthers")
        four = request.FILES.get("fourOthers")
        five = request.FILES.get("fiveOthers")

        if one:
            Others.objects.exclude(one="").delete()
            caminho = "C:/visteon/media/others/one"
            if os.path.exists(caminho):
                for entry in os.listdir(caminho):
                    if os.path.isfile(os.path.join(caminho, entry)):
                        os.remove(caminho + "/" + entry)
            novoOther = Others()
            novoOther.one = one
            novoOther.save()
        if two:
            Others.objects.exclude(two="").delete()
            caminho = "C:/visteon/media/others/two"
            if os.path.exists(caminho):
                for entry in os.listdir(caminho):
                    if os.path.isfile(os.path.join(caminho, entry)):
                        os.remove(caminho + "/" + entry)
            novoOther = Others()
            novoOther.two = two
            novoOther.save()
        if three:
            Others.objects.exclude(three="").delete()
            caminho = "C:/visteon/media/others/three"
            if os.path.exists(caminho):
                for entry in os.listdir(caminho):
                    if os.path.isfile(os.path.join(caminho, entry)):
                        os.remove(caminho + "/" + entry)
            novoOther = Others()
            novoOther.three = three
            novoOther.save()
        if four:
            Others.objects.exclude(four="").delete()
            caminho = "C:/visteon/media/others/four"
            if os.path.exists(caminho):
                for entry in os.listdir(caminho):
                    if os.path.isfile(os.path.join(caminho, entry)):
                        os.remove(caminho + "/" + entry)
            novoOther = Others()
            novoOther.four = four
            novoOther.save()
        if five:
            Others.objects.exclude(five="").delete()
            caminho = "C:/visteon/media/others/five"
            if os.path.exists(caminho):
                for entry in os.listdir(caminho):
                    if os.path.isfile(os.path.join(caminho, entry)):
                        os.remove(caminho + "/" + entry)
            novoOther = Others()
            novoOther.five = five
            novoOther.save()
        return redirect("vware:nonProductionOperation")


def PPTtoPDF(inputFileName, outputFileName, formatType=32):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1
    inputFile = input(inputFileName)

    if outputFileName[-3:] != "pdf":
        outputFileName = outputFileName + ".pdf"
    pdf = powerpoint.Presentations.Open(inputFile, WithWindow=False)
    pdf.SaveAs(outputFileName, 32)  # formatType = 32 for ppt to pdf
    pdf.Close()
    powerpoint.Quit()


@route("reportOperations", name="reportOperations")
def reportOperations(request):
    if request.method == "POST":
        texto = request.POST["reportICDR"].replace("\n", "</br>")

        message = "<b>Report criado pelo User: " + request.user.username + "</b>"
        message += "</br></br>" + texto
        subject, from_email, to = (
            "Novo report na página Database - Operations",
            "noreply@visteon.com",
            ["aroque1@visteon.com", "npires2@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()
        return redirect("vware:operations")


@route("reportNonProduction", name="reportNonProduction")
def reportNonProduction(request):
    if request.method == "POST":
        texto = request.POST["reportICDR"].replace("\n", "</br>")

        message = "<b>Report criado pelo User: " + request.user.username + "</b>"
        message += "</br></br>" + texto
        subject, from_email, to = (
            "Novo report na página Database - Non Production Operations",
            "noreply@visteon.com",
            ["aroque1@visteon.com", "npires2@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()
        return redirect("vware:nonProductionOperation")
