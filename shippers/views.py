from email import contentmanager
import json
import os
from datetime import datetime

import time
import tablib
import math
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core import serializers
from django.core.mail import EmailMultiAlternatives
from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render, redirect
import openpyxl
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
from xlwt import Workbook

from shippers.models import *
from qad_ee.models import *
from contextlib import contextmanager


@contextmanager
def timer():
    try:
        # __enter__
        t = time.perf_counter()
        yield
    finally:
        # __exit__
        print(f"A função  demorou {time.perf_counter() -t}ms")


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="admin").exists())
def configurations(request):
    users = User.objects
    return render(request, "shippers/configurations.html", {"users": users})


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="shippingTracking").exists())
def shippersTracking(request):
    with timer():
        # max 0.8 ms
        tabela = PreShipperBrowse.objects
        tabelaFilha = PreShipperDetailBrowse.objects
        return render(
            request,
            "shippers/shippers.html",
            {"tabela": tabela, "tabelaFilha": tabelaFilha},
        )


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="shippingConfirmation").exists())
def shippersConfirmation(request):
    ficheiro_Shippers = finalFicheiroShippers.objects
    return render(
        request,
        "shippers/shippersConfirmation.html",
        {"ficheiro_Shippers": ficheiro_Shippers},
    )


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="shippingSecurity").exists())
def security(request):
    return render(request, "shippers/security.html")


@login_required()
@user_passes_test(
    lambda u: u.groups.filter(
        Q(name="shippingPortaria") | Q(name="shippingPortariaReadOnly")
    ).exists()
)
def portaria(request):
    with timer():

        readOnly = request.user.groups.filter(name="shippingPortariaReadOnly").exists()
        entrada = request.session.get("entrada")
        saida = request.session.get("saida")
        empresas = GatewayEmpresa.objects
        condutores = GatewayCondutor.objects
        condutoresID = GatewayCondutorID.objects
        primeiraMatricula = GatewayPrimeiraMatricula.objects
        segundaMtricula = GatewaySegundaMatricula.objects
        cargaDescarga = GatewayCargaDescarga.objects
        docas = GatewayDoca.objects
        destinosCarga = GatewayDestinoCarga.objects
        elementosGateway = Gateway.objects.all()
        viatura = GatewayTipoViatura.objects.first()
        infoCondutores = GatewayInfoCondutor.objects

        p = Paginator(elementosGateway, 20)
        page_num = request.GET.get("page", 1)

        page_content = p.page(page_num)

    return render(
        request,
        "shippers/portaria.html",
        {
            "empresas": empresas,
            "condutores": condutores,
            "condutoresID": condutoresID,
            "primeiraMatricula": primeiraMatricula,
            "segundaMtricula": segundaMtricula,
            "cargaDescarga": cargaDescarga,
            "docas": docas,
            "destinosCarga": destinosCarga,
            "elementosGateway": elementosGateway,
            "viatura": viatura,
            "infoCondutores": infoCondutores,
            "readOnly": readOnly,
            "entrada": entrada,
            "saida": saida,
            "items": page_content,
            "current_page": page_num,
            "page_max": math.ceil(len(elementosGateway) / 20),
        },
    )


# elif request.user.groups.filter(name='shippingPortariaReadOnly').exists():
#     empresas = GatewayEmpresa.objects
#     condutores = GatewayCondutor.objects
#     condutoresID = GatewayCondutorID.objects
#     primeiraMatricula = GatewayPrimeiraMatricula.objects
#     segundaMtricula = GatewaySegundaMatricula.objects
#     cargaDescarga = GatewayCargaDescarga.objects
#     docas = GatewayDoca.objects
#     destinosCarga = GatewayDestinoCarga.objects
#     elementosGateway = Gateway.objects
#     viatura = GatewayTipoViatura.objects.first()
#     return render(request, 'shippers/portariaReadOnly.html',
#                   {'empresas': empresas, 'condutores': condutores, 'condutoresID': condutoresID,
#                    'primeiraMatricula': primeiraMatricula, 'segundaMtricula': segundaMtricula,
#                    'cargaDescarga': cargaDescarga, 'docas': docas, 'destinosCarga': destinosCarga,
#                    'elementosGateway': elementosGateway, 'viatura': viatura})


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="shippingTracking").exists())
def tracking(request):
    print("tracking")
    with timer():
        actualDay = datetime.today().strftime("%Y-%m-%d")
        dadosQAD = []
        gateway = Gateway.objects.filter(Q(estado="verde") | Q(estado="terminado"))
        gatewayValues = Gateway.objects.filter(
            Q(estado="verde") | Q(estado="terminado")
        ).values("primeiraMatricula")
        dadosQADabs = (
            AbsMstr.objects.filter(abs_shp_date=actualDay)
            .filter(Q(abs_id__startswith="s") | Q(abs_id__startswith="p"))
            .filter((Q(abs_type="s")) | (Q(abs_type="p")))
            .filter(abs_shipfrom="3515")
            .values(
                "abs_id",
                "abs_shp_date",
                "abs_shp_time",
                "abs_qad01",
                "oid_abs_mstr",
                "abs_status",
                "abs_shipto",
                "abs_item",
                "abs_domain",
            )
        )
        dadosQADad = (
            AdMstr.objects.filter(ad_addr__in=dadosQADabs.values_list("abs_shipto"))
            .values("ad_addr", "ad_city", "ad_country")
            .distinct()
        )

        for abs in dadosQADabs.all():
            abs["abs_shp_time"] = str(convert(abs["abs_shp_time"]))
            if abs["abs_status"][1:2] == "y":
                abs["abs_status"] = "Yes"
            else:
                abs["abs_status"] = "No"
            QADad = dadosQADad.filter(ad_addr=abs["abs_shipto"]).distinct()
            for ad in QADad.all():
                row = {
                    "id": abs["abs_id"],
                    "shipDate": str(abs["abs_shp_date"])[0:10],
                    "shipTime": abs["abs_shp_time"],
                    "city": ad["ad_city"],
                    "country": ad["ad_country"],
                    "carrier": "",
                    "fob": abs["abs_qad01"][20:40],
                    "modeOfTransport": abs["abs_qad01"][60:80],
                    "vehicleID": abs["abs_qad01"][80:100],
                    "totalMasterPacks": str(abs["oid_abs_mstr"]),
                    "confirmed": abs["abs_status"],
                    "itemNumber": "",
                    "description": "",
                    "qtyToShip": "",
                    "qtyShipped": "",
                }
                dadosQAD.append(row)

    return render(
        request, "shippers/shipping.html", {"dadosQAD": dadosQAD, "gateway": gateway}
    )


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="admin").exists())
def tracking2(request):
    print("Tracking2")
    with timer():
        actualDay = datetime.today().strftime("%Y-%m-%d")
        dadosQAD = []
        dadosQADabs = (
            AbsMstr.objects.filter(abs_shp_date=actualDay)
            .filter(Q(abs_id__startswith="s") | Q(abs_id__startswith="p"))
            .filter((Q(abs_type="s")) | (Q(abs_type="p")))
            .filter(abs_shipfrom="3515")
            .values(
                "abs_id",
                "abs_shp_date",
                "abs_shp_time",
                "abs_qad01",
                "oid_abs_mstr",
                "abs_status",
                "abs_shipto",
                "abs_item",
                "abs_domain",
            )
        )
        dadosQADad = (
            AdMstr.objects.filter(ad_addr__in=dadosQADabs.values_list("abs_shipto"))
            .values("ad_addr", "ad_city", "ad_country")
            .distinct()
        )
        dadosQADabsc = AbscDet.objects.filter(
            absc_abs_id__in=dadosQADabs.values_list("abs_id")
        ).values("absc_abs_id", "absc_carrier")
        dadosQADabsALTERADOS = AbsMstr.objects.filter(
            abs_par_id__in=dadosQADabs.values_list("abs_id")
        ).values("abs_par_id", "abs_item", "abs_qty", "abs_ship_qty")
        dadosQADpt = PtMstr.objects.filter(
            pt_part__in=dadosQADabsALTERADOS.values_list("abs_item")
        ).values("pt_desc1", "pt_desc2", "pt_part")
        AbsMstrPriv.objects.all().delete()
        AdPriv.objects.all().delete()
        AbscPriv.objects.all().delete()
        Abs2Priv.objects.all().delete()
        PtPriv.objects.all().delete()
        for abs in dadosQADabs.all():
            row = AbsMstrPriv(
                None,
                abs["abs_id"],
                str(abs["abs_shp_date"])[0:10],
                str(abs["abs_shp_time"]),
                abs["abs_qad01"],
                str(abs["oid_abs_mstr"]),
                abs["abs_status"],
                abs["abs_shipto"],
                abs["abs_item"],
                abs["abs_domain"],
            )
            row.save()

        for abs in AbsMstrPriv.objects.all():
            for ad in dadosQADad.all():
                if ad["ad_addr"] == abs.abs_shipto_2:
                    rowAD = AdPriv()
                    rowAD.ad_addr_2 = (abs,)
                    rowAD.ad_city_2 = (ad["ad_city"],)
                    rowAD.ad_country_2 = ad["ad_country"]
                    rowAD.save()
            for pt in dadosQADpt.all():
                if pt["pt_part"] == abs.abs_item:
                    rowAD = AdPriv(None, pt["pt_desc1"], pt["pt_desc2"], abs.abs_item)
                    rowAD.save()
            for absc in dadosQADabsc.all():
                if absc["absc_abs_id"] == abs.abs_id:
                    rowABSC = AbscPriv(None, abs.abs_id, absc["absc_carrier"])
                    rowABSC.save()
            for abs2 in dadosQADabsALTERADOS.all():
                if abs2["abs_par_id"] == abs.abs_id:
                    rowABS2 = Abs2Priv(
                        None,
                        abs.abs_id,
                        abs2["abs_item"],
                        abs2["abs_qty"],
                        abs2["abs_shp_qty"],
                    )
                    rowABS2.save()

            rowAbs = {
                "id": abs["abs_id"],
                "shipDate": str(abs["abs_shp_date"])[0:10],
                "shipTime": abs["abs_shp_time"],
                "fob": abs["abs_qad01"][20:40],
                "modeOfTransport": abs["abs_qad01"][60:80],
                "vehicleID": abs["abs_qad01"][80:100],
                "totalMasterPacks": str(abs["oid_abs_mstr"]),
                "confirmed": abs["abs_status"],
            }

            rowAd = {}
            if dadosQADad.filter(ad_addr=abs["abs_shipto"]).exists():
                ad = dadosQADad.filter(ad_addr=abs["abs_shipto"])[0]
                rowAd = {"city": ad["ad_city"], "country": ad["ad_country"]}

            rowAbsc = {}
            if dadosQADabsc.filter(absc_abs_id=abs["abs_id"]).exists():
                absc = dadosQADabsc.get(absc_abs_id=abs["abs_id"])
                rowAbsc = {
                    "carrier": absc["absc_carrier"],
                }

            if dadosQADabsALTERADOS.filter(abs_par_id=abs["abs_id"]).exists():
                for abs2 in dadosQADabsALTERADOS.filter(
                    abs_par_id=abs["abs_id"]
                ).distinct():
                    rowAbs2 = {
                        "itemNumber": abs2["abs_item"],
                        "qtyToShip": str(abs2["abs_qty"]),
                        "qtyShipped": str(abs2["abs_ship_qty"]),
                    }

                    rowPt = {}

                    if dadosQADpt.filter(pt_part=abs["abs_item"]).exists():
                        pt = dadosQADpt.get(pt_part=abs["abs_item"])
                        rowPt = {
                            "description": pt["pt_desc1"] + pt["pt_desc2"],
                        }
                    mergedRow = rowAbs | rowAd | rowAbsc | rowPt | rowAbs2
                    dadosQAD.append(mergedRow)
            else:
                mergedRow = rowAbs | rowAd | rowAbsc
                dadosQAD.append(mergedRow)

        # for abs in dadosQADabs.all():
        #     rowAbs2 = {}
        #     if dadosQADabsALTERADOS.filter(abs_par_id=abs['abs_id']).exists():
        #         for abs2 in dadosQADabsALTERADOS.filter(abs_par_id=abs['abs_id']):
        #             rowAbs2 = {
        #                 'itemNumber': abs2['abs_item'],
        #                 'qtyToShip': str(abs2['abs_qty']),
        #                 'qtyShipped': str(abs2['abs_ship_qty'])
        #             }
        #
        #             rowPt = {}
        #
        #             if dadosQADpt.filter(pt_part= abs['abs_item']).exists():
        #                 pt = dadosQADpt.get(pt_part= abs['abs_item'])
        #                 rowPt = {
        #                     'description': pt['pt_desc1'] + pt['pt_desc2'],
        #                 }
        #             mergedRow = rowPt | rowAbs2
        #             dadosQAD.append(mergedRow)

        # for abs in dadosQADabs.all():
        #     if dadosQADabsALTERADOS.filter(abs_par_id=abs['abs_id']).exists() and dadosQADad.filter(
        #             ad_addr=abs['abs_shipto']).exists() and dadosQADabsc.filter(absc_abs_id=abs['abs_id']).exists():
        #         row = {
        #             'id': abs['abs_id'],
        #             'shipDate': str(abs['abs_shp_date'])[0:10],
        #             'shipTime': abs['abs_shp_time'],
        #             'city': '',
        #             'country': '',
        #             'carrier': '',
        #             'fob': abs['abs_qad01'][20:40],
        #             'modeOfTransport': abs['abs_qad01'][60:80],
        #             'vehicleID': abs['abs_qad01'][80:100],
        #             'totalMasterPacks': str(abs['oid_abs_mstr']),
        #             'confirmed': abs['abs_status'],
        #             'itemNumber': '',
        #             'description': '',
        #             'qtyToShip': '',
        #             'qtyShipped': ''
        #         }
        #         dadosQAD.append(row)
        #
        #     for pt in dadosQADpt.all():
        #         if abs['abs_item'] == pt['pt_part']:
        #             row = {
        #                 'id': abs['abs_id'],
        #                 'shipDate': str(abs['abs_shp_date'])[0:10],
        #                 'shipTime': abs['abs_shp_time'],
        #                 'city': '',
        #                 'country': '',
        #                 'carrier': '',
        #                 'fob': abs['abs_qad01'][20:40],
        #                 'modeOfTransport': abs['abs_qad01shipping.html'][60:80],
        #                 'vehicleID': abs['abs_qad01'][80:100],
        #                 'totalMasterPacks': str(abs['oid_abs_mstr']),
        #                 'confirmed': abs['abs_status'],
        #                 'itemNumber': '',
        #                 'description': '',
        #                 'qtyToShip': '',
        #                 'qtyShipped': ''
        #             }
        #             dadosQAD.append(row)

        return render(request, "shippers/shipping.html", {"dadosQAD": dadosQAD})

    # for abs in dadosQADabs.all():
    #
    #     abs['abs_shp_time'] = str(convert(abs['abs_shp_time']))
    #     if abs['abs_status'][1:2] == 'y':
    #         abs['abs_status'] = 'Yes'
    #     else:
    #         abs['abs_status'] = 'No'
    #     description = ''
    #     abs_item = AbsMstr.objects.values_list('abs_item', flat=True).filter(abs_par_id=abs['abs_id']).last()
    #     abs_qty = AbsMstr.objects.values_list('abs_qty', flat=True).filter(abs_par_id=abs['abs_id']).last()
    #     abs_ship_qty = AbsMstr.objects.values_list('abs_ship_qty', flat=True).filter(abs_par_id=abs['abs_id']).last()
    #     pt_desc1 = PtMstr.objects.values_list('pt_desc1', flat=True).filter(pt_part=abs_item).last()
    #     pt_desc2 = PtMstr.objects.values_list('pt_desc2', flat=True).filter(pt_part=abs_item).last()
    #     ad_city = AdMstr.objects.values_list('ad_city', flat=True).filter(ad_domain=abs['abs_domain'],
    #                                                                       ad_addr=abs['abs_shipto']).last()
    #     ad_country = AdMstr.objects.values_list('ad_country', flat=True).filter(ad_domain=abs['abs_domain'],
    #                                                                             ad_addr=abs['abs_shipto']).last()
    #     absc_carrier = AbscDet.objects.values_list('absc_carrier', flat=True).filter(absc_abs_id=abs['abs_id']).last()
    #     if pt_desc1 is None:
    #         pt_desc1 = ''
    #     if pt_desc2 is None:
    #         pt_desc2 = ''
    #     if abs_item is None:
    #         abs_item = ''
    #     if abs_qty is None:
    #         abs_qty = ''
    #     if abs_ship_qty is None:
    #         abs_ship_qty = ''
    #     description += pt_desc1
    #     if pt_desc1 is None:
    #         pt_desc1 = ''
    #     if len(pt_desc1) == 24:
    #         aux = ' '
    #     else:
    #         aux = ''
    #     description += aux + pt_desc2
    #     row = {
    #         'id': abs['abs_id'],
    #         'shipDate': str(abs['abs_shp_date'])[0:10],
    #         'shipTime': abs['abs_shp_time'],
    #         'city': ad_city,
    #         'country': ad_country,
    #         'carrier': absc_carrier,
    #         'fob': abs['abs_qad01'][20:40],
    #         'modeOfTransport': abs['abs_qad01'][60:80],
    #         'vehicleID': abs['abs_qad01'][80:100],
    #         'totalMasterPacks': str(abs['oid_abs_mstr']),
    #         'confirmed': abs['abs_status'],
    #         'itemNumber': abs_item,
    #         'description': aux,
    #         'qtyToShip': abs_qty,
    #         'qtyShipped': abs_ship_qty
    #     }
    #     dadosQAD.append(row)

    # for abs in dadosQADabs.all():
    #     control = 0
    #     for absc in dadosQADabsc.all():
    #         if abs['abs_id'] == absc['absc_abs_id']:
    #             for ad in dadosQADad.all():
    #                 if abs['abs_shipto'] == ad['ad_addr']:
    #                     for absALT in dadosQADabsALTERADOS.all():
    #                         if absALT['abs_par_id'] == abs['abs_id']:
    #                             for pt in dadosQADpt.all():
    #                                 if pt['pt_part'] == absALT['abs_item']:
    #                                     abs['abs_shp_time'] = str(convert(abs['abs_shp_time']))
    #                                     if abs['abs_status'][1:2] == 'y':
    #                                         abs['abs_status'] = 'Yes'
    #                                     else:
    #                                         abs['abs_status'] = 'No'
    #                                     if len(pt['pt_desc1']) == 24:
    #                                          aux = ' '
    #                                     else: aux = ''
    #                                     row = {
    #                                         'id': abs['abs_id'],
    #                                         'shipDate': str(abs['abs_shp_date'])[0:10],
    #                                         'shipTime': abs['abs_shp_time'],
    #                                         'city': ad['ad_city'],
    #                                         'country': ad['ad_country'],
    #                                         'carrier': absc['absc_carrier'],
    #                                         'fob': abs['abs_qad01'][20:40],
    #                                         'modeOfTransport': abs['abs_qad01'][60:80],
    #                                         'vehicleID': abs['abs_qad01'][80:100],
    #                                         'totalMasterPacks': str(abs['oid_abs_mstr']),
    #                                         'confirmed': abs['abs_status'],
    #                                         'itemNumber': absALT['abs_item'],
    #                                         'description': pt['pt_desc1']+aux+pt['pt_desc2'],
    #                                         'qtyToShip': str(absALT['abs_qty']),
    #                                         'qtyShipped': str(absALT['abs_ship_qty'])
    #                                     }
    #                                     dadosQAD.append(row)
    #                                     control = 1
    #                                 if control == 1:
    #                                     break
    #                         if control == 1:
    #                             break
    #                 if control == 1:
    #                     break
    #         if control == 1:
    #             break


# def getInfoConfirmationData(request):
#    if request.is_ajax():
#       ficheiro_Shippers = finalFicheiroShippers.objects.all()
#       file_serializer = serializers.serialize('json', ficheiro_Shippers)
#       return JsonResponse(file_serializer, safe=False)

# utilizado em shippersTracking
def uploadFiles(request):
    if request.method == "POST":
        # if request.FILES.get('browseFile') and request.FILES.get('detailFile'):
        # browseDatabook = tablib.Databook()
        # detailDatabook = tablib.Databook()
        # browseFile = request.FILES['browseFile']
        # detailFile = request.FILES['detailFile']

        # if not browseFile.name.endswith('xlsx') or not detailFile.name.endswith('xlsx'):
        #    path = Path.objects
        #    return render(request, 'shippers/shippersTracking.html',
        #                  {"path": path, "erro2": "WRONG FORMAT! Only xlsx files"})

        excel_files = [
            "//PAVPD002/E_Proj/sharedir/MP&L/Warehouse/PWMS/Shipping/Teste_Browse.xlsx",
            "//PAVPD002/E_Proj/sharedir/MP&L/Warehouse/PWMS/Shipping/Teste_Detail.xlsx",
        ]

        filteredTable.objects.all().delete()
        Teste_browse.objects.all().delete()
        Teste_detail.objects.all().delete()

        # imported_browse = browseDatabook.load(browseFile.read(), format='xlsx')
        # imported_detail = detailDatabook.load(detailFile.read(), format='xlsx')

        # for data in imported_browse.sheets():
        for file in excel_files:
            if (
                file
                == "//PAVPD002/E_Proj/sharedir/MP&L/Warehouse/PWMS/Shipping/Teste_Browse.xlsx"
            ):
                workbook = openpyxl.load_workbook(file)
                worksheet = workbook["Sheet1"]
                for element in worksheet:
                    value2 = Teste_browse(
                        None,
                        element[0].value,
                        element[1].value,
                        element[2].value,
                        element[3].value,
                        element[4].value,
                        element[5].value,
                        element[6].value,
                        element[7].value,
                        element[8].value,
                        element[9].value,
                        element[10].value,
                        element[11].value,
                        element[12].value,
                        element[13].value,
                        element[14].value,
                        element[15].value,
                        element[16].value,
                        element[17].value,
                        element[18].value,
                        element[19].value,
                        element[20].value,
                        element[21].value,
                        element[22].value,
                    )
                    value2.save()
                    # cria elemento na filteredTable com dados apenas do ficheiro Teste Browse
                    tabelaFiltrada = filteredTable(
                        None,
                        element[2].value,
                        element[8].value,
                        element[9].value,
                        element[4].value,
                        element[5].value,
                        element[10].value,
                        element[13].value,
                        element[14].value,
                        None,
                        None,
                        None,
                        None,
                        element[19].value,
                        element[20].value,
                    )
                    tabelaFiltrada.save()

            if (
                file
                == "//PAVPD002/E_Proj/sharedir/MP&L/Warehouse/PWMS/Shipping/Teste_Detail.xlsx"
            ):
                workbook = openpyxl.load_workbook(file)
                worksheet = workbook["Sheet1"]
                # for data in imported_detail.sheets():
                for element in worksheet:
                    for elementoTabelaFiltrada in filteredTable.objects.all():
                        if elementoTabelaFiltrada.idComum == element[2].value:
                            # complementa os elementos que estao na filteredTable com dados do ficheiro Teste Detail
                            if (
                                elementoTabelaFiltrada.itemNumber == None
                                and elementoTabelaFiltrada.quantityShipped == None
                                and elementoTabelaFiltrada.description == None
                                and elementoTabelaFiltrada.quantityToShip == None
                            ):
                                elementoTabelaFiltrada.itemNumber = element[7].value
                                elementoTabelaFiltrada.description = element[8].value
                                elementoTabelaFiltrada.quantityToShip = element[9].value
                                elementoTabelaFiltrada.quantityShipped = element[
                                    10
                                ].value
                                elementoTabelaFiltrada.save()
                            # caso haja mais que um elemento com aquele idComum, cria novo
                            else:
                                novoElemento = filteredTable(
                                    None,
                                    elementoTabelaFiltrada.idComum,
                                    elementoTabelaFiltrada.shipDate,
                                    elementoTabelaFiltrada.shipTime,
                                    elementoTabelaFiltrada.name,
                                    elementoTabelaFiltrada.city,
                                    elementoTabelaFiltrada.carrier,
                                    elementoTabelaFiltrada.modeOfTransport,
                                    elementoTabelaFiltrada.vehicleID,
                                    element[7].value,
                                    element[8].value,
                                    element[9].value,
                                    element[10].value,
                                    elementoTabelaFiltrada.inProcess,
                                    elementoTabelaFiltrada.confirmed,
                                )
                                novoElemento.save()

                    value = Teste_detail(
                        None,
                        element[0].value,
                        element[1].value,
                        element[2].value,
                        element[3].value,
                        element[4].value,
                        element[5].value,
                        element[6].value,
                        element[7].value,
                        element[8].value,
                        element[9].value,
                        element[10].value,
                        element[11].value,
                        element[12].value,
                        element[13].value,
                        element[14].value,
                        element[15].value,
                        element[16].value,
                        element[17].value,
                        element[18].value,
                        element[19].value,
                        element[20].value,
                        element[21].value,
                    )
                    value.save()

    return redirect("shippers:shippersTracking")


# filtra alguns campos de diferentes sheets e guarda na base de dados. utilizado em shippers
def uploadDataExcel(request):
    if request.method == "POST":
        excel_file = [
            "//PAVPD002/E_Proj/sharedir/MP&L/Warehouse/PWMS/Shipping/Shippers Tracking.xlsx"
        ]
        workbook = openpyxl.load_workbook(excel_file[0])
        for sheet in workbook:
            if sheet.title == "Pre-Shipper Browse":
                # if PreShipperBrowse.objects.get(shipDate=sheet[1][6].value):
                # return
                # caso seja igual, ver as diferenças linha a linha e acrescentar
                # else:
                PreShipperBrowse.objects.all().delete()
                for element in sheet:
                    value2 = PreShipperBrowse(
                        None,
                        element[0].value,
                        element[1].value,
                        element[2].value,
                        element[3].value,
                        element[4].value,
                        element[5].value,
                        element[6].value,
                        element[7].value,
                        element[8].value,
                        element[9].value,
                        element[10].value,
                        element[11].value,
                        element[12].value,
                        element[13].value,
                        element[14].value,
                        element[15].value,
                        element[16].value,
                        element[17].value,
                        element[18].value,
                        element[19].value,
                        element[20].value,
                        element[21].value,
                    )
                    value2.save()

            if sheet.title == "Pre-Shipper Detail Browse":
                PreShipperDetailBrowse.objects.all().delete()
                for element in sheet:
                    value2 = PreShipperDetailBrowse(
                        None,
                        element[0].value,
                        element[1].value,
                        element[2].value,
                        element[3].value,
                        element[4].value,
                        element[5].value,
                        element[6].value,
                        element[7].value,
                        element[8].value,
                        element[9].value,
                        element[10].value,
                        element[11].value,
                        element[12].value,
                        element[13].value,
                        element[14].value,
                        element[15].value,
                        element[16].value,
                        element[17].value,
                        element[18].value,
                        element[19].value,
                        element[20].value,
                        element[21].value,
                    )
                    value2.save()
    return redirect("shippers:shippersTracking")


def getChildValues(request):
    with timer():
        print("getChild Values")
        if request.method == "GET":
            shipperID = request.GET["shipperID"]
            listTableValues = list(
                PreShipperDetailBrowse.objects.filter(idShipper=shipperID).values()
            )
        return JsonResponse({"filteredTableValues": listTableValues})


def getDataFicheiro(request):
    if request.method == "GET":
        dataAtualFicheiro = request.GET["dataAtualFicheiro"]
        excel_file = [
            "//PAVPD002/E_Proj/sharedir/MP&L/Warehouse/PWMS/Shipping/Shippers Tracking.xlsx"
        ]
        workbook = openpyxl.load_workbook(excel_file[0])
        data = ""
        for sheet in workbook:
            if sheet.title == "Pre-Shipper Browse":
                for element in sheet:
                    data = element[8].value
        return JsonResponse({"dataFicheiro": data})


def uploadShippersConfirmation(request):
    if request.method == "POST":
        if request.FILES.get("ficheiroConfirmacao"):

            ficheiroShippers.objects.all().delete()
            finalFicheiroShippers.objects.all().delete()

            ficheiroConfirmacao = [request.FILES["ficheiroConfirmacao"]]
            workbook = openpyxl.load_workbook(ficheiroConfirmacao[0])

            for sheet in workbook:
                if sheet.title == "extended packaging data browse":
                    for element in sheet:
                        novoElemento = ficheiroShippers(
                            None,
                            element[0].value,
                            element[2].value,
                            element[5].value,
                            element[10].value,
                        )
                        novoElemento.save()

            totalFicheiros = ficheiroShippers.objects.all()
            masterSerial = None
            preShipper = None
            pack = None
            packAnterior = None
            numberPack = None
            totalPacks = 0
            for linha in totalFicheiros:
                if linha.masterSerialID == masterSerial:
                    if linha.packItem == pack:
                        totalPacks = totalPacks + int(linha.numberOfPacks, base=10)
                    else:
                        novoElemento = finalFicheiroShippers(
                            None, masterSerial, preShipper, pack, totalPacks
                        )
                        novoElemento.save()
                        totalPacks = int(linha.numberOfPacks, base=10)
                else:
                    if linha.numberOfPacks != "Number of Packs":
                        if pack == packAnterior:
                            totalPacks = totalPacks
                            novoElemento = finalFicheiroShippers(
                                None, masterSerial, preShipper, pack, totalPacks
                            )
                            novoElemento.save()
                            totalPacks = int(linha.numberOfPacks, base=10)
                        else:
                            totalPacks = int(linha.numberOfPacks, base=10)
                            novoElemento = finalFicheiroShippers(
                                None, masterSerial, preShipper, pack, numberPack
                            )
                            novoElemento.save()

                masterSerial = linha.masterSerialID
                preShipper = linha.preShipperShipper
                packAnterior = pack
                pack = linha.packItem
                numberPack = linha.numberOfPacks

            # Para alcançar o ultimo elemento da lista
            for i in range(0, len(totalFicheiros)):
                if i == (len(totalFicheiros) - 1):
                    novoElemento = finalFicheiroShippers(
                        None, masterSerial, preShipper, pack, numberPack
                    )
                    novoElemento.save()

    return redirect("shippers:shippersConfirmation")


def resetVeiculoDB(request):
    if request.method == "POST":
        GatewayTipoViatura.objects.all().delete()
    return redirect("shippers:portaria")


def submitGatewayRowUpdate(request):
    if (
        request.method == "POST"
        and request.user.groups.filter(name="shippingPortaria").exists()
    ):
        dataHoraEntrada = ""
        abandono = request.POST["abandono"]
        comentariosEntrada = request.POST["comentariosEntrada"]
        dataHoraSaida = ""
        comentariosSaida = request.POST["comentariosSaida"]
        id = request.POST["id"]
        enviarEmailAbandonado = ""

        if request.POST["dataHoraEntrada"] != "":
            dataHoraEntrada = request.POST["dataHoraEntrada"]
        if request.POST["dataHoraSaida"] != "":
            dataHoraSaida = request.POST["dataHoraSaida"]

        elemento = Gateway.objects.get(id=id)
        if dataHoraSaida != "":
            elemento.dataHoraSaida = dataHoraSaida
        if dataHoraEntrada != "":
            elemento.dataHoraEntrada = dataHoraEntrada
            elemento.estado = "terminado"

        if elemento.abandono == "true":
            if abandono == "false":
                elemento.dataHoraEntrada = ""
                elemento.estado = ""
                enviarEmailAbandonado = "voltou"
        else:
            if abandono == "true":
                elemento.dataHoraEntrada = datetime.today().strftime("%Y-%m-%d %H:%M")
                elemento.dataHoraSaida = datetime.today().strftime("%Y-%m-%d %H:%M")
                elemento.estado = "terminado"
                enviarEmailAbandonado = "abandonou"
        elemento.abandono = abandono
        if comentariosEntrada != "":
            elemento.comentEntrada = comentariosEntrada
        if comentariosSaida != "":
            elemento.comentSaida = comentariosSaida
        if elemento.dataHoraSaida != "" or elemento.abandono == "true":
            elemento.estado = "feitoEsaiu"
        elemento.save()

        # alterei a primeira linha, e adicionei a cor diretamente no style das células
        if enviarEmailAbandonado == "abandonou":
            table = '</br><table class="display"><thead style="background-color: lightgray"><tr><th>DATA/HORA CHEGADA</th><th>CONDUTOR</th><th>ID</th><th>CONTACTO</th><th>EMPRESA</th><th>1ª MATRICULA</th><th>2ª MATRICULA</th><th>CARGA/DESCARGA</th><th>DOCA</th><th>DESTINO CARGA</th><th>TIPO VIATURA</th><th>DATA/HORA ENTRADA</th><th>ABANDONO</th><th>COMENTARIOS ENTRADA</th><th>DATA/HORA SAIDA</th><th>COMENTARIOS SAIDA</th></tr></thead><tbody>'

            table += (
                '</td><td style="padding:0 15px 0 15px;background-color: red">'
                + elemento.dataHoraChegada
                + '</td><td style="padding:0 15px 0 15px;background-color: red">'
                + elemento.condutor
                + '</td><td style="padding:0 15px 0 15px;background-color: red">'
                + elemento.ident
                + '</td><td style="padding:0 15px 0 15px;background-color: red">'
                + elemento.contacto
                + '</td><td style="padding:0 15px 0 15px;background-color: red">'
                + elemento.empresa
                + '</td><td style="padding:0 15px 0 15px;background-color: red">'
                + elemento.primeiraMatricula
                + '</td><td style="padding:0 15px 0 15px;background-color: red">'
                + elemento.segundaMatricula
                + '</td><td style="padding:0 15px 0 15px;background-color: red">'
                + elemento.cargaDescarga
                + '</td><td style="padding:0 15px 0 15px;background-color: red">'
                + elemento.doca
                + '</td><td style="padding:0 15px 0 15px;background-color: red">'
                + elemento.destinoCarga
                + '</td><td style="padding:0 15px 0 15px;background-color: red">'
                + elemento.tipoViatura
                + '</td><td style="padding:0 15px 0 15px; text-align: center;background-color: red">'
                + elemento.dataHoraEntrada
                + '</td><td style="padding:0 15px 0 15px; text-align: center;background-color: red">'
                + "X"
                + '</td><td style="padding:0 15px 0 15px; text-align: center;background-color: red">'
                + elemento.comentEntrada
                + '</td><td style="padding:0 15px 0 15px;background-color: red">'
                + elemento.dataHoraSaida
                + '</td><td style="padding:0 15px 0 15px;background-color: red">'
                + elemento.comentEntrada
                + "</td></tr>"
            )
            table += (
                '<tr style="background-color: lightgray"><td colspan="18"> </td></tr>'
            )
            table += "</body></table>"

            subject, from_email, to = (
                "Alteração em Shipping - Portaria",
                "noreply@visteon.com",
                ["pmarti30@visteon.com"],
            )

            # [ 'aroque1@visteon.com', 'npires2@visteon.com', 'pmarti30@visteon.com']

            msg = EmailMultiAlternatives(subject, table, from_email, to)
            msg.attach_alternative(table, "text/html")
            msg.send()
            # alterei a primeira linha, e adicionei a cor diretamente no style das células
        if enviarEmailAbandonado == "voltou":
            table = '</br><table class="display"><thead style="background-color: lightgray"><tr><th>DATA/HORA CHEGADA</th><th>CONDUTOR</th><th>ID</th><th>CONTACTO</th><th>EMPRESA</th><th>1ª MATRICULA</th><th>2ª MATRICULA</th><th>CARGA/DESCARGA</th><th>DOCA</th><th>DESTINO CARGA</th><th>TIPO VIATURA</th><th>DATA/HORA ENTRADA</th><th>ABANDONO</th><th>COMENTARIOS ENTRADA</th><th>DATA/HORA SAIDA</th><th>COMENTARIOS SAIDA</th></tr></thead><tbody>'
            #'<tr style="background-color: whitesmoke">' + \
            table += (
                '</td><td style="padding:0 15px 0 15px;background-color: whitesmoke">'
                + elemento.dataHoraChegada
                + '</td><td style="padding:0 15px 0 15px;background-color: whitesmoke">'
                + elemento.condutor
                + '</td><td style="padding:0 15px 0 15px;background-color: whitesmoke">'
                + elemento.ident
                + '</td><td style="padding:0 15px 0 15px;background-color: whitesmoke">'
                + elemento.contacto
                + '</td><td style="padding:0 15px 0 15px;background-color: whitesmoke">'
                + elemento.empresa
                + '</td><td style="padding:0 15px 0 15px;background-color: whitesmoke">'
                + elemento.primeiraMatricula
                + '</td><td style="padding:0 15px 0 15px;background-color: whitesmoke">'
                + elemento.segundaMatricula
                + '</td><td style="padding:0 15px 0 15px;background-color: whitesmoke">'
                + elemento.cargaDescarga
                + '</td><td style="padding:0 15px 0 15px;background-color: whitesmoke">'
                + elemento.doca
                + '</td><td style="padding:0 15px 0 15px;background-color: whitesmoke">'
                + elemento.destinoCarga
                + '</td><td style="padding:0 15px 0 15px;background-color: whitesmoke">'
                + elemento.tipoViatura
                + '</td><td style="padding:0 15px 0 15px; text-align: center;background-color: whitesmoke">'
                + elemento.dataHoraEntrada
                + '</td><td style="padding:0 15px 0 15px; text-align: center;background-color: whitesmoke">'
                + ""
                + '</td><td style="padding:0 15px 0 15px; text-align: center;background-color: whitesmoke">'
                + elemento.comentEntrada
                + '</td><td style="padding:0 15px 0 15px;background-color: whitesmoke">'
                + elemento.dataHoraSaida
                + '</td><td style="padding:0 15px 0 15px;background-color: whitesmoke">'
                + elemento.comentEntrada
                + "</td></tr>"
            )
            table += (
                '<tr style="background-color: lightgray"><td colspan="18"> </td></tr>'
            )
            table += "</body></table>"

            subject, from_email, to = (
                "Alteração em Shipping - Portaria",
                "noreply@visteon.com",
                ["pmarti30@visteon.com"],
            )

            #'aroque1@visteon.com', 'npires2@visteon.com','pmarti30@visteon.com']

            msg = EmailMultiAlternatives(subject, table, from_email, to)
            msg.attach_alternative(table, "text/html")
            msg.send()
        return redirect("shippers:portaria")

    elif not request.user.groups.filter(name="shippingPortaria").exists():
        empresas = GatewayEmpresa.objects
        condutores = GatewayCondutor.objects
        primeiraMatricula = GatewayPrimeiraMatricula.objects
        segundaMtricula = GatewaySegundaMatricula.objects
        cargaDescarga = GatewayCargaDescarga.objects
        docas = GatewayDoca.objects
        destinosCarga = GatewayDestinoCarga.objects
        elementosGateway = Gateway.objects
        viatura = GatewayTipoViatura.objects.first()
        return render(
            request,
            "shippers/portaria.html",
            {
                "empresas": empresas,
                "condutores": condutores,
                "primeiraMatricula": primeiraMatricula,
                "segundaMtricula": segundaMtricula,
                "cargaDescarga": cargaDescarga,
                "docas": docas,
                "destinosCarga": destinosCarga,
                "elementosGateway": elementosGateway,
                "erro": "Não tem permissão para fazer alterações",
                "viatura": viatura,
            },
        )
    else:
        return redirect("shippers:portaria")


def submitPortaria(request):
    if (
        request.method == "POST"
        and request.user.groups.filter(name="shippingPortaria").exists()
    ):
        empresa = request.POST["empresa"]
        if not GatewayEmpresa.objects.filter(nome=empresa).exists():
            GatewayEmpresa(None, empresa).save()
        condutor = request.POST["condutor"]
        if not GatewayCondutor.objects.filter(nome=condutor).exists():
            GatewayCondutor(None, condutor).save()
        condutorID = request.POST["condutorID"]
        if not GatewayCondutorID.objects.filter(nome=condutorID).exists():
            GatewayCondutorID(None, condutorID).save()
        matricula1 = request.POST["1matricula"]
        if not GatewayPrimeiraMatricula.objects.filter(nome=matricula1).exists():
            GatewayPrimeiraMatricula(None, matricula1).save()
        matricula2 = request.POST["2matricula"]
        if not GatewaySegundaMatricula.objects.filter(nome=matricula2).exists():
            GatewaySegundaMatricula(None, matricula2).save()
        cargaDescarga = request.POST["cargaDescarga"]
        if not GatewayCargaDescarga.objects.filter(nome=cargaDescarga).exists():
            GatewayCargaDescarga(None, cargaDescarga).save()
        doca = request.POST["doca"]
        if not GatewayDoca.objects.filter(nome=doca).exists():
            GatewayDoca(None, doca).save()
        destinoCarga = request.POST["destinoCarga"]
        if not GatewayDestinoCarga.objects.filter(nome=destinoCarga).exists():
            GatewayDestinoCarga(None, destinoCarga).save()
        contacto = request.POST["contacto"]
        if not GatewayContactoCondutor.objects.filter(nome=contacto).exists():
            GatewayContactoCondutor(None, contacto).save()
        dataHoraChegada = datetime.today().strftime("%Y-%m-%d %H:%M")
        viatura = GatewayTipoViatura.objects.first()

        novoElemento = Gateway(
            None,
            dataHoraChegada,
            empresa,
            condutor,
            condutorID,
            contacto,
            matricula1,
            matricula2,
            cargaDescarga,
            doca,
            destinoCarga,
            viatura,
            "",
            "",
            "",
            "",
            "",
            "",
        )
        novoElemento.save()
        condutorP = ""
        condutorIDP = ""
        contactoP = ""
        empresaP = ""
        if GatewayCondutor.objects.filter(nome=condutor).exists():
            condutorP = GatewayCondutor.objects.get(nome=condutor)
        if GatewayCondutorID.objects.filter(nome=condutorID).exists():
            condutorIDP = GatewayCondutorID.objects.get(nome=condutorID)
        if GatewayContactoCondutor.objects.filter(nome=contacto).exists():
            contactoP = GatewayContactoCondutor.objects.get(nome=contacto)
        if GatewayEmpresa.objects.filter(nome=empresa).exists():
            empresaP = GatewayEmpresa.objects.get(nome=empresa)
        if GatewayInfoCondutor.objects.filter(
            Q(condutor=condutorP) | Q(condutorID=condutorIDP) | Q(contacto=contactoP)
        ).exists():
            GatewayInfoCondutor.objects.filter(
                Q(condutor=condutorP)
                | Q(condutorID=condutorIDP)
                | Q(contacto=contactoP)
            ).delete()
        novoCondutor = GatewayInfoCondutor(
            None, condutorP.id, condutorIDP.id, contactoP.id, empresaP.id
        )
        novoCondutor.save()
        GatewayTipoViatura.objects.all().delete()
        return redirect("shippers:portaria")
    else:
        empresas = GatewayEmpresa.objects
        condutores = GatewayCondutor.objects
        primeiraMatricula = GatewayPrimeiraMatricula.objects
        segundaMtricula = GatewaySegundaMatricula.objects
        cargaDescarga = GatewayCargaDescarga.objects
        docas = GatewayDoca.objects
        destinosCarga = GatewayDestinoCarga.objects
        elementosGateway = Gateway.objects
        viatura = GatewayTipoViatura.objects.first()
        return render(
            request,
            "shippers/portaria.html",
            {
                "empresas": empresas,
                "condutores": condutores,
                "primeiraMatricula": primeiraMatricula,
                "segundaMtricula": segundaMtricula,
                "cargaDescarga": cargaDescarga,
                "docas": docas,
                "destinosCarga": destinosCarga,
                "elementosGateway": elementosGateway,
                "erro": "Não tem permissão para fazer alterações",
                "viatura": viatura,
            },
        )


def submitViatura(request):
    if request.method == "POST":
        posicao = request.POST["data"]

        if posicao == "":
            GatewayTipoViatura.objects.all().delete()
            return redirect("shippers:portaria")

        GatewayTipoViatura.objects.all().delete()
        viatura = GatewayTipoViatura()
        viatura.nome = posicao
        viatura.save()
        return redirect("shippers:portaria")


def comparaMatriculas(request):
    if request.method == "POST":
        matricula = request.POST["matricula"]
        actualDay = datetime.today().strftime("%Y-%m-%d")
        gateway = (
            Gateway.objects.filter(
                Q(primeiraMatricula__contains=matricula)
                | Q(segundaMatricula__contains=matricula)
            )
            .filter(abandono="", dataHoraSaida="")
            .distinct()
        )
        dadosQADabs = (
            AbsMstr.objects.filter(abs_shp_date=actualDay)
            .filter(Q(abs_id__startswith="s") | Q(abs_id__startswith="p"))
            .filter((Q(abs_type="s")) | (Q(abs_type="p")))
            .filter(abs_shipfrom="3515")
            .values(
                "abs_id",
                "abs_shp_date",
                "abs_shp_time",
                "abs_qad01",
                "oid_abs_mstr",
                "abs_status",
                "abs_shipto",
                "abs_item",
                "abs_domain",
            )
        )
        for elem in gateway.all():
            elem.estado = "verde"
            elem.save()
        return redirect("shippers:tracking2")


def changeUserGroups(request):
    if request.method == "POST":
        user = User.objects.get(username=request.POST["username"])
        grupo = request.POST["paginas"]
        if User.objects.filter(
            username=request.POST["username"], groups__name="shippingPortaria"
        ):
            my_group = Group.objects.using("default").get(name="shippingPortaria")
            my_group.user_set.remove(user)
        if User.objects.filter(
            username=request.POST["username"], groups__name="shippingPortariaReadOnly"
        ):
            my_group = Group.objects.using("default").get(
                name="shippingPortariaReadOnly"
            )
            my_group.user_set.remove(user)
        if User.objects.filter(
            username=request.POST["username"], groups__name="shippingTracking"
        ):
            my_group = Group.objects.using("default").get(name="shippingTracking")
            my_group.user_set.remove(user)
        if User.objects.filter(
            username=request.POST["username"], groups__name="shippingSecurity"
        ):
            my_group = Group.objects.using("default").get(name="shippingSecurity")
            my_group.user_set.remove(user)
        if User.objects.filter(
            username=request.POST["username"], groups__name="shippingConfirmation"
        ):
            my_group = Group.objects.using("default").get(name="shippingConfirmation")
            my_group.user_set.remove(user)
        if grupo == "none":
            # message = 'User ' + user.username + ' perdeu acesso às páginas de Shipping.'
            # subject, from_email, to = 'Alteração em Receiving - Line Request - Configurations', 'noreply@visteon.com', [
            #     'aroque1@visteon.com']
            # msg = EmailMultiAlternatives(subject, message, from_email, to)
            # msg.attach_alternative(message, "text/html")
            # msg.send()
            return redirect("shippers:configurations")
        if grupo == "portaria":
            my_group = Group.objects.using("default").get(name="shippingPortaria")
            my_group.user_set.add(user)
        if grupo == "portariaReadOnly":
            my_group = Group.objects.using("default").get(
                name="shippingPortariaReadOnly"
            )
            my_group.user_set.add(user)
        if grupo == "tracking":
            my_group = Group.objects.using("default").get(name="shippingTracking")
            my_group.user_set.add(user)
        if grupo == "security":
            my_group = Group.objects.using("default").get(name="shippingSecurity")
            my_group.user_set.add(user)
        if grupo == "confirmation":
            my_group = Group.objects.using("default").get(name="shippingConfirmation")
            my_group.user_set.add(user)

        if grupo == "portaria/tracking":
            my_group = Group.objects.using("default").get(name="shippingPortaria")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingTracking")
            my_group.user_set.add(user)
        if grupo == "portaria/security":
            my_group = Group.objects.using("default").get(name="shippingPortaria")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingSecurity")
            my_group.user_set.add(user)
        if grupo == "portaria/confirmation":
            my_group = Group.objects.using("default").get(name="shippingPortaria")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingConfirmation")
            my_group.user_set.add(user)
        if grupo == "portariaReadOnly/tracking":
            my_group = Group.objects.using("default").get(
                name="shippingPortariaReadOnly"
            )
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingTracking")
            my_group.user_set.add(user)
        if grupo == "portariaReadOnly/security":
            my_group = Group.objects.using("default").get(
                name="shippingPortariaReadOnly"
            )
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingSecurity")
            my_group.user_set.add(user)
        if grupo == "portariaReadOnly/confirmation":
            my_group = Group.objects.using("default").get(
                name="shippingPortariaReadOnly"
            )
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingConfirmation")
            my_group.user_set.add(user)
        if grupo == "tracking/security":
            my_group = Group.objects.using("default").get(name="shippingTracking")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingSecurity")
            my_group.user_set.add(user)
        if grupo == "tracking/confirmation":
            my_group = Group.objects.using("default").get(name="shippingTracking")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingConfirmation")
            my_group.user_set.add(user)
        if grupo == "security/confirmation":
            my_group = Group.objects.using("default").get(name="shippingSecurity")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingConfirmation")
            my_group.user_set.add(user)

        if grupo == "portaria/tracking/security":
            my_group = Group.objects.using("default").get(name="shippingPortaria")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingTracking")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingSecurity")
            my_group.user_set.add(user)
        if grupo == "portaria/tracking/confirmation":
            my_group = Group.objects.using("default").get(name="shippingPortaria")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingTracking")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingConfirmation")
            my_group.user_set.add(user)
        if grupo == "portaria/security/confirmation":
            my_group = Group.objects.using("default").get(name="shippingPortaria")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingSecurity")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingConfirmation")
            my_group.user_set.add(user)
        if grupo == "portariaReadOnly/tracking/security":
            my_group = Group.objects.using("default").get(
                name="shippingPortariaReadOnly"
            )
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingTracking")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingSecurity")
            my_group.user_set.add(user)
        if grupo == "portariaReadOnly/tracking/confirmation":
            my_group = Group.objects.using("default").get(
                name="shippingPortariaReadOnly"
            )
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingTracking")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingConfirmation")
            my_group.user_set.add(user)
        if grupo == "portariaReadOnly/security/confirmation":
            my_group = Group.objects.using("default").get(
                name="shippingPortariaReadOnly"
            )
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingSecurity")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingConfirmation")
            my_group.user_set.add(user)
        if grupo == "tracking/security/confirmation":
            my_group = Group.objects.using("default").get(name="shippingTracking")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingSecurity")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingConfirmation")
            my_group.user_set.add(user)

        if grupo == "portaria/tracking/security/confirmation":
            my_group = Group.objects.using("default").get(name="shippingPortaria")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingTracking")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingSecurity")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingConfirmation")
            my_group.user_set.add(user)
        if grupo == "portariaReadOnly/tracking/security/confirmation":
            my_group = Group.objects.using("default").get(
                name="shippingPortariaReadOnly"
            )
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingTracking")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingSecurity")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="shippingConfirmation")
            my_group.user_set.add(user)
        # message = 'User ' + user.username + ' com páginas acessiveis - ' + grupo.replace("/", " , ")
        # subject, from_email, to = 'Alteração em Shipping - Configurations', 'noreply@visteon.com', [
        #     'aroque1@visteon.com']
        # msg = EmailMultiAlternatives(subject, message, from_email, to)
        # msg.attach_alternative(message, "text/html")
        # msg.send()
        return redirect("shippers:configurations")


def searchAllInfo(request):
    if request.method == "GET":
        resposta = []
        todos = GatewayInfoCondutor.objects.all()
        for elem in todos:
            row = {
                "condutor": elem.condutor.nome,
                "condutorID": elem.condutorID.nome,
                "contacto": elem.contacto.nome,
                "empresa": elem.empresa.nome,
            }
            resposta.append(row)
        return JsonResponse({"resposta": resposta})


def searchEmpresa(request):
    with timer():
        if request.method == "GET":
            empresa = request.GET["empresa"]
            resposta = []
            if GatewayInfoCondutor.objects.filter(empresa__nome=empresa).exists():
                elem = GatewayInfoCondutor.objects.filter(empresa__nome=empresa)
                for elem1 in elem.all():
                    row = {
                        "condutor": elem1.condutor.nome,
                        "condutorID": elem1.condutorID.nome,
                        "contacto": elem1.contacto.nome,
                        "empresa": elem1.empresa.nome,
                    }
                    resposta.append(row)
            return JsonResponse({"resposta": resposta})


def searchCondutor(request):
    with timer():
        if request.method == "GET":
            condutor = request.GET["condutor"]
            resposta = []
            if GatewayInfoCondutor.objects.filter(
                condutor__in=GatewayCondutor.objects.filter(nome=condutor)
            ).exists():
                elem = GatewayInfoCondutor.objects.get(
                    condutor=GatewayCondutor.objects.get(nome=condutor)
                )
                row = {
                    "condutor": elem.condutor.nome,
                    "condutorID": elem.condutorID.nome,
                    "contacto": elem.contacto.nome,
                    "empresa": elem.empresa.nome,
                }
                resposta.append(row)
            return JsonResponse({"resposta": resposta})


def searchCondutorID(request):
    with timer():
        if request.method == "GET":
            condutorID = request.GET["condutorID"]
            resposta = []
            if GatewayInfoCondutor.objects.filter(
                condutorID__in=GatewayCondutorID.objects.filter(nome=condutorID)
            ).exists():
                elem = GatewayInfoCondutor.objects.get(
                    condutorID=GatewayCondutorID.objects.get(nome=condutorID)
                )
                row = {
                    "condutor": elem.condutor.nome,
                    "condutorID": elem.condutorID.nome,
                    "contacto": elem.contacto.nome,
                    "empresa": elem.empresa.nome,
                }
                resposta.append(row)
            return JsonResponse({"resposta": resposta})


def searchContacto(request):
    with timer():
        if request.method == "GET":
            contacto = request.GET["contacto"]
            resposta = []
            if GatewayInfoCondutor.objects.filter(
                contacto__in=GatewayContactoCondutor.objects.filter(nome=contacto)
            ).exists():
                elem = GatewayInfoCondutor.objects.get(
                    contacto=GatewayContactoCondutor.objects.get(nome=contacto)
                )
                row = {
                    "condutor": elem.condutor.nome,
                    "condutorID": elem.contacto.nome,
                    "contacto": elem.contacto.nome,
                    "empresa": elem.empresa.nome,
                }
                resposta.append(row)
            return JsonResponse({"resposta": resposta})


def setDataHoraSaida(request):
    if request.method == "POST":
        id = request.POST["id"]
        elem = Gateway.objects.get(id=id)
        if elem.dataHoraEntrada != "":
            elem.dataHoraSaida = datetime.today().strftime("%Y-%m-%d %H:%M")
        elem.save()
        return redirect("shippers:portaria")


def setDataHoraEntrada(request):
    if request.method == "POST":
        id = request.POST["id"]
        elem = Gateway.objects.get(id=id)
        elem.dataHoraEntrada = datetime.today().strftime("%Y-%m-%d %H:%M")
        elem.save()
        return redirect("shippers:portaria")


def mudaEstadoFiltro(request):
    with timer():
        if request.method == "POST":
            posicao = request.POST["posicao"]
            estado = request.POST["estado"]

            if posicao == "entrada":
                if estado == "on":
                    request.session["entrada"] = "entrada"
                else:
                    del request.session["entrada"]
            #     botao.entrada = estado
            if posicao == "saida":
                if estado == "on":
                    request.session["saida"] = "saida"
                else:
                    del request.session["saida"]
            #     botao.saida = estado
            # botao.save()

            return redirect("shippers:portaria")


def downloadExcel(request):
    if request.method == "GET":
        elementos = Gateway.objects

        caminho = "C:/visteon/media/shippers/portaria"
        if os.path.exists(caminho):
            for entry in os.listdir(caminho):
                if os.path.isfile(os.path.join(caminho, entry)):
                    os.remove(caminho + "/" + entry)

        wbProduction = Workbook()
        sheetProduction = wbProduction.add_sheet("Sheet 1")

        row = 0
        col = 0
        sheetProduction.write(row, col, "Data/hora chegada")
        sheetProduction.write(row, col + 1, "Condutor")
        sheetProduction.write(row, col + 2, "ID Condutor")
        sheetProduction.write(row, col + 3, "Contacto")
        sheetProduction.write(row, col + 4, "Empresa")
        sheetProduction.write(row, col + 5, "1ª matricula")
        sheetProduction.write(row, col + 6, "2ª matricula")
        sheetProduction.write(row, col + 7, "Carga/descarga")
        sheetProduction.write(row, col + 8, "Doca")
        sheetProduction.write(row, col + 9, "Destino carga")
        sheetProduction.write(row, col + 10, "Tipo viatura")
        sheetProduction.write(row, col + 11, "Data/hora entrada")
        sheetProduction.write(row, col + 12, "Abandono")
        sheetProduction.write(row, col + 13, "Comentários entrada")
        sheetProduction.write(row, col + 14, "Data/hora saida")
        sheetProduction.write(row, col + 15, "Comentários saída")
        row += 1

        for elem in elementos.all():
            sheetProduction.write(row, col, elem.dataHoraChegada)
            sheetProduction.write(row, col + 1, elem.condutor)
            sheetProduction.write(row, col + 2, elem.ident)
            sheetProduction.write(row, col + 3, elem.contacto)
            sheetProduction.write(row, col + 4, elem.empresa)
            sheetProduction.write(row, col + 5, elem.primeiraMatricula)
            sheetProduction.write(row, col + 6, elem.segundaMatricula)
            sheetProduction.write(row, col + 7, elem.cargaDescarga)
            sheetProduction.write(row, col + 8, elem.doca)
            sheetProduction.write(row, col + 9, elem.destinoCarga)
            sheetProduction.write(row, col + 10, elem.tipoViatura)
            sheetProduction.write(row, col + 11, elem.dataHoraEntrada)
            sheetProduction.write(row, col + 12, elem.abandono)
            sheetProduction.write(row, col + 13, elem.comentEntrada)
            sheetProduction.write(row, col + 14, elem.dataHoraSaida)
            sheetProduction.write(row, col + 15, elem.comentSaida)
            row += 1
        wbProduction.save(
            "C:\\visteon\\media\\shippers\\portaria\\workbookPortaria.xls"
        )

        return redirect("shippers:portaria")


def uploadDataPortaria(request):
    if request.method == "POST":
        if request.FILES.get("ficheiro"):

            ficheiro = [request.FILES["ficheiro"]]

            workbook = openpyxl.load_workbook(ficheiro[0])
            worksheet = workbook["Sheet 1"]

            for element in worksheet:
                if element[0].value != None and element[1].value != "Condutor":
                    novoElemento = Gateway(
                        None,
                        element[0].value,
                        element[4].value,
                        element[1].value,
                        element[2].value,
                        element[3].value,
                        element[5].value,
                        element[6].value,
                        element[7].value,
                        element[8].value,
                        element[9].value,
                        element[10].value,
                        element[11].value,
                        "feitoEsaiu",
                        element[12].value,
                        element[13].value,
                        element[14].value,
                        element[15].value,
                    )
                    novoElemento.save()

        return redirect("shippers:portaria")


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)


def reportPortaria(request):
    if request.method == "POST":
        texto = request.POST["reportICDR"].replace("\n", "</br>")

        message = "<b>Report criado pelo User: " + request.user.username + "</b>"
        message += "</br></br>" + texto
        subject, from_email, to = (
            "Novo report na página Shippers - Portaria",
            "noreply@visteon.com",
            ["aroque1@visteon.com", "npires2@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()
        return redirect("shippers:portaria")


def reportTracking(request):
    if request.method == "POST":
        texto = request.POST["reportICDR"].replace("\n", "</br>")

        message = "<b>Report criado pelo User: " + request.user.username + "</b>"
        message += "</br></br>" + texto
        subject, from_email, to = (
            "Novo report na página Shippers - Tracking",
            "noreply@visteon.com",
            ["aroque1@visteon.com", "npires2@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()
        return redirect("shippers:tracking")


def reportSecurity(request):
    if request.method == "POST":
        texto = request.POST["reportICDR"].replace("\n", "</br>")

        message = "<b>Report criado pelo User: " + request.user.username + "</b>"
        message += "</br></br>" + texto
        subject, from_email, to = (
            "Novo report na página Shippers - Security",
            "noreply@visteon.com",
            ["aroque1@visteon.com", "npires2@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()
        return redirect("shippers:security")


def reportConfirmation(request):
    if request.method == "POST":
        texto = request.POST["reportICDR"].replace("\n", "</br>")

        message = "<b>Report criado pelo User: " + request.user.username + "</b>"
        message += "</br></br>" + texto
        subject, from_email, to = (
            "Novo report na página Shippers - Confirmation",
            "noreply@visteon.com",
            ["aroque1@visteon.com", "npires2@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()
        return redirect("shippers:shippersConfirmation")