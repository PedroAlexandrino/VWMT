import json
import os
import datetime

import numpy as np
import openpyxl
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMultiAlternatives
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q

from datetime import datetime, date, timedelta
from collections import Counter

from xlwt import Workbook

from qad_ee.models import *
from receiving.models import *


def tenda(request):
    ldDetWHOUT = LdDet.objects.filter(ld_site="3515", ld_loc="WHOUT").values(
        "ld_part", "ld_loc", "ld_qty_oh"
    )
    ldDetNotWHOUT = (
        LdDet.objects.filter(
            ld_site="3515", ld_part__in=ldDetWHOUT.values_list("ld_part")
        )
        .exclude(Q(ld_loc="WHOUT") | Q(ld_loc="QUALITY"))
        .values("ld_part", "ld_loc")
    )
    ptMstr = PtMstr.objects.filter(
        pt_part__in=ldDetWHOUT.values_list("ld_part"), pt_site="3515"
    ).values("pt_part", "pt_desc1", "pt_desc2")
    serMstrWHOUT = SerMstr.objects.filter(
        ser_part__in=ldDetWHOUT.values_list("ld_part"), ser_site="3515", ser_loc="WHOUT"
    ).values("ser_part")
    serMstrNotWHOUT = (
        SerMstr.objects.filter(
            ser_part__in=ldDetWHOUT.values_list("ld_part"), ser_site="3515"
        )
        .exclude(Q(ser_loc="WHOUT") | Q(ser_loc="QUALITY"))
        .values("ser_part", "ser_qty_avail")
    )

    elementos = []

    xxusrw = XxusrwWkfl.objects.filter(
        xxusrw_key6="KCB00602-AA", xxusrw_domain="3511010"
    ).values("xxusrw_decfld_1", "xxusrw_key4", "xxusrw_key6", "xxusrw_decfld_2")
    # woMstr = WoMstr.objects.filter(wo_part__in=xxusrw.values_list('xxusrw_key4'),
    #                                wo_due_date="2022-04-20").values(
    #     'wo_part', 'wo_qty_exp_complete')

    counterWHOUT = Counter()
    counterNotWHOUT = Counter()
    counterSerWHOUT = Counter()
    counterSerNotWHOUT = Counter()

    for ld in ldDetWHOUT:
        counterWHOUT[ld["ld_part"]] += ld["ld_qty_oh"]

    # for ld in ldDetNotWHOUT:
    #     counterNotWHOUT[ld['ld_part']] += ld['ld_qty_oh']

    for ser in serMstrWHOUT:
        counterSerWHOUT[ser["ser_part"]] += 1

    for ser in serMstrNotWHOUT:
        counterSerNotWHOUT[ser["ser_part"]] += 1
        counterNotWHOUT[ser["ser_part"]] += ser["ser_qty_avail"]

    for ld in ldDetWHOUT:
        for pt in ptMstr:
            if pt["pt_part"] == ld["ld_part"]:
                if len(pt["pt_desc1"]) == 24:
                    pt["pt_desc1"] = pt["pt_desc1"] + "" + pt["pt_desc2"]
                else:
                    pt["pt_desc1"] = pt["pt_desc1"] + " " + pt["pt_desc2"]
                if str(counterWHOUT[ld["ld_part"]]) == "0E-10":
                    counterWHOUT[ld["ld_part"]] = "0.0000000000"
                if not any(elem["itemNumber"] == ld["ld_part"] for elem in elementos):
                    row = {
                        "itemNumber": ld["ld_part"],
                        "descricao": pt["pt_desc1"],
                        "qtyOnHand": str(counterWHOUT[ld["ld_part"]])[:-11],
                        "serialsWHOUT": counterSerWHOUT[ld["ld_part"]],
                        "qtyOnHandNotWHOUT": 0,
                        "serialsNotWHOUT": counterSerNotWHOUT[ld["ld_part"]],
                        "unitCost": "-",
                        "min": "-",
                        "max": "-",
                        "consumptionValue": 0,
                        "consumptionValueDiaSeguinte": 0,
                        "consumptionValueDiaAposDiaSeguinte": 0,
                        "totalCost": "-",
                    }
                    elementos.append(row)
    for ldNotWHOUT in ldDetNotWHOUT:
        for elem in elementos:
            if elem["itemNumber"] == ldNotWHOUT["ld_part"]:
                elem["qtyOnHandNotWHOUT"] = str(counterNotWHOUT[ldNotWHOUT["ld_part"]])[
                    :-11
                ]
                if elem["qtyOnHandNotWHOUT"] == "":
                    elem["qtyOnHandNotWHOUT"] = "0"
                break

    # for xx in xxusrw:
    #     for wo in woMstr:
    #         if wo['wo_part'] == xx['xxusrw_key4']:
    #             for elem in elementos:
    #                 if elem['itemNumber'] == xx['xxusrw_key6']:
    #                     elem['contas'] += xx['xxusrw_key4'] + " " + str(xx['xxusrw_decfld_1']) + "*" + str(
    #                         wo['wo_qty_exp_complete'])
    #                     elem['consumptionValue'] += round(
    #                         float(xx['xxusrw_decfld_1']) * float(wo['wo_qty_exp_complete']), 2)
    #                     break

    return render(request, "tenda.html", {"elementos": elementos})


def uploadTendaCosts(request):
    if request.method == "GET":
        ldDetWHOUT = LdDet.objects.filter(ld_site="3515", ld_loc="WHOUT").values(
            "ld_part", "ld_loc", "ld_qty_oh"
        )
        ldDetNotWHOUT = (
            LdDet.objects.filter(
                ld_site="3515", ld_part__in=ldDetWHOUT.values_list("ld_part")
            )
            .exclude(Q(ld_loc="WHOUT") | Q(ld_loc="QUALITY"))
            .values("ld_part", "ld_loc")
        )
        ptMstr = PtMstr.objects.filter(
            pt_part__in=ldDetWHOUT.values_list("ld_part"), pt_site="3515"
        ).values("pt_part", "pt_desc1", "pt_desc2")
        serMstrWHOUT = SerMstr.objects.filter(
            ser_part__in=ldDetWHOUT.values_list("ld_part"),
            ser_site="3515",
            ser_loc="WHOUT",
        ).values("ser_part")
        serMstrNotWHOUT = (
            SerMstr.objects.filter(
                ser_part__in=ldDetWHOUT.values_list("ld_part"), ser_site="3515"
            )
            .exclude(Q(ser_loc="WHOUT") | Q(ser_loc="QUALITY"))
            .values("ser_part", "ser_qty_avail")
        )

        xx = []
        elementos = []

        partNumberList = ldDetWHOUT.values_list("ld_part").values("ld_part").distinct()

        for pn in partNumberList:
            if SctDet.objects.filter(
                sct_part=pn["ld_part"], sct_site="3515", sct_sim="Standard"
            ).exists():
                xx.append(
                    SctDet.objects.filter(
                        sct_part=pn["ld_part"], sct_site="3515", sct_sim="Standard"
                    ).values("sct_cst_tot", "sct_part")
                )
            # if XxusrwWkfl.objects.filter(xxusrw_key6=pn['ld_part'], xxusrw_domain="3511010").exists():
            #     xx.append(XxusrwWkfl.objects.filter(xxusrw_key6=pn['ld_part'], xxusrw_domain="3511010").values(
            #         'xxusrw_decfld_1',
            #         'xxusrw_key4',
            #         'xxusrw_key6',
            #         'xxusrw_decfld_2')[0])

        counterWHOUT = Counter()
        counterNotWHOUT = Counter()
        counterSerWHOUT = Counter()
        counterSerNotWHOUT = Counter()

        for ld in ldDetWHOUT:
            counterWHOUT[ld["ld_part"]] += ld["ld_qty_oh"]

        # for ld in ldDetNotWHOUT:
        #     counterNotWHOUT[ld['ld_part']] += ld['ld_qty_oh']

        for ser in serMstrWHOUT:
            counterSerWHOUT[ser["ser_part"]] += 1

        for ser in serMstrNotWHOUT:
            counterSerNotWHOUT[ser["ser_part"]] += 1
            counterNotWHOUT[ser["ser_part"]] += ser["ser_qty_avail"]

        for ld in ldDetWHOUT:
            for pt in ptMstr:
                if pt["pt_part"] == ld["ld_part"]:
                    if len(pt["pt_desc1"]) == 24:
                        pt["pt_desc1"] = pt["pt_desc1"] + "" + pt["pt_desc2"]
                    else:
                        pt["pt_desc1"] = pt["pt_desc1"] + " " + pt["pt_desc2"]
                    if not any(
                        elem["itemNumber"] == ld["ld_part"] for elem in elementos
                    ):
                        row = {
                            "itemNumber": ld["ld_part"],
                            "descricao": pt["pt_desc1"],
                            "qtyOnHand": str(counterWHOUT[ld["ld_part"]])[:-11],
                            "serialsWHOUT": counterSerWHOUT[ld["ld_part"]],
                            "qtyOnHandNotWHOUT": 0,
                            "serialsNotWHOUT": counterSerNotWHOUT[ld["ld_part"]],
                            "unitCost": "-",
                            "min": "-",
                            "max": "-",
                            "consumptionValue": 0,
                            "consumptionValueDiaSeguinte": 0,
                            "consumptionValueDiaAposDiaSeguinte": 0,
                            "totalCost": "-",
                        }
                        elementos.append(row)
        for ldNotWHOUT in ldDetNotWHOUT:
            for elem in elementos:
                if elem["itemNumber"] == ldNotWHOUT["ld_part"]:
                    elem["qtyOnHandNotWHOUT"] = str(
                        counterNotWHOUT[ldNotWHOUT["ld_part"]]
                    )[:-11]
                    if elem["qtyOnHandNotWHOUT"] == "":
                        elem["qtyOnHandNotWHOUT"] = "0"
                    break

        for elem in elementos:
            for elemXX in xx:
                for elemenXX in elemXX:
                    if elem["itemNumber"] == elemenXX["sct_part"]:
                        if elem["qtyOnHand"] == "":
                            elem["qtyOnHand"] = "0"
                        elem["unitCost"] = round(float(elemenXX["sct_cst_tot"]), 2)
                        elem["totalCost"] = round(
                            float(elem["qtyOnHand"]) * elem["unitCost"], 2
                        )
                        break

        return render(request, "tenda.html", {"elementos": elementos})


def updateTenda(request):
    if request.method == "GET":
        diaCorrente = date.today()
        diaSeguinte = date.today() + timedelta(days=1)
        diaAposDiaSeguinte = date.today() + timedelta(days=2)

        # quinta
        if diaCorrente.weekday() == 3:
            diaSeguinte = date.today() + timedelta(days=1)
            diaAposDiaSeguinte = date.today() + timedelta(days=4)
        # sexta
        if diaCorrente.weekday() == 4:
            diaSeguinte = date.today() + timedelta(days=3)
            diaAposDiaSeguinte = date.today() + timedelta(days=4)
        # sabado
        if diaCorrente.weekday() == 5:
            diaCorrente = date.today() + timedelta(days=2)
            diaSeguinte = date.today() + timedelta(days=3)
            diaAposDiaSeguinte = date.today() + timedelta(days=4)
        # domingo
        if diaCorrente.weekday() == 6:
            diaCorrente = date.today() + timedelta(days=1)
            diaSeguinte = date.today() + timedelta(days=2)
            diaAposDiaSeguinte = date.today() + timedelta(days=3)

        ldDetWHOUT = LdDet.objects.filter(ld_site="3515", ld_loc="WHOUT").values(
            "ld_part", "ld_loc", "ld_qty_oh"
        )
        ldDetNotWHOUT = (
            LdDet.objects.filter(
                ld_site="3515", ld_part__in=ldDetWHOUT.values_list("ld_part")
            )
            .exclude(Q(ld_loc="WHOUT") | Q(ld_loc="QUALITY"))
            .values("ld_part", "ld_loc")
        )
        ptMstr = PtMstr.objects.filter(
            pt_part__in=ldDetWHOUT.values_list("ld_part"), pt_site="3515"
        ).values("pt_part", "pt_desc1", "pt_desc2")
        serMstrWHOUT = SerMstr.objects.filter(
            ser_part__in=ldDetWHOUT.values_list("ld_part"),
            ser_site="3515",
            ser_loc="WHOUT",
        ).values("ser_part")
        serMstrNotWHOUT = (
            SerMstr.objects.filter(
                ser_part__in=ldDetWHOUT.values_list("ld_part"), ser_site="3515"
            )
            .exclude(Q(ser_loc="WHOUT") | Q(ser_loc="QUALITY"))
            .values("ser_part", "ser_qty_avail")
        )
        xxusrw = XxusrwWkfl.objects.filter(
            xxusrw_key6__in=ldDetWHOUT.values_list("ld_part"), xxusrw_domain="3511010"
        ).values("xxusrw_decfld_1", "xxusrw_key4", "xxusrw_key6", "xxusrw_decfld_2")
        woMstr = WoMstr.objects.filter(
            wo_part__in=xxusrw.values_list("xxusrw_key4"),
            wo_due_date=diaCorrente.strftime("%Y-%m-%d"),
        ).values("wo_part", "wo_qty_exp_complete")
        woMstrDiaSeguinte = WoMstr.objects.filter(
            wo_part__in=xxusrw.values_list("xxusrw_key4"),
            wo_due_date=diaSeguinte.strftime("%Y-%m-%d"),
        ).values("wo_part", "wo_qty_exp_complete")
        woMstrDiaAposDiaSeguinte = WoMstr.objects.filter(
            wo_part__in=xxusrw.values_list("xxusrw_key4"),
            wo_due_date=diaAposDiaSeguinte.strftime("%Y-%m-%d"),
        ).values("wo_part", "wo_qty_exp_complete")

        elementos = []
        xxList = []

        partNumberList = ldDetWHOUT.values_list("ld_part").values("ld_part").distinct()

        for pn in partNumberList:
            if SctDet.objects.filter(
                sct_part=pn["ld_part"], sct_site="3515", sct_sim="Standard"
            ).exists():
                xxList.append(
                    SctDet.objects.filter(
                        sct_part=pn["ld_part"], sct_site="3515", sct_sim="Standard"
                    ).values("sct_cst_tot", "sct_part")
                )

        counterWHOUT = Counter()
        counterNotWHOUT = Counter()
        counterSerWHOUT = Counter()
        counterSerNotWHOUT = Counter()

        for ld in ldDetWHOUT:
            counterWHOUT[ld["ld_part"]] += ld["ld_qty_oh"]

        for ser in serMstrWHOUT:
            counterSerWHOUT[ser["ser_part"]] += 1

        for ser in serMstrNotWHOUT:
            counterSerNotWHOUT[ser["ser_part"]] += 1
            counterNotWHOUT[ser["ser_part"]] += ser["ser_qty_avail"]

        for ld in ldDetWHOUT:
            for pt in ptMstr:
                if pt["pt_part"] == ld["ld_part"]:
                    if len(pt["pt_desc1"]) == 24:
                        pt["pt_desc1"] = pt["pt_desc1"] + "" + pt["pt_desc2"]
                    else:
                        pt["pt_desc1"] = pt["pt_desc1"] + " " + pt["pt_desc2"]
                    if not any(
                        elem["itemNumber"] == ld["ld_part"] for elem in elementos
                    ):
                        row = {
                            "diaAtual": diaCorrente,
                            "diaSeguinte": diaSeguinte,
                            "diaAposDiaSeguinte": diaAposDiaSeguinte,
                            "itemNumber": ld["ld_part"],
                            "descricao": pt["pt_desc1"],
                            "qtyOnHand": str(counterWHOUT[ld["ld_part"]])[:-11],
                            "serialsWHOUT": counterSerWHOUT[ld["ld_part"]],
                            "qtyOnHandNotWHOUT": 0,
                            "serialsNotWHOUT": counterSerNotWHOUT[ld["ld_part"]],
                            "unitCost": "-",
                            "min": "-",
                            "max": "-",
                            "consumptionValue": 0,
                            "consumptionValueDiaSeguinte": 0,
                            "consumptionValueDiaAposDiaSeguinte": 0,
                            "totalCost": "-",
                        }
                        elementos.append(row)
        for ldNotWHOUT in ldDetNotWHOUT:
            for elem in elementos:
                if elem["itemNumber"] == ldNotWHOUT["ld_part"]:
                    elem["qtyOnHandNotWHOUT"] = str(
                        counterNotWHOUT[ldNotWHOUT["ld_part"]]
                    )[:-11]
                    if elem["qtyOnHandNotWHOUT"] == "":
                        elem["qtyOnHandNotWHOUT"] = "0"
                    break

        for xx in xxusrw:
            for wo in woMstr:
                if wo["wo_part"] == xx["xxusrw_key4"]:
                    for elem in elementos:
                        if elem["itemNumber"] == xx["xxusrw_key6"]:
                            elem["consumptionValue"] += round(
                                float(xx["xxusrw_decfld_1"])
                                * float(wo["wo_qty_exp_complete"]),
                                2,
                            )
                            break
            for woDiaSeguinte in woMstrDiaSeguinte:
                if woDiaSeguinte["wo_part"] == xx["xxusrw_key4"]:
                    for elem in elementos:
                        if elem["itemNumber"] == xx["xxusrw_key6"]:
                            elem["consumptionValueDiaSeguinte"] += round(
                                float(xx["xxusrw_decfld_1"])
                                * float(woDiaSeguinte["wo_qty_exp_complete"]),
                                2,
                            )
                            break
            for woDiaAposDiaSeguinte in woMstrDiaAposDiaSeguinte:
                if woDiaAposDiaSeguinte["wo_part"] == xx["xxusrw_key4"]:
                    for elem in elementos:
                        if elem["itemNumber"] == xx["xxusrw_key6"]:
                            elem["consumptionValueDiaAposDiaSeguinte"] += round(
                                float(xx["xxusrw_decfld_1"])
                                * float(woDiaAposDiaSeguinte["wo_qty_exp_complete"]),
                                2,
                            )
                            break
        for elem in elementos:
            for elemXX in xxList:
                for elemenXX in elemXX:
                    if elem["itemNumber"] == elemenXX["sct_part"]:
                        if elem["qtyOnHand"] == "":
                            elem["qtyOnHand"] = "0"
                        elem["unitCost"] = round(float(elemenXX["sct_cst_tot"]), 2)
                        elem["totalCost"] = round(
                            float(elem["qtyOnHand"]) * elem["unitCost"], 2
                        )
                        break
        return render(request, "tenda.html", {"elementos": elementos})


def icdr(request):
    # UserICDR.objects.all().delete()
    # workbook = openpyxl.load_workbook(
    #     "//PAVPD002/E_Proj/sharedir/MP&L/Warehouse/PWMS/Receiving/ICDR/Copy of Copy of Copy of ICDR.xlsx")
    # worksheet = workbook['Users']
    #
    # for element in worksheet:
    #     if element[0].value != "":
    #         novoElemento = UserICDR(
    #             None,
    #             element[3].value,
    #             element[0].value,
    #             element[1].value,
    #             element[2].value
    #         )
    #         novoElemento.save()

    ultimoElemento = ICDRultimoValor.objects.first()
    motivos = ICDRmotivo.objects
    utilizadoresICDR = UserICDR.objects
    listaICDR = ICDR.objects
    filtroDesativado = request.session.get("filtroDesativado")
    tipo1 = request.user.groups.filter(name="ICDR - tipo1").exists()
    tipo2 = request.user.groups.filter(name="ICDR - tipo2").exists()
    tipo3 = request.user.groups.filter(name="ICDR - tipo3").exists()
    tipo1tipo2tipo3 = tipo1 and tipo2 and tipo3
    tipo1tipo2 = tipo1 and tipo2
    tipo1tipo3 = tipo1 and tipo3
    tipo2tipo3 = tipo2 and tipo3
    return render(
        request,
        "icdr.html",
        {
            "ultimoElemento": ultimoElemento,
            "motivos": motivos,
            "utilizadoresICDR": utilizadoresICDR,
            "listaICDR": listaICDR,
            "tipo1": tipo1,
            "tipo2": tipo2,
            "tipo3": tipo3,
            "tipo1tipo2": tipo1tipo2,
            "tipo2tipo3": tipo2tipo3,
            "tipo1tipo3": tipo1tipo3,
            "tipo1tipo2tipo3": tipo1tipo2tipo3,
            "filtroDesativado": filtroDesativado,
        },
    )


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="receivingLINES").exists())
def lineRequest(request):
    lineRequestProcessing = LineRequestProcessing.objects
    lineRequestFinished = LineRequestFinished.objects
    linhas = Line.objects
    justificacoes = Justification.objects
    return render(
        request,
        "lineRequest.html",
        {
            "lineRequestFinished": lineRequestFinished,
            "lineRequestProcessing": lineRequestProcessing,
            "linhas": linhas,
            "justificacoes": justificacoes,
        },
    )


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="coordReceiving").exists())
def configurations(request):
    linhas = Line.objects
    justificacoes = Justification.objects
    # users = User.objects.filter(groups__name__in=['receivingLINES', 'receivingMNFG', 'receivingTPM']).distinct()
    users = User.objects
    return render(
        request,
        "configurations.html",
        {"linhas": linhas, "justificacoes": justificacoes, "users": users},
    )


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="coordReceiving").exists())
def configurationsTPM(request):
    posicao1 = ReceivingPosicao1Items.objects
    posicao2 = ReceivingPosicao2Items.objects
    posicao3 = ReceivingPosicao3Items.objects
    posicao4 = ReceivingPosicao4Items.objects
    posicao5 = ReceivingPosicao5Items.objects
    posicao6 = ReceivingPosicao6Items.objects
    posicao7 = ReceivingPosicao7Items.objects
    posicao8 = ReceivingPosicao8Items.objects
    tipoSubItems = ReceivingSubItemsTipo.objects
    subItems = ReceivingSubItems.objects
    users = User.objects
    habilitados = HabilitarQuadrados.objects
    tempos = DefinirTempos.objects
    return render(
        request,
        "configurationsTPM.html",
        {
            "posicao1": posicao1,
            "posicao2": posicao2,
            "posicao3": posicao3,
            "posicao4": posicao4,
            "posicao5": posicao5,
            "posicao6": posicao6,
            "posicao7": posicao7,
            "posicao8": posicao8,
            "subItems": subItems,
            "habilitados": habilitados,
            "tempos": tempos,
            "users": users,
            "tipoSubItems": tipoSubItems,
        },
    )


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="receivingMNFG").exists())
def mnfgSupply(request):
    taskBrowse = TaskBrowse.objects
    data = LastUpdate.objects
    areaA = AreaA.objects
    areaB = AreaB.objects
    kardex = Kardex.objects

    dia = date.today() - timedelta(days=10)
    dadosQAD = WtskMstr.objects.filter(
        wtsk_create_date__gt=dia.strftime("%Y-%m-%d")
    ).exclude(wtsk_to_loc="kardex")
    wevDetFilterFA = WevdDet.objects.filter(
        wevd_create_date__gt=dia.strftime("%Y-%m-%d"),
        wevd_loc_to__startswith="F",
        wevd_status="PENDING",
        wevd_line="Repl02",
        wevd_domain="3511010",
    ).values("wevd_event_id", "wevd_from_part", "wevd_qty_remain", "wevd_create_date")

    wevDetFilterBP = WevdDet.objects.filter(
        wevd_create_date__gt=dia.strftime("%Y-%m-%d"),
        wevd_loc_to__startswith="S",
        wevd_status="PENDING",
        wevd_line="Repl02",
        wevd_domain="3511010",
    ).values("wevd_event_id", "wevd_from_part", "wevd_qty_remain", "wevd_create_date")

    wevMstrFA = WevMstr.objects.filter(
        wev_create_date__gt=dia.strftime("%Y-%m-%d"),
        wev_event_id__in=wevDetFilterFA.values_list("wevd_event_id"),
    ).values("wev_event_id", "wev_create_time")

    wevMstrBP = WevMstr.objects.filter(
        wev_create_date__gt=dia.strftime("%Y-%m-%d"),
        wev_event_id__in=wevDetFilterBP.values_list("wevd_event_id"),
    ).values("wev_event_id", "wev_create_time")

    elementosFA = []
    elementosBP = []
    for mstr in wevMstrFA:
        for det in wevDetFilterFA:
            if mstr["wev_event_id"] == det["wevd_event_id"]:
                row = {
                    "item": det["wevd_from_part"],
                    "qtyRemaining": str(det["wevd_qty_remain"])[:-11],
                    "date": str(det["wevd_create_date"])[:-9],
                    "time": mstr["wev_create_time"],
                }
                elementosFA.append(row)
                break
    for mstr in wevMstrBP:
        for det in wevDetFilterBP:
            if mstr["wev_event_id"] == det["wevd_event_id"]:
                row = {
                    "item": det["wevd_from_part"],
                    "qtyRemaining": str(det["wevd_qty_remain"])[:-11],
                    "date": str(det["wevd_create_date"])[:-9],
                    "time": mstr["wev_create_time"],
                }
                elementosBP.append(row)
                break
    return render(
        request,
        "mNFGSupply.html",
        {
            "taskBrowse": taskBrowse,
            "data": data,
            "areaA": areaA,
            "areaB": areaB,
            "kardex": kardex,
            "dadosQAD": dadosQAD,
            "elementosFA": elementosFA,
            "elementosBP": elementosBP,
        },
    )


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="receivingMNFG").exists())
def faSupply(request):
    taskBrowse = TaskBrowse.objects
    areaB = AreaB.objects
    data = LastUpdate.objects
    dia = date.today() - timedelta(days=10)
    dadosQAD = WtskMstr.objects.filter(
        wtsk_create_date__gt=dia.strftime("%Y-%m-%d")
    ).exclude(wtsk_to_loc="kardex")

    return render(
        request,
        "fASupply.html",
        {"taskBrowse": taskBrowse, "data": data, "areaB": areaB, "dadosQAD": dadosQAD},
    )


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="receivingMNFG").exists())
def bpDropinSupply(request):
    taskBrowse = TaskBrowse.objects
    data = LastUpdate.objects
    areaA = AreaA.objects
    dia = date.today() - timedelta(days=10)
    dadosQAD = WtskMstr.objects.filter(
        wtsk_create_date__gt=dia.strftime("%Y-%m-%d")
    ).exclude(wtsk_to_loc="kardex")
    return render(
        request,
        "bPDropinSupply.html",
        {"taskBrowse": taskBrowse, "data": data, "areaA": areaA, "dadosQAD": dadosQAD},
    )


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="receivingMNFG").exists())
def bpSMDSupply(request):
    taskBrowse = TaskBrowse.objects
    data = LastUpdate.objects
    kardex = Kardex.objects
    dia = date.today() - timedelta(days=10)
    dadosQAD = WtskMstr.objects.filter(
        wtsk_create_date__gt=dia.strftime("%Y-%m-%d")
    ).exclude(wtsk_to_loc="kardex")
    return render(
        request,
        "bPSMDSupply.html",
        {
            "taskBrowse": taskBrowse,
            "data": data,
            "kardex": kardex,
            "dadosQAD": dadosQAD,
        },
    )


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="admin").exists())
def errorLog(request):
    return render(request, "errorLog.html")


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="admin").exists())
def pending(request):
    dia = date.today() - timedelta(days=10)

    wevDetFilterFA = WevdDet.objects.filter(
        wevd_create_date__gt=dia.strftime("%Y-%m-%d"),
        wevd_loc_to__startswith="F",
        wevd_status="PENDING",
        wevd_line="Repl02",
        wevd_domain="3511010",
    ).values(
        "wevd_event_id",
        "wevd_ev_sub_id",
        "wevd_from_part",
        "wevd_loc_to",
        "wevd_qty_req",
        "wevd_qty_remain",
        "wevd_create_date",
    )

    wevDetFilterBP = WevdDet.objects.filter(
        wevd_create_date__gt=dia.strftime("%Y-%m-%d"),
        wevd_loc_to__startswith="S",
        wevd_status="PENDING",
        wevd_line="Repl02",
        wevd_domain="3511010",
    ).values(
        "wevd_event_id",
        "wevd_ev_sub_id",
        "wevd_from_part",
        "wevd_loc_to",
        "wevd_qty_req",
        "wevd_qty_remain",
        "wevd_create_date",
    )

    wevMstrFA = WevMstr.objects.filter(
        wev_create_date__gt=dia.strftime("%Y-%m-%d"),
        wev_event_id__in=wevDetFilterFA.values_list("wevd_event_id"),
    ).values("wev_event_id", "wev_create_time")

    wevMstrBP = WevMstr.objects.filter(
        wev_create_date__gt=dia.strftime("%Y-%m-%d"),
        wev_event_id__in=wevDetFilterBP.values_list("wevd_event_id"),
    ).values("wev_event_id", "wev_create_time")

    data = LastUpdate.objects

    elementosFA = []
    elementosBP = []
    for mstr in wevMstrFA:
        for det in wevDetFilterFA:
            if mstr["wev_event_id"] == det["wevd_event_id"]:
                row = {
                    "id": det["wevd_event_id"],
                    "subID": det["wevd_ev_sub_id"],
                    "item": det["wevd_from_part"],
                    "locTo": det["wevd_loc_to"],
                    "qtyRequired": str(det["wevd_qty_req"])[:-11],
                    "qtyRemaining": str(det["wevd_qty_remain"])[:-11],
                    "date": str(det["wevd_create_date"])[:-9],
                    "time": mstr["wev_create_time"],
                }
                elementosFA.append(row)
                break
    for mstr in wevMstrBP:
        for det in wevDetFilterBP:
            if mstr["wev_event_id"] == det["wevd_event_id"]:
                row = {
                    "id": det["wevd_event_id"],
                    "subID": det["wevd_ev_sub_id"],
                    "item": det["wevd_from_part"],
                    "locTo": det["wevd_loc_to"],
                    "qtyRequired": str(det["wevd_qty_req"])[:-11],
                    "qtyRemaining": str(det["wevd_qty_remain"])[:-11],
                    "date": str(det["wevd_create_date"])[:-9],
                    "time": mstr["wev_create_time"],
                }
                elementosBP.append(row)
                break

    return render(
        request,
        "pending.html",
        {"data": data, "elementosFA": elementosFA, "elementosBP": elementosBP},
    )


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="receivingTPM").exists())
def tpm(request):
    posicao1 = ReceivingPosicao1Items.objects
    posicao2 = ReceivingPosicao2Items.objects
    posicao3 = ReceivingPosicao3Items.objects
    posicao4 = ReceivingPosicao4Items.objects
    posicao5 = ReceivingPosicao5Items.objects
    posicao6 = ReceivingPosicao6Items.objects
    posicao7 = ReceivingPosicao7Items.objects
    posicao8 = ReceivingPosicao8Items.objects
    tipoSubItems = ReceivingSubItemsTipo.objects
    subItems = ReceivingSubItems.objects
    habilitados = HabilitarQuadrados.objects
    tempos = DefinirTempos.objects
    return render(
        request,
        "tpm.html",
        {
            "posicao1": posicao1,
            "posicao2": posicao2,
            "posicao3": posicao3,
            "posicao4": posicao4,
            "posicao5": posicao5,
            "posicao6": posicao6,
            "posicao7": posicao7,
            "posicao8": posicao8,
            "subItems": subItems,
            "habilitados": habilitados,
            "tempos": tempos,
            "tipoSubItems": tipoSubItems,
        },
    )


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="admin").exists())
def operationAnalyse(request):
    return render(request, "operationAnalyse.html")


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="coordReceiving").exists())
def configurationMNFG(request):
    areaA = AreaA.objects
    areaB = AreaB.objects
    kardex = Kardex.objects
    data = LastUpdate.objects
    return render(
        request,
        "configurationsMNFG.html",
        {"areaA": areaA, "areaB": areaB, "kardex": kardex, "data": data},
    )


@login_required()
@user_passes_test(lambda u: u.groups.filter(name="admin").exists())
def configurationsICDR(request):
    users = User.objects
    utilizadoresICDR = UserICDR.objects
    triggers = TriggerEnvioEmailsICDR.objects
    listasUsers = ListaUsersICDR.objects
    return render(
        request,
        "configurationsICDR.html",
        {
            "users": users,
            "utilizadoresICDR": utilizadoresICDR,
            "triggers": triggers,
            "listasUsers": listasUsers,
        },
    )


def addRequest(request):
    if request.method == "POST":
        partNumber = request.POST["partNumber"]
        horaPedido = request.POST["horaPedidoUsar"]
        requisitante = request.POST["requisitante"]
        justification = request.POST["justification"]
        comentario = request.POST["comentario"]
        receiver = request.POST["receiver"]

        if request.POST["lineSelect"]:
            line = request.POST["lineSelect"]
        if request.POST["lineInput"]:
            line = request.POST["lineInput"]

        if "_pending" in request.POST:
            novoRequest = LineRequestProcessing(
                None,
                horaPedido,
                partNumber,
                line,
                requisitante,
                receiver,
                justification,
                comentario,
            )
            novoRequest.save()
            return redirect("receiving:lineRequest")

        if "_finished" in request.POST:
            novoRequest = LineRequestFinished(
                None,
                horaPedido,
                partNumber,
                line,
                requisitante,
                receiver,
                justification,
                comentario,
            )
            novoRequest.save()
            return redirect("receiving:lineRequest")


def updatePending(request):
    if request.method == "POST":
        newPartNumber = request.POST["newPartNumberPending"]
        newLine = request.POST["newLinePending"]
        newRequisitante = request.POST["newRequirePending"]
        newReceiver = request.POST["newReceiverPending"]
        newJustification = request.POST["newJustificationPending"]
        newComentario = request.POST["newCommentPending"]

        oldPartNumber = request.POST["partNumberPendingVal"]
        partNumber = request.POST["partNumberPendingVal"]
        horaPedido = request.POST["horaPedidoPendingVal"]
        line = request.POST["linePendingVal"]
        requisitante = request.POST["requirePendingVal"]
        receiver = request.POST["receiverPendingVal"]
        justification = request.POST["justificationPendingVal"]
        comentario = request.POST["commentPendingVal"]

        if newPartNumber != "":
            partNumber = newPartNumber
        if newLine != "":
            line = newLine
        if newRequisitante != "":
            requisitante = newRequisitante
        if newReceiver != "":
            receiver = newReceiver
        if newJustification != "":
            justification = newJustification
        if newComentario != "":
            comentario = newComentario

        if "_deletePending" in request.POST:
            oldLine = LineRequestProcessing.objects.get(
                horaPedido=horaPedido, partNumber=oldPartNumber
            )
            oldLine.delete()
            return redirect("receiving:lineRequest")

        if "_pending" in request.POST:
            oldLine = LineRequestProcessing.objects.get(
                horaPedido=horaPedido, partNumber=oldPartNumber
            )
            oldLine.delete()
            novoRequest = LineRequestProcessing(
                None,
                horaPedido,
                partNumber,
                line,
                requisitante,
                receiver,
                justification,
                comentario,
            )
            novoRequest.save()
            return redirect("receiving:lineRequest")

        if justification == "":
            lineRequestProcessing = LineRequestProcessing.objects
            lineRequestFinished = LineRequestFinished.objects
            linhas = Line.objects
            justificacoes = Justification.objects
            return render(
                request,
                "lineRequest.html",
                {
                    "lineRequestFinished": lineRequestFinished,
                    "lineRequestProcessing": lineRequestProcessing,
                    "linhas": linhas,
                    "justificacoes": justificacoes,
                    "alert": "Not succeed! To proceed to finish need Justification",
                },
            )

        if "_finished" in request.POST:
            oldLine = LineRequestProcessing.objects.get(
                horaPedido=horaPedido,
                partNumber=partNumber,
                linha=line,
                receiver=receiver,
            )
            oldLine.delete()
            novoRequest = LineRequestFinished(
                None,
                horaPedido,
                partNumber,
                line,
                requisitante,
                receiver,
                justification,
                comentario,
            )
        novoRequest.save()
        return redirect("receiving:lineRequest")

    return redirect("receiving:lineRequest")


def createLine(request):
    if request.method == "POST":
        try:
            linha = request.POST["newLine"]
            linha = Line.objects.get(linha=linha)
        except ObjectDoesNotExist:
            novaLinha = Line()
            novaLinha.linha = request.POST["newLine"]
            novaLinha.save()

            message = "Adicionada linha " + novaLinha.linha
            subject, from_email, to = (
                "Alteração em Receiving - Line Request - Configurations",
                "noreply@visteon.com",
                ["aroque1@visteon.com"],
            )
            msg = EmailMultiAlternatives(subject, message, from_email, to)
            msg.attach_alternative(message, "text/html")
            msg.send()

            return redirect("receiving:configurations")
    linhas = Line.objects
    justificacoes = Justification.objects
    return render(
        request,
        "configurations.html",
        {
            "linhas": linhas,
            "justificacoes": justificacoes,
            "erro": "Line already exists",
        },
    )


def createJustification(request):
    if request.method == "POST":
        try:
            justificacao = request.POST["newJustification"]
            justificacao = Justification.objects.get(justificacao=justificacao)
        except ObjectDoesNotExist:
            novaJustificacao = Justification()
            novaJustificacao.justificacao = request.POST["newJustification"]
            novaJustificacao.save()

            message = "Adicionada justificação - " + novaJustificacao.justificacao
            subject, from_email, to = (
                "Alteração em Receiving - Line Request - Configurations",
                "noreply@visteon.com",
                ["aroque1@visteon.com"],
            )
            msg = EmailMultiAlternatives(subject, message, from_email, to)
            msg.attach_alternative(message, "text/html")
            msg.send()
            return redirect("receiving:configurations")
    linhas = Line.objects
    justificacoes = Justification.objects
    return render(
        request,
        "configurations.html",
        {
            "linhas": linhas,
            "justificacoes": justificacoes,
            "erro": "Justification already exists",
        },
    )


def deleteLine(request):
    if request.method == "POST":
        linha = request.POST["nome2"]

        nome = Line.objects.get(linha=linha)

        message = "Eliminada linha " + nome.linha
        subject, from_email, to = (
            "Alteração em Receiving - Line Request - Configurations",
            "noreply@visteon.com",
            ["aroque1@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()

        nome.delete()
        return redirect("receiving:configurations")


def deleteJustification(request):
    if request.method == "POST":
        justificacao = request.POST["nome3"]

        nome = Justification.objects.get(justificacao=justificacao)

        message = "Eliminada justificação - " + nome.justificacao
        subject, from_email, to = (
            "Alteração em Receiving - Line Request - Configurations",
            "noreply@visteon.com",
            ["aroque1@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()

        nome.delete()
        return redirect("receiving:configurations")


def uploadTaskBrowse(request):
    if request.method == "POST":

        # TaskBrowse.objects.all().delete()
        # workbook = openpyxl.load_workbook("//PAVPD002/E_Proj/sharedir/MP&L/Warehouse/PWMS/Receiving/Task Browse.xlsx")
        # worksheet = workbook['Data']
        #
        # for element in worksheet:
        #     if element[23].value != "KARDEX" and element[0].value != "Task ID":
        #         novoElemento = TaskBrowse(
        #             None,
        #             element[0].value,
        #             element[3].value,
        #             element[5].value,
        #             element[13].value,
        #             element[18].value,
        #             element[23].value,
        #             element[39].value,
        #             element[40].value
        #         )
        #         novoElemento.save()
        #
        # worksheet = workbook['Info']
        diaCorrente = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        oldLastUpdate = LastUpdate.objects.get()
        novaData = LastUpdate(
            None,
            diaCorrente,
            oldLastUpdate.redHour,
            oldLastUpdate.yellowHour,
            oldLastUpdate.lastUpdateRed,
        )
        novaData.save()
        oldLastUpdate.delete()

        if "_updateFA" in request.POST:
            return redirect("receiving:faSupply")
        elif "_updateSMD" in request.POST:
            return redirect("receiving:bpSMDSupply")
        elif "_updateDropin" in request.POST:
            return redirect("receiving:bpDropinSupply")
        elif "_updatePending" in request.POST:
            return redirect("receiving:pending")
        else:
            return redirect("receiving:mnfgSupply")


# def getTaskBrowse(request):
#     if request.method == 'GET':
#         TaskBrowse.objects.all().delete()
#         LastUpdate.objects.all().delete()
#         workbook = openpyxl.load_workbook("//PAVPD002/E_Proj/sharedir/MP&L/Warehouse/PWMS/Receiving/Task Browse.xlsx")
#         worksheet = workbook['Data']
#
#         for element in worksheet:
#             if element[23].value != "KARDEX" and element[0].value != "Task ID":
#                 novoElemento = TaskBrowse(
#                     None,
#                     element[0].value,
#                     element[3].value,
#                     element[5].value,
#                     element[13].value,
#                     element[18].value,
#                     element[23].value,
#                     element[39].value,
#                     element[40].value
#                 )
#                 novoElemento.save()
#
#         worksheet = workbook['Info']
#         novaData = LastUpdate(
#             None,
#             worksheet["B3"].value
#         )
#         novaData.save()
#
#         return redirect('receiving:faSupply')


def createAreaA(request):
    if request.method == "POST":
        try:
            newAreaA = request.POST["newAreaA"]
            newAreaA = AreaA.objects.get(storageZone=newAreaA)
        except ObjectDoesNotExist:
            novaAreaA = AreaA()
            novaAreaA.storageZone = request.POST["newAreaA"]
            novaAreaA.save()

            message = (
                "<b>BP Dropin Supply </b></br>Adicionado " + request.POST["newAreaA"]
            )
            subject, from_email, to = (
                "Alteração em Receiving - MNFG Supply - Configurations",
                "noreply@visteon.com",
                ["aroque1@visteon.com"],
            )
            msg = EmailMultiAlternatives(subject, message, from_email, to)
            msg.attach_alternative(message, "text/html")
            msg.send()
            return redirect("receiving:configurationMNFG")
    return redirect("receiving:configurationMNFG")


def createAreaB(request):
    if request.method == "POST":
        try:
            newAreaB = request.POST["newAreaB"]
            newAreaB = AreaB.objects.get(storageZone=newAreaB)
        except ObjectDoesNotExist:
            novaAreaB = AreaB()
            novaAreaB.storageZone = request.POST["newAreaB"]
            novaAreaB.save()

            message = "<b>FA Supply </b></br>Adicionado " + request.POST["newAreaB"]
            subject, from_email, to = (
                "Alteração em Receiving - MNFG Supply - Configurations",
                "noreply@visteon.com",
                ["aroque1@visteon.com"],
            )
            msg = EmailMultiAlternatives(subject, message, from_email, to)
            msg.attach_alternative(message, "text/html")
            msg.send()

            return redirect("receiving:configurationMNFG")
    return redirect("receiving:configurationMNFG")


def createKardex(request):
    if request.method == "POST":
        try:
            newKardex = request.POST["newKardex"]
            newKardex = Kardex.objects.get(storageZone=newKardex)
        except ObjectDoesNotExist:
            novaKardex = Kardex()
            novaKardex.storageZone = request.POST["newKardex"]
            novaKardex.save()

            message = (
                "<b>BP SMD Supply </b></br>Adicionado " + request.POST["newKardex"]
            )
            subject, from_email, to = (
                "Alteração em Receiving - MNFG Supply - Configurations",
                "noreply@visteon.com",
                ["aroque1@visteon.com"],
            )
            msg = EmailMultiAlternatives(subject, message, from_email, to)
            msg.attach_alternative(message, "text/html")
            msg.send()

            return redirect("receiving:configurationMNFG")
    return redirect("receiving:configurationMNFG")


def deleteAreaA(request):
    if request.method == "POST":
        storageZone = request.POST["nomeAreaA"]

        nome = AreaA.objects.get(storageZone=storageZone)

        message = "<b>BP Dropin Supply </b></br>Removido " + nome.storageZone
        subject, from_email, to = (
            "Alteração em Receiving - MNFG Supply - Configurations",
            "noreply@visteon.com",
            ["aroque1@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()

        nome.delete()
        return redirect("receiving:configurationMNFG")


def deleteAreaB(request):
    if request.method == "POST":
        storageZone = request.POST["nomeAreaB"]

        nome = AreaB.objects.get(storageZone=storageZone)

        message = "<b>FA Supply </b></br>Removido " + nome.storageZone
        subject, from_email, to = (
            "Alteração em Receiving - MNFG Supply - Configurations",
            "noreply@visteon.com",
            ["aroque1@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()

        nome.delete()
        return redirect("receiving:configurationMNFG")


def deleteKardex(request):
    if request.method == "POST":
        storageZone = request.POST["nomeKardex"]

        nome = Kardex.objects.get(storageZone=storageZone)

        message = "<b>BP SMD Supply </b></br>Removido " + nome.storageZone
        subject, from_email, to = (
            "Alteração em Receiving - MNFG Supply - Configurations",
            "noreply@visteon.com",
            ["pmarti30@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()

        nome.delete()
        return redirect("receiving:configurationMNFG")


def updateTimers(request):
    if request.method == "POST":

        oldLastUpdate = LastUpdate.objects.get()
        lastUpdate = LastUpdate()
        if request.POST["redLine"] != "":
            lastUpdate.redHour = request.POST["redLine"]
        else:
            lastUpdate.redHour = oldLastUpdate.redHour
        if request.POST["yellowLine"] != "":
            lastUpdate.yellowHour = request.POST["yellowLine"]
        else:
            lastUpdate.yellowHour = oldLastUpdate.yellowHour
        if request.POST["redTime"] != "":
            lastUpdate.lastUpdateRed = request.POST["redTime"]
        else:
            lastUpdate.lastUpdateRed = oldLastUpdate.lastUpdateRed

        lastUpdate.data = oldLastUpdate.data
        lastUpdate.save()

        message = (
            "<b>Alterados Timers </b></br></br><b>Now: </b></br>Red line: "
            + lastUpdate.redHour
            + "</br>Yellow line: "
            + lastUpdate.yellowHour
            + "</br>Red last update Time: "
            + lastUpdate.lastUpdateRed
            + "</br></br><b>Before: </b></br>Red Line: "
            + str(oldLastUpdate.redHour)
            + "</br>Yellow line: "
            + str(oldLastUpdate.yellowHour)
            + "</br>Red last update Time: "
            + str(oldLastUpdate.lastUpdateRed)
        )
        subject, from_email, to = (
            "Alteração em Receiving - MNFG Supply - Configurations",
            "noreply@visteon.com",
            ["aroque1@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()

        oldLastUpdate.delete()

        return redirect("receiving:configurationMNFG")


def addNewItemReceivingPos(request):
    if request.method == "POST":
        itemName = request.POST["itemAdd"]
        posicao = request.POST["posicaoModal"]
        tipoSubItem = request.POST["subItemTipo"]

        if tipoSubItem == "Novo":
            novoTipo = ReceivingSubItemsTipo()
            novoTipo.tipo = itemName
            novoTipo.save()
            return redirect("receiving:configurationsTPM")

        if posicao == "1":
            novoItem = ReceivingPosicao1Items()
            if not ReceivingPosicao1Items.objects.filter(item=itemName).exists():
                novoItem.item = itemName
                novoItem.tipo = tipoSubItem
                novoItem.posicao = posicao
                novoItem.save()
        elif posicao == "2":
            novoItem = ReceivingPosicao2Items()
            if not ReceivingPosicao2Items.objects.filter(item=itemName).exists():
                novoItem.item = itemName
                novoItem.tipo = tipoSubItem
                novoItem.posicao = posicao
                novoItem.save()
        elif posicao == "3":
            novoItem = ReceivingPosicao3Items()
            if not ReceivingPosicao3Items.objects.filter(item=itemName).exists():
                novoItem.item = itemName
                novoItem.tipo = tipoSubItem
                novoItem.posicao = posicao
                novoItem.save()
        elif posicao == "4":
            novoItem = ReceivingPosicao4Items()
            if not ReceivingPosicao4Items.objects.filter(item=itemName).exists():
                novoItem.item = itemName
                novoItem.tipo = tipoSubItem
                novoItem.posicao = posicao
                novoItem.save()
        elif posicao == "5":
            novoItem = ReceivingPosicao5Items()
            if not ReceivingPosicao5Items.objects.filter(item=itemName).exists():
                novoItem.item = itemName
                novoItem.tipo = tipoSubItem
                novoItem.posicao = posicao
                novoItem.save()
        elif posicao == "6":
            novoItem = ReceivingPosicao6Items()
            if not ReceivingPosicao6Items.objects.filter(item=itemName).exists():
                novoItem.item = itemName
                novoItem.tipo = tipoSubItem
                novoItem.posicao = posicao
                novoItem.save()
        elif posicao == "7":
            novoItem = ReceivingPosicao7Items()
            if not ReceivingPosicao7Items.objects.filter(item=itemName).exists():
                novoItem.item = itemName
                novoItem.tipo = tipoSubItem
                novoItem.posicao = posicao
                novoItem.save()
        elif posicao == "8":
            novoItem = ReceivingPosicao8Items()
            if not ReceivingPosicao8Items.objects.filter(item=itemName).exists():
                novoItem.item = itemName
                novoItem.tipo = tipoSubItem
                novoItem.posicao = posicao
                novoItem.save()
        return redirect("receiving:configurationsTPM")


def getBodyInfo(request):
    if request.method == "GET":
        tipo = request.GET["tipo"]

        subItems = ReceivingSubItems.objects

        body = []

        for subItem in subItems.all():
            if subItem.tipo == tipo:
                if subItem.usar == "Stop":
                    elemento = {
                        "linha": '<tr style="background-color: rgb(255, 0, 0, .2)">'
                        "<td>"
                        + subItem.item
                        + '</td><td><input type="checkbox" id="turnoOk" required>&nbsp;&nbsp;&nbsp'
                        ';&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="checkbox" id="turnoNok" required></td><td>'
                        '<input style="width: 370px; margin-left: 8px" class="" type="text" '
                        'name="inicio{{ pos.id }}" id="inicio{{ pos.id }}"></td><td '
                        'style="display:none" id="posicaoGenerico"></td><td style="display:none"'
                        ' id="turnoGenerico"></td><td style="display:none" id="idDiaGenerico"></td></tr>'
                    }
                    body.append(elemento)
                else:
                    elemento = {
                        "linha": "<tr><td>"
                        + subItem.item
                        + '</td><td><input type="checkbox" id="turnoOk" required>&nbsp;&nbsp;&nbsp'
                        ';&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="checkbox" id="turnoNok" required></td><td>'
                        '<input style="width: 370px; margin-left: 8px" class="" type="text" '
                        'name="inicio{{ pos.id }}" id="inicio{{ pos.id }}"></td><td '
                        'style="display:none" id="posicaoGenerico"></td><td style="display:none"'
                        ' id="turnoGenerico"></td><td style="display:none" id="idDiaGenerico"></td></tr>'
                    }
                    body.append(elemento)
        return JsonResponse({"body": body})


# onde é feito o delete de cada linha individual
# def deleteItemReceivingPos1(request):
#     if request.method == "POST":
#         itemID = request.POST['idDelete']
#
#         ReceivingPosicao1Items.objects.get(id=itemID).delete()
#
#         return redirect('receiving:tpm')

# onde é feito o update de cada linha individual
# def editItemReceivingPos1(request):
#     if request.method == "POST":
#         itemID = request.POST['idEdit']
#         itemName = request.POST['itemEdit']
#         itemComentarioFinal = request.POST['comentarioFinalEdit']
#         itemComentarioInicio = request.POST['comentarioInicioEdit']
#
#         item = ReceivingPosicao1Items.objects.get(id=itemID)
#
#         if (itemName):
#             item.item = itemName
#         if (itemComentarioFinal):
#             item.comentarioFinalTurno = itemComentarioFinal
#         if (itemComentarioInicio):
#             item.comentarioInicioTurno = itemComentarioInicio
#
#         item.save()
#
#         return redirect('receiving:tpm')
def submitSubItems(request):
    if request.method == "POST":
        datatable = json.loads(request.POST["datatable"])
        idLinhaBotao = request.POST["idLinhaBotao"]
        for elem in datatable:
            posicao = elem.get("posicao", None)
            idDiaAtual = elem.get("idDia", None)
            idDia = idLinhaBotao + " " + idDiaAtual
            item = elem.get("item", None)
            if posicao == "1":
                if ReceivingPosicao1SubItems.objects.filter(
                    idDia=idDia, item=item
                ).exists():
                    elemento = ReceivingPosicao1SubItems.objects.get(
                        idDia=idDia, item=item
                    )
                    elemento.idDia = idDia
                    elemento.item = elem.get("item", None)
                    elemento.comentario = elem.get("comentario", None)
                    elemento.ok = elem.get("ok", None)
                    elemento.nok = elem.get("nok", None)
                    elemento.save()
                else:
                    elemento = ReceivingPosicao1SubItems()
                    elemento.idDia = idDia
                    elemento.item = elem.get("item", None)
                    elemento.comentario = elem.get("comentario", None)
                    elemento.ok = elem.get("ok", None)
                    elemento.nok = elem.get("nok", None)
                    elemento.save()
            elif posicao == "2":
                if ReceivingPosicao2SubItems.objects.filter(
                    idDia=idDia, item=item
                ).exists():
                    elemento = ReceivingPosicao2SubItems.objects.get(
                        idDia=idDia, item=item
                    )
                    elemento.idDia = idDia
                    elemento.item = elem.get("item", None)
                    elemento.comentario = elem.get("comentario", None)
                    elemento.ok = elem.get("ok", None)
                    elemento.nok = elem.get("nok", None)
                    elemento.save()
                else:
                    elemento = ReceivingPosicao2SubItems()
                    elemento.idDia = idDia
                    elemento.item = elem.get("item", None)
                    elemento.comentario = elem.get("comentario", None)
                    elemento.ok = elem.get("ok", None)
                    elemento.nok = elem.get("nok", None)
                    elemento.save()
            elif posicao == "3":
                if ReceivingPosicao3SubItems.objects.filter(
                    idDia=idDia, item=item
                ).exists():
                    elemento = ReceivingPosicao3SubItems.objects.get(
                        idDia=idDia, item=item
                    )
                    elemento.idDia = idDia
                    elemento.item = elem.get("item", None)
                    elemento.comentario = elem.get("comentario", None)
                    elemento.ok = elem.get("ok", None)
                    elemento.nok = elem.get("nok", None)
                    elemento.save()
                else:
                    elemento = ReceivingPosicao3SubItems()
                    elemento.idDia = idDia
                    elemento.item = elem.get("item", None)
                    elemento.comentario = elem.get("comentario", None)
                    elemento.ok = elem.get("ok", None)
                    elemento.nok = elem.get("nok", None)
                    elemento.save()
            elif posicao == "4":
                if ReceivingPosicao4SubItems.objects.filter(
                    idDia=idDia, item=item
                ).exists():
                    elemento = ReceivingPosicao4SubItems.objects.get(
                        idDia=idDia, item=item
                    )
                    elemento.idDia = idDia
                    elemento.item = elem.get("item", None)
                    elemento.comentario = elem.get("comentario", None)
                    elemento.ok = elem.get("ok", None)
                    elemento.nok = elem.get("nok", None)
                    elemento.save()
                else:
                    elemento = ReceivingPosicao4SubItems()
                    elemento.idDia = idDia
                    elemento.item = elem.get("item", None)
                    elemento.comentario = elem.get("comentario", None)
                    elemento.ok = elem.get("ok", None)
                    elemento.nok = elem.get("nok", None)
                    elemento.save()
            elif posicao == "5":
                if ReceivingPosicao5SubItems.objects.filter(
                    idDia=idDia, item=item
                ).exists():
                    elemento = ReceivingPosicao5SubItems.objects.get(
                        idDia=idDia, item=item
                    )
                    elemento.idDia = idDia
                    elemento.item = elem.get("item", None)
                    elemento.comentario = elem.get("comentario", None)
                    elemento.ok = elem.get("ok", None)
                    elemento.nok = elem.get("nok", None)
                    elemento.save()
                else:
                    elemento = ReceivingPosicao5SubItems()
                    elemento.idDia = idDia
                    elemento.item = elem.get("item", None)
                    elemento.comentario = elem.get("comentario", None)
                    elemento.ok = elem.get("ok", None)
                    elemento.nok = elem.get("nok", None)
                    elemento.save()
            elif posicao == "6":
                if ReceivingPosicao6SubItems.objects.filter(
                    idDia=idDia, item=item
                ).exists():
                    elemento = ReceivingPosicao6SubItems.objects.get(
                        idDia=idDia, item=item
                    )
                    elemento.idDia = idDia
                    elemento.item = elem.get("item", None)
                    elemento.comentario = elem.get("comentario", None)
                    elemento.ok = elem.get("ok", None)
                    elemento.nok = elem.get("nok", None)
                    elemento.save()
                else:
                    elemento = ReceivingPosicao6SubItems()
                    elemento.idDia = idDia
                    elemento.item = elem.get("item", None)
                    elemento.comentario = elem.get("comentario", None)
                    elemento.ok = elem.get("ok", None)
                    elemento.nok = elem.get("nok", None)
                    elemento.save()
            elif posicao == "7":
                if ReceivingPosicao7SubItems.objects.filter(
                    idDia=idDia, item=item
                ).exists():
                    elemento = ReceivingPosicao7SubItems.objects.get(
                        idDia=idDia, item=item
                    )
                    elemento.idDia = idDia
                    elemento.item = elem.get("item", None)
                    elemento.comentario = elem.get("comentario", None)
                    elemento.ok = elem.get("ok", None)
                    elemento.nok = elem.get("nok", None)
                    elemento.save()
                else:
                    elemento = ReceivingPosicao7SubItems()
                    elemento.idDia = idDia
                    elemento.item = elem.get("item", None)
                    elemento.comentario = elem.get("comentario", None)
                    elemento.ok = elem.get("ok", None)
                    elemento.nok = elem.get("nok", None)
                    elemento.save()
            elif posicao == "8":
                if ReceivingPosicao8SubItems.objects.filter(
                    idDia=idDia, item=item
                ).exists():
                    elemento = ReceivingPosicao8SubItems.objects.get(
                        idDia=idDia, item=item
                    )
                    elemento.idDia = idDia
                    elemento.item = elem.get("item", None)
                    elemento.comentario = elem.get("comentario", None)
                    elemento.ok = elem.get("ok", None)
                    elemento.nok = elem.get("nok", None)
                    elemento.save()
                else:
                    elemento = ReceivingPosicao8SubItems()
                    elemento.idDia = idDia
                    elemento.item = elem.get("item", None)
                    elemento.comentario = elem.get("comentario", None)
                    elemento.ok = elem.get("ok", None)
                    elemento.nok = elem.get("nok", None)
                    elemento.save()
    return redirect("receiving:tpm")


# def submitSubItems1(request):
#     if request.method == "POST":
#         datatable = json.loads(request.POST['datatable'])
#         for elem in datatable:
#             posicao = elem.get('posicao', None)
#             item = elem.get('item', None)
#             if ReceivingPosicao1SubItems.objects.filter(idDia=idDia, item=item).exists():
#                 elemento = ReceivingPosicao1SubItems.objects.get(idDia=idDia, item=item)
#                 elemento.idDia = elem.get('idDia', None)
#                 elemento.item = elem.get('item', None)
#                 elemento.comentario = elem.get('comentario', None)
#                 elemento.ok = elem.get('ok', None)
#                 elemento.nok = elem.get('nok', None)
#                 elemento.save()
#             else:
#                 elemento = ReceivingPosicao1SubItems()
#                 elemento.idDia = elem.get('idDia', None)
#                 elemento.item = elem.get('item', None)
#                 elemento.comentario = elem.get('comentario', None)
#                 elemento.ok = elem.get('ok', None)
#                 elemento.nok = elem.get('nok', None)
#                 elemento.save()
#     return redirect('receiving:tpm')


def submitDataFinalTurno(request):
    if request.method == "POST":
        datatable = json.loads(request.POST["datatable"])
        for elem in datatable:
            dataPosicao = elem.get("posicao", None)
            item = elem.get("item", None)
            if ReceivingPosicao1Historico.objects.filter(
                dataPosicao=dataPosicao, item=item
            ).exists():
                elemento = ReceivingPosicao1Historico.objects.get(
                    dataPosicao=dataPosicao, item=item
                )
                if (elemento.inicioTurnoOk or elemento.inicioTurnoNok) and (
                    elemento.fimTurnoOk or elemento.fimTurnoNok
                ):
                    return redirect("receiving:tpm")
                else:
                    elemento.dataPosicao = elem.get("posicao", None)
                    elemento.item = elem.get("item", None)
                    elemento.comentarioFinalTurno = elem.get("comentario", None)
                    fimDoTurno = elem.get("fimDoTurno", None)
                    if fimDoTurno == False:
                        fimDoTurno = None
                    elemento.fimTurnoOk = fimDoTurno
                    fimDoTurnoNok = elem.get("fimDoTurnoNok", None)
                    if fimDoTurnoNok == False:
                        fimDoTurnoNok = None
                    elemento.fimTurnoNok = fimDoTurnoNok
                    elemento.dataFinalTurno = elem.get("data", None)
                    elemento.horaFinalTurno = elem.get("hora", None)
                    elemento.responsavelFinalTurno = elem.get("responsavel", None)
                    elemento.tipo = elem.get("tipo", None)
                    elemento.save()
            else:
                elemento = ReceivingPosicao1Historico()
                elemento.dataPosicao = elem.get("posicao", None)
                elemento.item = elem.get("item", None)
                elemento.comentarioFinalTurno = elem.get("comentario", None)
                fimDoTurno = elem.get("fimDoTurno", None)
                if fimDoTurno == False:
                    fimDoTurno = None
                elemento.fimTurnoOk = fimDoTurno
                fimDoTurnoNok = elem.get("fimDoTurnoNok", None)
                if fimDoTurnoNok == False:
                    fimDoTurnoNok = None
                elemento.fimTurnoNok = fimDoTurnoNok
                elemento.dataFinalTurno = elem.get("data", None)
                elemento.horaFinalTurno = elem.get("hora", None)
                elemento.responsavelFinalTurno = elem.get("responsavel", None)
                elemento.tipo = elem.get("tipo", None)
                elemento.save()
    return redirect("receiving:tpm")


def submitDataInicioTurno(request):
    if request.method == "POST":
        datatable = json.loads(request.POST["datatable"])
        for elem in datatable:
            dataPosicao = elem.get("posicao", None)
            item = elem.get("item", None)
            if ReceivingPosicao1Historico.objects.filter(
                dataPosicao=dataPosicao, item=item
            ).exists():
                elemento = ReceivingPosicao1Historico.objects.get(
                    dataPosicao=dataPosicao, item=item
                )
                if (elemento.inicioTurnoOk or elemento.inicioTurnoNok) and (
                    elemento.fimTurnoOk or elemento.fimTurnoNok
                ):
                    return redirect("receiving:tpm")
                else:
                    elemento.dataPosicao = elem.get("posicao", None)
                    elemento.item = elem.get("item", None)
                    elemento.comentarioInicioTurno = elem.get("comentario", None)
                    inicioDoTurno = elem.get("inicioDoTurno", None)
                    if inicioDoTurno == False:
                        inicioDoTurno = None
                    elemento.inicioTurnoOk = inicioDoTurno
                    inicioDoTurnoNok = elem.get("inicioDoTurnoNok", None)
                    if inicioDoTurnoNok == False:
                        inicioDoTurnoNok = None
                    elemento.inicioTurnoNok = inicioDoTurnoNok
                    elemento.dataInicioTurno = elem.get("data", None)
                    elemento.horaInicioTurno = elem.get("hora", None)
                    elemento.responsavelInicioTurno = elem.get("responsavel", None)
                    elemento.tipo = elem.get("tipo", None)
                    elemento.save()
            else:
                elemento = ReceivingPosicao1Historico()
                elemento.dataPosicao = elem.get("posicao", None)
                elemento.item = elem.get("item", None)
                elemento.comentarioInicioTurno = elem.get("comentario", None)
                inicioDoTurno = elem.get("inicioDoTurno", None)
                if inicioDoTurno == False:
                    inicioDoTurno = None
                elemento.inicioTurnoOk = inicioDoTurno
                inicioDoTurnoNok = elem.get("inicioDoTurnoNok", None)
                if inicioDoTurnoNok == False:
                    inicioDoTurnoNok = None
                elemento.inicioTurnoNok = inicioDoTurnoNok
                elemento.dataInicioTurno = elem.get("data", None)
                elemento.horaInicioTurno = elem.get("hora", None)
                elemento.responsavelInicioTurno = elem.get("responsavel", None)
                elemento.tipo = elem.get("tipo", None)
                elemento.save()
    return redirect("receiving:tpm")


def submitDataFinalTurno2(request):
    if request.method == "POST":
        datatable = json.loads(request.POST["datatable"])
        for elem in datatable:
            dataPosicao = elem.get("posicao", None)
            item = elem.get("item", None)
            if ReceivingPosicao2Historico.objects.filter(
                dataPosicao=dataPosicao, item=item
            ).exists():
                elemento = ReceivingPosicao2Historico.objects.get(
                    dataPosicao=dataPosicao, item=item
                )
                if (elemento.inicioTurnoOk or elemento.inicioTurnoNok) and (
                    elemento.fimTurnoOk or elemento.fimTurnoNok
                ):
                    return redirect("receiving:tpm")
                else:
                    elemento.dataPosicao = elem.get("posicao", None)
                    elemento.item = elem.get("item", None)
                    elemento.comentarioFinalTurno = elem.get("comentario", None)
                    fimDoTurno = elem.get("fimDoTurno", None)
                    if fimDoTurno == False:
                        fimDoTurno = None
                    elemento.fimTurnoOk = fimDoTurno
                    fimDoTurnoNok = elem.get("fimDoTurnoNok", None)
                    if fimDoTurnoNok == False:
                        fimDoTurnoNok = None
                    elemento.fimTurnoNok = fimDoTurnoNok
                    elemento.dataFinalTurno = elem.get("data", None)
                    elemento.horaFinalTurno = elem.get("hora", None)
                    elemento.responsavelFinalTurno = elem.get("responsavel", None)
                    elemento.tipo = elem.get("tipo", None)
                    elemento.save()
            else:
                elemento = ReceivingPosicao2Historico()
                elemento.dataPosicao = elem.get("posicao", None)
                elemento.item = elem.get("item", None)
                elemento.comentarioFinalTurno = elem.get("comentario", None)
                fimDoTurno = elem.get("fimDoTurno", None)
                if fimDoTurno == False:
                    fimDoTurno = None
                elemento.fimTurnoOk = fimDoTurno
                fimDoTurnoNok = elem.get("fimDoTurnoNok", None)
                if fimDoTurnoNok == False:
                    fimDoTurnoNok = None
                elemento.fimTurnoNok = fimDoTurnoNok
                elemento.dataFinalTurno = elem.get("data", None)
                elemento.horaFinalTurno = elem.get("hora", None)
                elemento.responsavelFinalTurno = elem.get("responsavel", None)
                elemento.tipo = elem.get("tipo", None)
                elemento.save()
    return redirect("receiving:tpm")


def submitDataInicioTurno2(request):
    if request.method == "POST":
        datatable = json.loads(request.POST["datatable"])
        for elem in datatable:
            dataPosicao = elem.get("posicao", None)
            item = elem.get("item", None)
            if ReceivingPosicao2Historico.objects.filter(
                dataPosicao=dataPosicao, item=item
            ).exists():
                elemento = ReceivingPosicao2Historico.objects.get(
                    dataPosicao=dataPosicao, item=item
                )
                if (elemento.inicioTurnoOk or elemento.inicioTurnoNok) and (
                    elemento.fimTurnoOk or elemento.fimTurnoNok
                ):
                    return redirect("receiving:tpm")
                else:
                    elemento.dataPosicao = elem.get("posicao", None)
                    elemento.item = elem.get("item", None)
                    elemento.comentarioInicioTurno = elem.get("comentario", None)
                    inicioDoTurno = elem.get("inicioDoTurno", None)
                    if inicioDoTurno == False:
                        inicioDoTurno = None
                    elemento.inicioTurnoOk = inicioDoTurno
                    inicioDoTurnoNok = elem.get("inicioDoTurnoNok", None)
                    if inicioDoTurnoNok == False:
                        inicioDoTurnoNok = None
                    elemento.inicioTurnoNok = inicioDoTurnoNok
                    elemento.dataInicioTurno = elem.get("data", None)
                    elemento.horaInicioTurno = elem.get("hora", None)
                    elemento.responsavelInicioTurno = elem.get("responsavel", None)
                    elemento.tipo = elem.get("tipo", None)
                    elemento.save()
            else:
                elemento = ReceivingPosicao2Historico()
                elemento.dataPosicao = elem.get("posicao", None)
                elemento.item = elem.get("item", None)
                elemento.comentarioInicioTurno = elem.get("comentario", None)
                inicioDoTurno = elem.get("inicioDoTurno", None)
                if inicioDoTurno == False:
                    inicioDoTurno = None
                elemento.inicioTurnoOk = inicioDoTurno
                inicioDoTurnoNok = elem.get("inicioDoTurnoNok", None)
                if inicioDoTurnoNok == False:
                    inicioDoTurnoNok = None
                elemento.inicioTurnoNok = inicioDoTurnoNok
                elemento.dataInicioTurno = elem.get("data", None)
                elemento.horaInicioTurno = elem.get("hora", None)
                elemento.responsavelInicioTurno = elem.get("responsavel", None)
                elemento.tipo = elem.get("tipo", None)
                elemento.save()
    return redirect("receiving:tpm")


def submitDataFinalTurno3(request):
    if request.method == "POST":
        datatable = json.loads(request.POST["datatable"])
        for elem in datatable:
            dataPosicao = elem.get("posicao", None)
            item = elem.get("item", None)
            if ReceivingPosicao3Historico.objects.filter(
                dataPosicao=dataPosicao, item=item
            ).exists():
                elemento = ReceivingPosicao3Historico.objects.get(
                    dataPosicao=dataPosicao, item=item
                )
                if (elemento.inicioTurnoOk or elemento.inicioTurnoNok) and (
                    elemento.fimTurnoOk or elemento.fimTurnoNok
                ):
                    return redirect("receiving:tpm")
                else:
                    elemento.dataPosicao = elem.get("posicao", None)
                    elemento.item = elem.get("item", None)
                    elemento.comentarioFinalTurno = elem.get("comentario", None)
                    fimDoTurno = elem.get("fimDoTurno", None)
                    if fimDoTurno == False:
                        fimDoTurno = None
                    elemento.fimTurnoOk = fimDoTurno
                    fimDoTurnoNok = elem.get("fimDoTurnoNok", None)
                    if fimDoTurnoNok == False:
                        fimDoTurnoNok = None
                    elemento.fimTurnoNok = fimDoTurnoNok
                    elemento.dataFinalTurno = elem.get("data", None)
                    elemento.horaFinalTurno = elem.get("hora", None)
                    elemento.responsavelFinalTurno = elem.get("responsavel", None)
                    elemento.tipo = elem.get("tipo", None)
                    elemento.save()
            else:
                elemento = ReceivingPosicao3Historico()
                elemento.dataPosicao = elem.get("posicao", None)
                elemento.item = elem.get("item", None)
                elemento.comentarioFinalTurno = elem.get("comentario", None)
                fimDoTurno = elem.get("fimDoTurno", None)
                if fimDoTurno == False:
                    fimDoTurno = None
                elemento.fimTurnoOk = fimDoTurno
                fimDoTurnoNok = elem.get("fimDoTurnoNok", None)
                if fimDoTurnoNok == False:
                    fimDoTurnoNok = None
                elemento.fimTurnoNok = fimDoTurnoNok
                elemento.dataFinalTurno = elem.get("data", None)
                elemento.horaFinalTurno = elem.get("hora", None)
                elemento.responsavelFinalTurno = elem.get("responsavel", None)
                elemento.tipo = elem.get("tipo", None)
                elemento.save()
    return redirect("receiving:tpm")


def submitDataInicioTurno3(request):
    if request.method == "POST":
        datatable = json.loads(request.POST["datatable"])
        for elem in datatable:
            dataPosicao = elem.get("posicao", None)
            item = elem.get("item", None)
            if ReceivingPosicao3Historico.objects.filter(
                dataPosicao=dataPosicao, item=item
            ).exists():
                elemento = ReceivingPosicao3Historico.objects.get(
                    dataPosicao=dataPosicao, item=item
                )
                if (elemento.inicioTurnoOk or elemento.inicioTurnoNok) and (
                    elemento.fimTurnoOk or elemento.fimTurnoNok
                ):
                    return redirect("receiving:tpm")
                else:
                    elemento.dataPosicao = elem.get("posicao", None)
                    elemento.item = elem.get("item", None)
                    elemento.comentarioInicioTurno = elem.get("comentario", None)
                    inicioDoTurno = elem.get("inicioDoTurno", None)
                    if inicioDoTurno == False:
                        inicioDoTurno = None
                    elemento.inicioTurnoOk = inicioDoTurno
                    inicioDoTurnoNok = elem.get("inicioDoTurnoNok", None)
                    if inicioDoTurnoNok == False:
                        inicioDoTurnoNok = None
                    elemento.inicioTurnoNok = inicioDoTurnoNok
                    elemento.dataInicioTurno = elem.get("data", None)
                    elemento.horaInicioTurno = elem.get("hora", None)
                    elemento.responsavelInicioTurno = elem.get("responsavel", None)
                    elemento.tipo = elem.get("tipo", None)
                    elemento.save()
            else:
                elemento = ReceivingPosicao3Historico()
                elemento.dataPosicao = elem.get("posicao", None)
                elemento.item = elem.get("item", None)
                elemento.comentarioInicioTurno = elem.get("comentario", None)
                inicioDoTurno = elem.get("inicioDoTurno", None)
                if inicioDoTurno == False:
                    inicioDoTurno = None
                elemento.inicioTurnoOk = inicioDoTurno
                inicioDoTurnoNok = elem.get("inicioDoTurnoNok", None)
                if inicioDoTurnoNok == False:
                    inicioDoTurnoNok = None
                elemento.inicioTurnoNok = inicioDoTurnoNok
                elemento.dataInicioTurno = elem.get("data", None)
                elemento.horaInicioTurno = elem.get("hora", None)
                elemento.responsavelInicioTurno = elem.get("responsavel", None)
                elemento.tipo = elem.get("tipo", None)
                elemento.save()
    return redirect("receiving:tpm")


def submitDataFinalTurno4(request):
    if request.method == "POST":
        datatable = json.loads(request.POST["datatable"])
        for elem in datatable:
            dataPosicao = elem.get("posicao", None)
            item = elem.get("item", None)
            if ReceivingPosicao4Historico.objects.filter(
                dataPosicao=dataPosicao, item=item
            ).exists():
                elemento = ReceivingPosicao4Historico.objects.get(
                    dataPosicao=dataPosicao, item=item
                )
                if (elemento.inicioTurnoOk or elemento.inicioTurnoNok) and (
                    elemento.fimTurnoOk or elemento.fimTurnoNok
                ):
                    return redirect("receiving:tpm")
                else:
                    elemento.dataPosicao = elem.get("posicao", None)
                    elemento.item = elem.get("item", None)
                    elemento.comentarioFinalTurno = elem.get("comentario", None)
                    fimDoTurno = elem.get("fimDoTurno", None)
                    if fimDoTurno == False:
                        fimDoTurno = None
                    elemento.fimTurnoOk = fimDoTurno
                    fimDoTurnoNok = elem.get("fimDoTurnoNok", None)
                    if fimDoTurnoNok == False:
                        fimDoTurnoNok = None
                    elemento.fimTurnoNok = fimDoTurnoNok
                    elemento.dataFinalTurno = elem.get("data", None)
                    elemento.horaFinalTurno = elem.get("hora", None)
                    elemento.responsavelFinalTurno = elem.get("responsavel", None)
                    elemento.tipo = elem.get("tipo", None)
                    elemento.save()
            else:
                elemento = ReceivingPosicao4Historico()
                elemento.dataPosicao = elem.get("posicao", None)
                elemento.item = elem.get("item", None)
                elemento.comentarioFinalTurno = elem.get("comentario", None)
                fimDoTurno = elem.get("fimDoTurno", None)
                if fimDoTurno == False:
                    fimDoTurno = None
                elemento.fimTurnoOk = fimDoTurno
                fimDoTurnoNok = elem.get("fimDoTurnoNok", None)
                if fimDoTurnoNok == False:
                    fimDoTurnoNok = None
                elemento.fimTurnoNok = fimDoTurnoNok
                elemento.dataFinalTurno = elem.get("data", None)
                elemento.horaFinalTurno = elem.get("hora", None)
                elemento.responsavelFinalTurno = elem.get("responsavel", None)
                elemento.tipo = elem.get("tipo", None)
                elemento.save()
    return redirect("receiving:tpm")


def submitDataInicioTurno4(request):
    if request.method == "POST":
        datatable = json.loads(request.POST["datatable"])
        for elem in datatable:
            dataPosicao = elem.get("posicao", None)
            item = elem.get("item", None)
            if ReceivingPosicao4Historico.objects.filter(
                dataPosicao=dataPosicao, item=item
            ).exists():
                elemento = ReceivingPosicao4Historico.objects.get(
                    dataPosicao=dataPosicao, item=item
                )
                if (elemento.inicioTurnoOk or elemento.inicioTurnoNok) and (
                    elemento.fimTurnoOk or elemento.fimTurnoNok
                ):
                    return redirect("receiving:tpm")
                else:
                    elemento.dataPosicao = elem.get("posicao", None)
                    elemento.item = elem.get("item", None)
                    elemento.comentarioInicioTurno = elem.get("comentario", None)
                    inicioDoTurno = elem.get("inicioDoTurno", None)
                    if inicioDoTurno == False:
                        inicioDoTurno = None
                    elemento.inicioTurnoOk = inicioDoTurno
                    inicioDoTurnoNok = elem.get("inicioDoTurnoNok", None)
                    if inicioDoTurnoNok == False:
                        inicioDoTurnoNok = None
                    elemento.inicioTurnoNok = inicioDoTurnoNok
                    elemento.dataInicioTurno = elem.get("data", None)
                    elemento.horaInicioTurno = elem.get("hora", None)
                    elemento.responsavelInicioTurno = elem.get("responsavel", None)
                    elemento.tipo = elem.get("tipo", None)
                    elemento.save()
            else:
                elemento = ReceivingPosicao4Historico()
                elemento.dataPosicao = elem.get("posicao", None)
                elemento.item = elem.get("item", None)
                elemento.comentarioInicioTurno = elem.get("comentario", None)
                inicioDoTurno = elem.get("inicioDoTurno", None)
                if inicioDoTurno == False:
                    inicioDoTurno = None
                elemento.inicioTurnoOk = inicioDoTurno
                inicioDoTurnoNok = elem.get("inicioDoTurnoNok", None)
                if inicioDoTurnoNok == False:
                    inicioDoTurnoNok = None
                elemento.inicioTurnoNok = inicioDoTurnoNok
                elemento.dataInicioTurno = elem.get("data", None)
                elemento.horaInicioTurno = elem.get("hora", None)
                elemento.responsavelInicioTurno = elem.get("responsavel", None)
                elemento.tipo = elem.get("tipo", None)
                elemento.save()
    return redirect("receiving:tpm")


def submitDataFinalTurno5(request):
    if request.method == "POST":
        datatable = json.loads(request.POST["datatable"])
        for elem in datatable:
            dataPosicao = elem.get("posicao", None)
            item = elem.get("item", None)
            if ReceivingPosicao5Historico.objects.filter(
                dataPosicao=dataPosicao, item=item
            ).exists():
                elemento = ReceivingPosicao5Historico.objects.get(
                    dataPosicao=dataPosicao, item=item
                )
                if (elemento.inicioTurnoOk or elemento.inicioTurnoNok) and (
                    elemento.fimTurnoOk or elemento.fimTurnoNok
                ):
                    return redirect("receiving:tpm")
                else:
                    elemento.dataPosicao = elem.get("posicao", None)
                    elemento.item = elem.get("item", None)
                    elemento.comentarioFinalTurno = elem.get("comentario", None)
                    fimDoTurno = elem.get("fimDoTurno", None)
                    if fimDoTurno == False:
                        fimDoTurno = None
                    elemento.fimTurnoOk = fimDoTurno
                    fimDoTurnoNok = elem.get("fimDoTurnoNok", None)
                    if fimDoTurnoNok == False:
                        fimDoTurnoNok = None
                    elemento.fimTurnoNok = fimDoTurnoNok
                    elemento.dataFinalTurno = elem.get("data", None)
                    elemento.horaFinalTurno = elem.get("hora", None)
                    elemento.responsavelFinalTurno = elem.get("responsavel", None)
                    elemento.tipo = elem.get("tipo", None)
                    elemento.save()
            else:
                elemento = ReceivingPosicao5Historico()
                elemento.dataPosicao = elem.get("posicao", None)
                elemento.item = elem.get("item", None)
                elemento.comentarioFinalTurno = elem.get("comentario", None)
                fimDoTurno = elem.get("fimDoTurno", None)
                if fimDoTurno == False:
                    fimDoTurno = None
                elemento.fimTurnoOk = fimDoTurno
                fimDoTurnoNok = elem.get("fimDoTurnoNok", None)
                if fimDoTurnoNok == False:
                    fimDoTurnoNok = None
                elemento.fimTurnoNok = fimDoTurnoNok
                elemento.dataFinalTurno = elem.get("data", None)
                elemento.horaFinalTurno = elem.get("hora", None)
                elemento.responsavelFinalTurno = elem.get("responsavel", None)
                elemento.tipo = elem.get("tipo", None)
                elemento.save()
    return redirect("receiving:tpm")


def submitDataInicioTurno5(request):
    if request.method == "POST":
        datatable = json.loads(request.POST["datatable"])
        for elem in datatable:
            dataPosicao = elem.get("posicao", None)
            item = elem.get("item", None)
            if ReceivingPosicao5Historico.objects.filter(
                dataPosicao=dataPosicao, item=item
            ).exists():
                elemento = ReceivingPosicao5Historico.objects.get(
                    dataPosicao=dataPosicao, item=item
                )
                if (elemento.inicioTurnoOk or elemento.inicioTurnoNok) and (
                    elemento.fimTurnoOk or elemento.fimTurnoNok
                ):
                    return redirect("receiving:tpm")
                else:
                    elemento.dataPosicao = elem.get("posicao", None)
                    elemento.item = elem.get("item", None)
                    elemento.comentarioInicioTurno = elem.get("comentario", None)
                    inicioDoTurno = elem.get("inicioDoTurno", None)
                    if inicioDoTurno == False:
                        inicioDoTurno = None
                    elemento.inicioTurnoOk = inicioDoTurno
                    inicioDoTurnoNok = elem.get("inicioDoTurnoNok", None)
                    if inicioDoTurnoNok == False:
                        inicioDoTurnoNok = None
                    elemento.inicioTurnoNok = inicioDoTurnoNok
                    elemento.dataInicioTurno = elem.get("data", None)
                    elemento.horaInicioTurno = elem.get("hora", None)
                    elemento.responsavelInicioTurno = elem.get("responsavel", None)
                    elemento.tipo = elem.get("tipo", None)
                    elemento.save()
            else:
                elemento = ReceivingPosicao5Historico()
                elemento.dataPosicao = elem.get("posicao", None)
                elemento.item = elem.get("item", None)
                elemento.comentarioInicioTurno = elem.get("comentario", None)
                inicioDoTurno = elem.get("inicioDoTurno", None)
                if inicioDoTurno == False:
                    inicioDoTurno = None
                elemento.inicioTurnoOk = inicioDoTurno
                inicioDoTurnoNok = elem.get("inicioDoTurnoNok", None)
                if inicioDoTurnoNok == False:
                    inicioDoTurnoNok = None
                elemento.inicioTurnoNok = inicioDoTurnoNok
                elemento.dataInicioTurno = elem.get("data", None)
                elemento.horaInicioTurno = elem.get("hora", None)
                elemento.responsavelInicioTurno = elem.get("responsavel", None)
                elemento.tipo = elem.get("tipo", None)
                elemento.save()
    return redirect("receiving:tpm")


def submitDataFinalTurno6(request):
    if request.method == "POST":
        datatable = json.loads(request.POST["datatable"])
        for elem in datatable:
            dataPosicao = elem.get("posicao", None)
            item = elem.get("item", None)
            if ReceivingPosicao6Historico.objects.filter(
                dataPosicao=dataPosicao, item=item
            ).exists():
                elemento = ReceivingPosicao6Historico.objects.get(
                    dataPosicao=dataPosicao, item=item
                )
                if (elemento.inicioTurnoOk or elemento.inicioTurnoNok) and (
                    elemento.fimTurnoOk or elemento.fimTurnoNok
                ):
                    return redirect("receiving:tpm")
                else:
                    elemento.dataPosicao = elem.get("posicao", None)
                    elemento.item = elem.get("item", None)
                    elemento.comentarioFinalTurno = elem.get("comentario", None)
                    fimDoTurno = elem.get("fimDoTurno", None)
                    if fimDoTurno == False:
                        fimDoTurno = None
                    elemento.fimTurnoOk = fimDoTurno
                    fimDoTurnoNok = elem.get("fimDoTurnoNok", None)
                    if fimDoTurnoNok == False:
                        fimDoTurnoNok = None
                    elemento.fimTurnoNok = fimDoTurnoNok
                    elemento.dataFinalTurno = elem.get("data", None)
                    elemento.horaFinalTurno = elem.get("hora", None)
                    elemento.responsavelFinalTurno = elem.get("responsavel", None)
                    elemento.tipo = elem.get("tipo", None)
                    elemento.save()
            else:
                elemento = ReceivingPosicao6Historico()
                elemento.dataPosicao = elem.get("posicao", None)
                elemento.item = elem.get("item", None)
                elemento.comentarioFinalTurno = elem.get("comentario", None)
                fimDoTurno = elem.get("fimDoTurno", None)
                if fimDoTurno == False:
                    fimDoTurno = None
                elemento.fimTurnoOk = fimDoTurno
                fimDoTurnoNok = elem.get("fimDoTurnoNok", None)
                if fimDoTurnoNok == False:
                    fimDoTurnoNok = None
                elemento.fimTurnoNok = fimDoTurnoNok
                elemento.dataFinalTurno = elem.get("data", None)
                elemento.horaFinalTurno = elem.get("hora", None)
                elemento.responsavelFinalTurno = elem.get("responsavel", None)
                elemento.tipo = elem.get("tipo", None)
                elemento.save()
    return redirect("receiving:tpm")


def submitDataInicioTurno6(request):
    if request.method == "POST":
        datatable = json.loads(request.POST["datatable"])
        for elem in datatable:
            dataPosicao = elem.get("posicao", None)
            item = elem.get("item", None)
            if ReceivingPosicao6Historico.objects.filter(
                dataPosicao=dataPosicao, item=item
            ).exists():
                elemento = ReceivingPosicao6Historico.objects.get(
                    dataPosicao=dataPosicao, item=item
                )
                if (elemento.inicioTurnoOk or elemento.inicioTurnoNok) and (
                    elemento.fimTurnoOk or elemento.fimTurnoNok
                ):
                    return redirect("receiving:tpm")
                else:
                    elemento.dataPosicao = elem.get("posicao", None)
                    elemento.item = elem.get("item", None)
                    elemento.comentarioInicioTurno = elem.get("comentario", None)
                    inicioDoTurno = elem.get("inicioDoTurno", None)
                    if inicioDoTurno == False:
                        inicioDoTurno = None
                    elemento.inicioTurnoOk = inicioDoTurno
                    inicioDoTurnoNok = elem.get("inicioDoTurnoNok", None)
                    if inicioDoTurnoNok == False:
                        inicioDoTurnoNok = None
                    elemento.inicioTurnoNok = inicioDoTurnoNok
                    elemento.dataInicioTurno = elem.get("data", None)
                    elemento.horaInicioTurno = elem.get("hora", None)
                    elemento.responsavelInicioTurno = elem.get("responsavel", None)
                    elemento.tipo = elem.get("tipo", None)
                    elemento.save()
            else:
                elemento = ReceivingPosicao6Historico()
                elemento.dataPosicao = elem.get("posicao", None)
                elemento.item = elem.get("item", None)
                elemento.comentarioInicioTurno = elem.get("comentario", None)
                inicioDoTurno = elem.get("inicioDoTurno", None)
                if inicioDoTurno == False:
                    inicioDoTurno = None
                elemento.inicioTurnoOk = inicioDoTurno
                inicioDoTurnoNok = elem.get("inicioDoTurnoNok", None)
                if inicioDoTurnoNok == False:
                    inicioDoTurnoNok = None
                elemento.inicioTurnoNok = inicioDoTurnoNok
                elemento.dataInicioTurno = elem.get("data", None)
                elemento.horaInicioTurno = elem.get("hora", None)
                elemento.responsavelInicioTurno = elem.get("responsavel", None)
                elemento.tipo = elem.get("tipo", None)
                elemento.save()
    return redirect("receiving:tpm")


def submitDataFinalTurno7(request):
    if request.method == "POST":
        datatable = json.loads(request.POST["datatable"])
        for elem in datatable:
            dataPosicao = elem.get("posicao", None)
            item = elem.get("item", None)
            if ReceivingPosicao7Historico.objects.filter(
                dataPosicao=dataPosicao, item=item
            ).exists():
                elemento = ReceivingPosicao7Historico.objects.get(
                    dataPosicao=dataPosicao, item=item
                )
                if (elemento.inicioTurnoOk or elemento.inicioTurnoNok) and (
                    elemento.fimTurnoOk or elemento.fimTurnoNok
                ):
                    return redirect("receiving:tpm")
                else:
                    elemento.dataPosicao = elem.get("posicao", None)
                    elemento.item = elem.get("item", None)
                    elemento.comentarioFinalTurno = elem.get("comentario", None)
                    fimDoTurno = elem.get("fimDoTurno", None)
                    if fimDoTurno == False:
                        fimDoTurno = None
                    elemento.fimTurnoOk = fimDoTurno
                    fimDoTurnoNok = elem.get("fimDoTurnoNok", None)
                    if fimDoTurnoNok == False:
                        fimDoTurnoNok = None
                    elemento.fimTurnoNok = fimDoTurnoNok
                    elemento.dataFinalTurno = elem.get("data", None)
                    elemento.horaFinalTurno = elem.get("hora", None)
                    elemento.responsavelFinalTurno = elem.get("responsavel", None)
                    elemento.tipo = elem.get("tipo", None)
                    elemento.save()
            else:
                elemento = ReceivingPosicao7Historico()
                elemento.dataPosicao = elem.get("posicao", None)
                elemento.item = elem.get("item", None)
                elemento.comentarioFinalTurno = elem.get("comentario", None)
                fimDoTurno = elem.get("fimDoTurno", None)
                if fimDoTurno == False:
                    fimDoTurno = None
                elemento.fimTurnoOk = fimDoTurno
                fimDoTurnoNok = elem.get("fimDoTurnoNok", None)
                if fimDoTurnoNok == False:
                    fimDoTurnoNok = None
                elemento.fimTurnoNok = fimDoTurnoNok
                elemento.dataFinalTurno = elem.get("data", None)
                elemento.horaFinalTurno = elem.get("hora", None)
                elemento.responsavelFinalTurno = elem.get("responsavel", None)
                elemento.tipo = elem.get("tipo", None)
                elemento.save()
    return redirect("receiving:tpm")


def submitDataInicioTurno7(request):
    if request.method == "POST":
        datatable = json.loads(request.POST["datatable"])
        for elem in datatable:
            dataPosicao = elem.get("posicao", None)
            item = elem.get("item", None)
            if ReceivingPosicao7Historico.objects.filter(
                dataPosicao=dataPosicao, item=item
            ).exists():
                elemento = ReceivingPosicao7Historico.objects.get(
                    dataPosicao=dataPosicao, item=item
                )
                if (elemento.inicioTurnoOk or elemento.inicioTurnoNok) and (
                    elemento.fimTurnoOk or elemento.fimTurnoNok
                ):
                    return redirect("receiving:tpm")
                else:
                    elemento.dataPosicao = elem.get("posicao", None)
                    elemento.item = elem.get("item", None)
                    elemento.comentarioInicioTurno = elem.get("comentario", None)
                    inicioDoTurno = elem.get("inicioDoTurno", None)
                    if inicioDoTurno == False:
                        inicioDoTurno = None
                    elemento.inicioTurnoOk = inicioDoTurno
                    inicioDoTurnoNok = elem.get("inicioDoTurnoNok", None)
                    if inicioDoTurnoNok == False:
                        inicioDoTurnoNok = None
                    elemento.inicioTurnoNok = inicioDoTurnoNok
                    elemento.dataInicioTurno = elem.get("data", None)
                    elemento.horaInicioTurno = elem.get("hora", None)
                    elemento.responsavelInicioTurno = elem.get("responsavel", None)
                    elemento.tipo = elem.get("tipo", None)
                    elemento.save()
            else:
                elemento = ReceivingPosicao7Historico()
                elemento.dataPosicao = elem.get("posicao", None)
                elemento.item = elem.get("item", None)
                elemento.comentarioInicioTurno = elem.get("comentario", None)
                inicioDoTurno = elem.get("inicioDoTurno", None)
                if inicioDoTurno == False:
                    inicioDoTurno = None
                elemento.inicioTurnoOk = inicioDoTurno
                inicioDoTurnoNok = elem.get("inicioDoTurnoNok", None)
                if inicioDoTurnoNok == False:
                    inicioDoTurnoNok = None
                elemento.inicioTurnoNok = inicioDoTurnoNok
                elemento.dataInicioTurno = elem.get("data", None)
                elemento.horaInicioTurno = elem.get("hora", None)
                elemento.responsavelInicioTurno = elem.get("responsavel", None)
                elemento.tipo = elem.get("tipo", None)
                elemento.save()
    return redirect("receiving:tpm")


def submitDataFinalTurno8(request):
    if request.method == "POST":
        datatable = json.loads(request.POST["datatable"])
        for elem in datatable:
            dataPosicao = elem.get("posicao", None)
            item = elem.get("item", None)
            if ReceivingPosicao8Historico.objects.filter(
                dataPosicao=dataPosicao, item=item
            ).exists():
                elemento = ReceivingPosicao8Historico.objects.get(
                    dataPosicao=dataPosicao, item=item
                )
                if (elemento.inicioTurnoOk or elemento.inicioTurnoNok) and (
                    elemento.fimTurnoOk or elemento.fimTurnoNok
                ):
                    return redirect("receiving:tpm")
                else:
                    elemento.dataPosicao = elem.get("posicao", None)
                    elemento.item = elem.get("item", None)
                    elemento.comentarioFinalTurno = elem.get("comentario", None)
                    fimDoTurno = elem.get("fimDoTurno", None)
                    if fimDoTurno == False:
                        fimDoTurno = None
                    elemento.fimTurnoOk = fimDoTurno
                    fimDoTurnoNok = elem.get("fimDoTurnoNok", None)
                    if fimDoTurnoNok == False:
                        fimDoTurnoNok = None
                    elemento.fimTurnoNok = fimDoTurnoNok
                    elemento.dataFinalTurno = elem.get("data", None)
                    elemento.horaFinalTurno = elem.get("hora", None)
                    elemento.responsavelFinalTurno = elem.get("responsavel", None)
                    elemento.tipo = elem.get("tipo", None)
                    elemento.save()
            else:
                elemento = ReceivingPosicao8Historico()
                elemento.dataPosicao = elem.get("posicao", None)
                elemento.item = elem.get("item", None)
                elemento.comentarioFinalTurno = elem.get("comentario", None)
                fimDoTurno = elem.get("fimDoTurno", None)
                if fimDoTurno == False:
                    fimDoTurno = None
                elemento.fimTurnoOk = fimDoTurno
                fimDoTurnoNok = elem.get("fimDoTurnoNok", None)
                if fimDoTurnoNok == False:
                    fimDoTurnoNok = None
                elemento.fimTurnoNok = fimDoTurnoNok
                elemento.dataFinalTurno = elem.get("data", None)
                elemento.horaFinalTurno = elem.get("hora", None)
                elemento.responsavelFinalTurno = elem.get("responsavel", None)
                elemento.tipo = elem.get("tipo", None)
                elemento.save()
    return redirect("receiving:tpm")


def submitDataInicioTurno8(request):
    if request.method == "POST":
        datatable = json.loads(request.POST["datatable"])
        for elem in datatable:
            dataPosicao = elem.get("posicao", None)
            item = elem.get("item", None)
            if ReceivingPosicao8Historico.objects.filter(
                dataPosicao=dataPosicao, item=item
            ).exists():
                elemento = ReceivingPosicao8Historico.objects.get(
                    dataPosicao=dataPosicao, item=item
                )
                if (elemento.inicioTurnoOk or elemento.inicioTurnoNok) and (
                    elemento.fimTurnoOk or elemento.fimTurnoNok
                ):
                    return redirect("receiving:tpm")
                else:
                    elemento.dataPosicao = elem.get("posicao", None)
                    elemento.item = elem.get("item", None)
                    elemento.comentarioInicioTurno = elem.get("comentario", None)
                    inicioDoTurno = elem.get("inicioDoTurno", None)
                    if inicioDoTurno == False:
                        inicioDoTurno = None
                    elemento.inicioTurnoOk = inicioDoTurno
                    inicioDoTurnoNok = elem.get("inicioDoTurnoNok", None)
                    if inicioDoTurnoNok == False:
                        inicioDoTurnoNok = None
                    elemento.inicioTurnoNok = inicioDoTurnoNok
                    elemento.dataInicioTurno = elem.get("data", None)
                    elemento.horaInicioTurno = elem.get("hora", None)
                    elemento.responsavelInicioTurno = elem.get("responsavel", None)
                    elemento.tipo = elem.get("tipo", None)
                    elemento.save()
            else:
                elemento = ReceivingPosicao8Historico()
                elemento.dataPosicao = elem.get("posicao", None)
                elemento.item = elem.get("item", None)
                elemento.comentarioInicioTurno = elem.get("comentario", None)
                inicioDoTurno = elem.get("inicioDoTurno", None)
                if inicioDoTurno == False:
                    inicioDoTurno = None
                elemento.inicioTurnoOk = inicioDoTurno
                inicioDoTurnoNok = elem.get("inicioDoTurnoNok", None)
                if inicioDoTurnoNok == False:
                    inicioDoTurnoNok = None
                elemento.inicioTurnoNok = inicioDoTurnoNok
                elemento.dataInicioTurno = elem.get("data", None)
                elemento.horaInicioTurno = elem.get("hora", None)
                elemento.responsavelInicioTurno = elem.get("responsavel", None)
                elemento.tipo = elem.get("tipo", None)
                elemento.save()
    return redirect("receiving:tpm")


def getPosicao1Data(request):
    if request.method == "GET":
        dataPosicao = request.GET["posicaoData"]
        elementosFiltrados = ReceivingPosicao1Historico.objects.filter(
            dataPosicao=dataPosicao
        )
        listElementosFiltrados = serialize("json", elementosFiltrados)
        return JsonResponse(listElementosFiltrados, safe=False)


def getPosicao2Data(request):
    if request.method == "GET":
        dataPosicao = request.GET["posicaoData"]
        elementosFiltrados = ReceivingPosicao2Historico.objects.filter(
            dataPosicao=dataPosicao
        )
        listElementosFiltrados = serialize("json", elementosFiltrados)
        return JsonResponse(listElementosFiltrados, safe=False)


def getPosicao3Data(request):
    if request.method == "GET":
        dataPosicao = request.GET["posicaoData"]
        elementosFiltrados = ReceivingPosicao3Historico.objects.filter(
            dataPosicao=dataPosicao
        )
        listElementosFiltrados = serialize("json", elementosFiltrados)
        return JsonResponse(listElementosFiltrados, safe=False)


def getPosicao4Data(request):
    if request.method == "GET":
        dataPosicao = request.GET["posicaoData"]
        elementosFiltrados = ReceivingPosicao4Historico.objects.filter(
            dataPosicao=dataPosicao
        )
        listElementosFiltrados = serialize("json", elementosFiltrados)
        return JsonResponse(listElementosFiltrados, safe=False)


def getPosicao5Data(request):
    if request.method == "GET":
        dataPosicao = request.GET["posicaoData"]
        elementosFiltrados = ReceivingPosicao5Historico.objects.filter(
            dataPosicao=dataPosicao
        )
        listElementosFiltrados = serialize("json", elementosFiltrados)
        return JsonResponse(listElementosFiltrados, safe=False)


def getPosicao6Data(request):
    if request.method == "GET":
        dataPosicao = request.GET["posicaoData"]
        elementosFiltrados = ReceivingPosicao6Historico.objects.filter(
            dataPosicao=dataPosicao
        )
        listElementosFiltrados = serialize("json", elementosFiltrados)
        return JsonResponse(listElementosFiltrados, safe=False)


def getPosicao7Data(request):
    if request.method == "GET":
        dataPosicao = request.GET["posicaoData"]
        elementosFiltrados = ReceivingPosicao7Historico.objects.filter(
            dataPosicao=dataPosicao
        )
        listElementosFiltrados = serialize("json", elementosFiltrados)
        return JsonResponse(listElementosFiltrados, safe=False)


def getPosicao8Data(request):
    if request.method == "GET":
        dataPosicao = request.GET["posicaoData"]
        elementosFiltrados = ReceivingPosicao8Historico.objects.filter(
            dataPosicao=dataPosicao
        )
        listElementosFiltrados = serialize("json", elementosFiltrados)
        return JsonResponse(listElementosFiltrados, safe=False)


def deleteSelectedItems(request):
    if request.method == "POST":
        items = json.loads(request.POST["items[]"])
        posicao = request.POST["posicao"]

        if posicao == "1":
            for elem in items:
                ReceivingPosicao1Items.objects.get(item=elem).delete()
        if posicao == "2":
            for elem in items:
                ReceivingPosicao2Items.objects.get(item=elem).delete()
        if posicao == "3":
            for elem in items:
                ReceivingPosicao3Items.objects.get(item=elem).delete()
        if posicao == "4":
            for elem in items:
                ReceivingPosicao4Items.objects.get(item=elem).delete()
        if posicao == "5":
            for elem in items:
                ReceivingPosicao5Items.objects.get(item=elem).delete()
        if posicao == "6":
            for elem in items:
                ReceivingPosicao6Items.objects.get(item=elem).delete()
        if posicao == "7":
            for elem in items:
                ReceivingPosicao7Items.objects.get(item=elem).delete()
        if posicao == "8":
            for elem in items:
                ReceivingPosicao8Items.objects.get(item=elem).delete()
    return redirect("receiving:configurationsTPM")


def deleteSelectedSubItems(request):
    items = json.loads(request.POST["items[]"])
    for elem in items:
        ReceivingSubItems.objects.get(item=elem).delete()
    return redirect("receiving:configurationsTPM")


# def updateComentario1(request):
#     if request.method == "POST":
#         id = request.POST['nome']
#         if id.startswith('inicio'):
#             id = id.removeprefix('inicio')
#             item = ReceivingPosicao1Items.objects.get(id=id)
#             item.comentarioInicioTurno = request.POST['comentario']
#             item.save()
#
#         elif id.startswith('fim'):
#             id = int(id.removeprefix('fim'), base=10)
#             item = ReceivingPosicao1Items.objects.get(id=id)
#             item.comentarioFinalTurno = request.POST['comentario']
#             item.save()
#         return redirect('receiving:tpm')
#
#
# def updateComentario2(request):
#     if request.method == "POST":
#         id = request.POST['nome']
#         if id.startswith('inicio'):
#             id = id.removeprefix('inicio')
#             item = ReceivingPosicao2Items.objects.get(id=id)
#             item.comentarioInicioTurno = request.POST['comentario']
#             item.save()
#
#         elif id.startswith('fim'):
#             id = int(id.removeprefix('fim'), base=10)
#             item = ReceivingPosicao2Items.objects.get(id=id)
#             item.comentarioFinalTurno = request.POST['comentario']
#             item.save()
#         return redirect('receiving:tpm')
#
#
# def updateComentario3(request):
#     if request.method == "POST":
#         id = request.POST['nome']
#         if id.startswith('inicio'):
#             id = id.removeprefix('inicio')
#             item = ReceivingPosicao3Items.objects.get(id=id)
#             item.comentarioInicioTurno = request.POST['comentario']
#             item.save()
#
#         elif id.startswith('fim'):
#             id = int(id.removeprefix('fim'), base=10)
#             item = ReceivingPosicao3Items.objects.get(id=id)
#             item.comentarioFinalTurno = request.POST['comentario']
#             item.save()
#         return redirect('receiving:tpm')
#
#
# def updateComentario4(request):
#     if request.method == "POST":
#         id = request.POST['nome']
#         if id.startswith('inicio'):
#             id = id.removeprefix('inicio')
#             item = ReceivingPosicao4Items.objects.get(id=id)
#             item.comentarioInicioTurno = request.POST['comentario']
#             item.save()
#
#         elif id.startswith('fim'):
#             id = int(id.removeprefix('fim'), base=10)
#             item = ReceivingPosicao4Items.objects.get(id=id)
#             item.comentarioFinalTurno = request.POST['comentario']
#             item.save()
#         return redirect('receiving:tpm')
#
#
# def updateComentario5(request):
#     if request.method == "POST":
#         id = request.POST['nome']
#         if id.startswith('inicio'):
#             id = id.removeprefix('inicio')
#             item = ReceivingPosicao5Items.objects.get(id=id)
#             item.comentarioInicioTurno = request.POST['comentario']
#             item.save()
#
#         elif id.startswith('fim'):
#             id = int(id.removeprefix('fim'), base=10)
#             item = ReceivingPosicao5Items.objects.get(id=id)
#             item.comentarioFinalTurno = request.POST['comentario']
#             item.save()
#         return redirect('receiving:tpm')
#
#
# def updateComentario6(request):
#     if request.method == "POST":
#         id = request.POST['nome']
#         if id.startswith('inicio'):
#             id = id.removeprefix('inicio')
#             item = ReceivingPosicao6Items.objects.get(id=id)
#             item.comentarioInicioTurno = request.POST['comentario']
#             item.save()
#
#         elif id.startswith('fim'):
#             id = int(id.removeprefix('fim'), base=10)
#             item = ReceivingPosicao6Items.objects.get(id=id)
#             item.comentarioFinalTurno = request.POST['comentario']
#             item.save()
#         return redirect('receiving:tpm')
#
#
# def updateComentario7(request):
#     if request.method == "POST":
#         id = request.POST['nome']
#         if id.startswith('inicio'):
#             id = id.removeprefix('inicio')
#             item = ReceivingPosicao7Items.objects.get(id=id)
#             item.comentarioInicioTurno = request.POST['comentario']
#             item.save()
#
#         elif id.startswith('fim'):
#             id = int(id.removeprefix('fim'), base=10)
#             item = ReceivingPosicao7Items.objects.get(id=id)
#             item.comentarioFinalTurno = request.POST['comentario']
#             item.save()
#         return redirect('receiving:tpm')
#
#
# def updateComentario8(request):
#     if request.method == "POST":
#         id = request.POST['nome']
#         if id.startswith('inicio'):
#             id = id.removeprefix('inicio')
#             item = ReceivingPosicao8Items.objects.get(id=id)
#             item.comentarioInicioTurno = request.POST['comentario']
#             item.save()
#
#         elif id.startswith('fim'):
#             id = int(id.removeprefix('fim'), base=10)
#             item = ReceivingPosicao8Items.objects.get(id=id)
#             item.comentarioFinalTurno = request.POST['comentario']
#             item.save()
#         return redirect('receiving:tpm')


def getSubItems(request):
    if request.method == "GET":
        dataPosicao = request.GET["dataPosicao"]
        posicao = request.GET["posicao"]
        nomeLinhaBotao = request.GET["nomeLinhaBotao"]
        listaObjetos = []

        if "inicio" in dataPosicao:
            dataPosicao = dataPosicao[-30:]
        elif "final" in dataPosicao:
            dataPosicao = dataPosicao[-29:]

        idDia = nomeLinhaBotao + " " + dataPosicao

        if posicao == "1":
            listaObjetos = ReceivingPosicao1SubItems.objects.filter(idDia=idDia)
        elif posicao == "2":
            listaObjetos = ReceivingPosicao2SubItems.objects.filter(idDia=idDia)
        elif posicao == "3":
            listaObjetos = ReceivingPosicao3SubItems.objects.filter(idDia=idDia)
        elif posicao == "4":
            listaObjetos = ReceivingPosicao4SubItems.objects.filter(idDia=idDia)
        elif posicao == "5":
            listaObjetos = ReceivingPosicao5SubItems.objects.filter(idDia=idDia)
        elif posicao == "6":
            listaObjetos = ReceivingPosicao6SubItems.objects.filter(idDia=idDia)
        elif posicao == "7":
            listaObjetos = ReceivingPosicao7SubItems.objects.filter(idDia=idDia)
        elif posicao == "8":
            listaObjetos = ReceivingPosicao8SubItems.objects.filter(idDia=idDia)

        listElementosFiltrados = serialize("json", listaObjetos)
        return JsonResponse(listElementosFiltrados, safe=False)
    return redirect("receiving:tpm")


def addNewSubItem(request):
    nome = request.POST["itemAdd"]
    tipo = request.POST.getlist("subItemTipo")
    usar = request.POST["usar"]
    stringTipo = ""

    for elem in tipo:
        stringTipo += ", " + elem

    novoItem = ReceivingSubItems()
    if not ReceivingSubItems.objects.filter(item=nome).exists():
        novoItem.item = nome
        novoItem.tipo = stringTipo[2:]
        novoItem.usar = usar
        novoItem.save()

    return redirect("receiving:configurationsTPM")


def changeUserGroups(request):
    if request.method == "POST":
        user = User.objects.get(username=request.POST["username"])
        grupo = request.POST["paginas"]
        if User.objects.filter(
            username=request.POST["username"], groups__name="receivingMNFG"
        ):
            my_group = Group.objects.using("default").get(name="receivingMNFG")
            my_group.user_set.remove(user)
        if User.objects.filter(
            username=request.POST["username"], groups__name="receivingLINES"
        ):
            my_group = Group.objects.using("default").get(name="receivingLINES")
            my_group.user_set.remove(user)
        if User.objects.filter(
            username=request.POST["username"], groups__name="receivingTPM"
        ):
            my_group = Group.objects.using("default").get(name="receivingTPM")
            my_group.user_set.remove(user)
        if grupo == "none":
            message = (
                "User " + user.username + " perdeu acesso às páginas de Receiving."
            )
            subject, from_email, to = (
                "Alteração em Receiving - Line Request - Configurations",
                "noreply@visteon.com",
                ["aroque1@visteon.com"],
            )
            msg = EmailMultiAlternatives(subject, message, from_email, to)
            msg.attach_alternative(message, "text/html")
            msg.send()
            return redirect("receiving:configurations")
        if grupo == "tpm":
            my_group = Group.objects.using("default").get(name="receivingTPM")
            my_group.user_set.add(user)
        if grupo == "lineRequest":
            my_group = Group.objects.using("default").get(name="receivingLINES")
            my_group.user_set.add(user)
        if grupo == "mnfgSupply":
            my_group = Group.objects.using("default").get(name="receivingMNFG")
            my_group.user_set.add(user)
        if grupo == "lineRequest/mnfgSupply":
            my_group = Group.objects.using("default").get(name="receivingMNFG")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="receivingLINES")
            my_group.user_set.add(user)
        if grupo == "lineRequest/tpm":
            my_group = Group.objects.using("default").get(name="receivingLINES")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="receivingTPM")
            my_group.user_set.add(user)
        if grupo == "mnfgSupply/tpm":
            my_group = Group.objects.using("default").get(name="receivingMNFG")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="receivingTPM")
            my_group.user_set.add(user)
        if grupo == "lineRequest/mnfgSupply/tpm":
            my_group = Group.objects.using("default").get(name="receivingMNFG")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="receivingLINES")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="receivingTPM")
            my_group.user_set.add(user)
        message = (
            "User "
            + user.username
            + " com páginas acessiveis - "
            + grupo.replace("/", " , ")
        )
        subject, from_email, to = (
            "Alteração em Receiving - Line Request - Configurations",
            "noreply@visteon.com",
            ["aroque1@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()
        return redirect("receiving:configurations")


def habilitarQuadrados(request):
    if request.method == "POST":
        message = "</br><b>Alterações de visibilidade </b></br></br>"
        if request.POST["1"] != "":
            pos = HabilitarQuadrados.objects.get(posicao="1")
            pos.valor = request.POST["1"]
            pos.save()
            message += (
                "Alterado estado visivel de Receções Físicas. </br>Visível? <b>"
                + pos.valor
                + "</b></br></br>"
            )
        if request.POST["2"] != "":
            pos = HabilitarQuadrados.objects.get(posicao="2")
            pos.valor = request.POST["2"]
            pos.save()
            message += (
                "Alterado estado visivel de Smart. </br>Visível? <b>"
                + pos.valor
                + "</b></br></br>"
            )
        if request.POST["3"] != "":
            pos = HabilitarQuadrados.objects.get(posicao="3")
            pos.valor = request.POST["3"]
            pos.save()
            message += (
                "Alterado estado visivel de Kardex.  </br>Visível? <b>"
                + pos.valor
                + "</b></br></br>"
            )
        if request.POST["4"] != "":
            pos = HabilitarQuadrados.objects.get(posicao="4")
            pos.valor = request.POST["4"]
            pos.save()
            message += (
                "Alterado estado visivel de Área A.  </br>Visível? <b>"
                + pos.valor
                + "</b></br></br>"
            )
        if request.POST["5"] != "":
            pos = HabilitarQuadrados.objects.get(posicao="5")
            pos.valor = request.POST["5"]
            pos.save()
            message += (
                "Alterado estado visivel de Área B.  </br>Visível? <b>"
                + pos.valor
                + "</b></br></br>"
            )
        if request.POST["6"] != "":
            pos = HabilitarQuadrados.objects.get(posicao="6")
            pos.valor = request.POST["6"]
            pos.save()
            message += (
                "Alterado estado visivel de Área B embalagens/Mecalux.  </br>Visível? <b>"
                + pos.valor
                + "</b></br></br>"
            )
        if request.POST["7"] != "":
            pos = HabilitarQuadrados.objects.get(posicao="7")
            pos.valor = request.POST["7"]
            pos.save()
            message += (
                "Alterado estado visivel de Empilhadores.  </br>Visível? <b>"
                + pos.valor
                + "</b></br></br>"
            )
        if request.POST["8"] != "":
            pos = HabilitarQuadrados.objects.get(posicao="8")
            pos.valor = request.POST["8"]
            pos.save()
            message += (
                "Alterado estado visivel de Doca.  </br>Visível? <b>"
                + pos.valor
                + "</b>"
            )
        subject, from_email, to = (
            "Alteração em Receiving - TPM - Configurations",
            "noreply@visteon.com",
            ["aroque1@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()
    return redirect("receiving:configurationsTPM")


def definirTempos(request):
    if request.method == "POST":
        elementos = DefinirTempos.objects
        message = "</br><b>Alterações de tempos </b></br></br>"
        elem1 = elementos.get(turno="1")
        elem2 = elementos.get(turno="2")
        elem4 = elementos.get(turno="4")
        if request.POST["inicio1"] != elem1.inicio:
            message += (
                "Alterado tempo inicio turno 1.</br>Antigo: <b>"
                + elem1.inicio
                + "h</b>. Novo: <b>"
                + request.POST["inicio1"]
                + "h</b></br></br>"
            )
            elem1.inicio = request.POST["inicio1"]
            elem1.save()
        if request.POST["final1"] != elem1.final:
            message += (
                "Alterado tempo final turno 1.</br>Antigo: <b>"
                + elem1.final
                + "h</b>. Novo: <b>"
                + request.POST["final1"]
                + "h</b></br></br>"
            )
            elem1.final = request.POST["final1"]
            elem1.save()
        if request.POST["inicio2"] != elem2.inicio:
            message += (
                "Alterado tempo inicio turno 2.</br>Antigo: <b>"
                + elem2.inicio
                + "h</b>. Novo: <b>"
                + request.POST["inicio2"]
                + "h</b></br></br>"
            )
            elem2.inicio = request.POST["inicio2"]
            elem2.save()
        if request.POST["final2"] != elem2.final:
            message += (
                "Alterado tempo final turno 2.</br>Antigo: <b>"
                + elem2.final
                + "h</b>. Novo: <b>"
                + request.POST["final2"]
                + "h</b></br></br>"
            )
            elem2.final = request.POST["final2"]
            elem2.save()
        if request.POST["inicio4"] != elem4.inicio:
            message += (
                "Alterado tempo inicio turno 4.</br>Antigo: <b>"
                + elem4.inicio
                + "h</b>. Novo: <b>"
                + request.POST["inicio4"]
                + "h</b></br></br>"
            )
            elem4.inicio = request.POST["inicio4"]
            elem4.save()
        if request.POST["final4"] != elem4.final:
            message += (
                "Alterado tempo final turno 4.</br>Antigo: <b>"
                + elem4.final
                + "h</b>. Novo: <b>"
                + request.POST["final4"]
                + "h</b>"
            )
            elem4.final = request.POST["final4"]
            elem4.save()

        subject, from_email, to = (
            "Alteração em Receiving - TPM - Configurations",
            "noreply@visteon.com",
            ["aroque1@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()
        return redirect("receiving:configurationsTPM")


def reAbrirICDR(request):
    if request.method == "POST":
        actualDay = datetime.today()
        actualDayString = actualDay.strftime("%Y-%m-%d")

        id = request.POST["id"]

        diaCorrente = datetime.now().strftime("%d/%m/%Y")
        horaCorrente = datetime.now().strftime("%H:%M:%S")

        icdr = ICDR.objects.get(id=id)
        elemDayString = icdr.aberturaICDR[0:10]
        contador = np.busday_count(elemDayString, actualDayString)
        icdr.ageing = contador
        icdr.date = ""
        comentarios = icdr.comentarioFechoICDR
        comentarios += (
            "\n\rICDR reaberto por - "
            + request.user.username
            + " - em "
            + diaCorrente
            + " às "
            + horaCorrente
        )
        icdr.comentarioFechoICDR = comentarios
        icdr.save()

        rctUnpCheck = ""
        cycleCountCheck = ""

        trigger = TriggerEnvioEmailsICDR.objects.get(nome="Reabertura")
        listTo = []

        for user in trigger.users.split(";"):
            if not user in listTo:
                if ListaUsersICDR.objects.filter(nome=user).exists():
                    lista = ListaUsersICDR.objects.get(nome=user)
                    for userListaBD in lista.user.split(";"):
                        if not userListaBD in listTo and not userListaBD == "":
                            listTo.append(userListaBD + "@visteon.com")
                else:
                    if not user == "":
                        listTo.append(user + "@visteon.com")

        if trigger.estado == "ativo":
            if icdr.rctUnpCheck == "false" or icdr.rctUnpCheck == "":
                rctUnpCheck = ""
            elif icdr.rctUnpCheck == "true":
                rctUnpCheck = "X"

            if icdr.cycleCountCheck == "false" or icdr.cycleCountCheck == "":
                cycleCountCheck = ""
            elif icdr.cycleCountCheck == "true":
                cycleCountCheck = "X"

            table = "<h3>User: <b>" + request.user.username + " </b></h3> "
            table += '</br><table class="display"><thead style="background-color: lightgray"><tr><th>DATA ABERTURA</th><th>AGEING (DIAS)</th><th>Nº/ANO</th><th>FORNECEDOR</th><th>PARTNUMBER</th><th>QT</th><th>MOTIVO</th><th>ALFANDEGA (S/N)</th><th>RESPONSÁVEL (NOME/DEPARTAMENTO)</th><th>COMENTÁRIOS (ABERTURA)</th><th>UN COST</th><th>TOTAL COST</th><th>RCT UNP</th><th>CYCLE COUNT</th><th>DATA FECHO</th><th>CYCLE COUNT</th><th>DATA CC</th><th>AUDIT CHECK</th></tr></thead><tbody>'
            table += (
                '<tr style="background-color: whitesmoke"><td style="padding:0 15px 0 15px;">'
                + icdr.aberturaICDR
                + '</td><td style="padding:0 15px 0 15px;">'
                + str(icdr.ageing)
                + '</td><td style="padding:0 15px 0 15px;">'
                + icdr.nAno
                + '</td><td style="padding:0 15px 0 15px;">'
                + icdr.fornecedor
                + '</td><td style="padding:0 15px 0 15px;">'
                + icdr.partnumber
                + '</td><td style="padding:0 15px 0 15px;">'
                + icdr.quantidade
                + '</td><td style="padding:0 15px 0 15px;">'
                + icdr.tipo
                + '</td><td style="padding:0 15px 0 15px;">'
                + icdr.simNao
                + '</td><td style="padding:0 15px 0 15px;">'
                + icdr.responsavel
                + "/"
                + icdr.departamento
                + '</td><td style="padding:0 15px 0 15px;">'
                + icdr.comentarioFecho
                + '</td><td style="padding:0 15px 0 15px;">'
                + icdr.unCost
                + '</td><td style="padding:0 15px 0 15px;">'
                + icdr.totalCost
                + '</td><td style="padding:0 15px 0 15px; text-align: center">'
                + rctUnpCheck
                + '</td><td style="padding:0 15px 0 15px; text-align: center">'
                + cycleCountCheck
                + '</td><td style="padding:0 15px 0 15px;">'
                + icdr.date
                + '</td><td style="padding:0 15px 0 15px;">'
                + icdr.cycleCount
                + '</td><td style="padding:0 15px 0 15px;">'
                + icdr.dataCycleCount
                + '</td><td style="padding:0 15px 0 15px;">'
                + icdr.auditCheck
                + "</td></tr>"
            )
            table += "</body></table>"

            subject, from_email, to = (
                "Reabertura de ICDR",
                "noreply@visteon.com",
                listTo,
            )
            msg = EmailMultiAlternatives(subject, table, from_email, to)
            msg.attach_alternative(table, "text/html")
            msg.send()

        return redirect("receiving:icdr")


def criarICDR(request):
    if request.method == "POST":
        numeroAno = request.POST["numeroAno"]
        fornecedor = request.POST["fornecedor"]
        partNumber = request.POST["partnumber"]
        quantidade = request.POST["quantidade"]
        tipo = request.POST["tipo"]
        alfandegaSimNao = request.POST["alfandegaSimNao"]
        responsavel = request.POST["responsavel"]
        departamento = request.POST["departamento"]
        comentario = request.POST["comentarios"]

        numeroICDR = numeroAno.split("/")
        numeroICDR = int(numeroICDR[0][1:], base=10) + 1

        ultimoICDR = ICDRultimoValor.objects.filter().first()
        if ultimoICDR.valor == numeroICDR - 1:
            ultimoICDR.valor = numeroICDR
            ultimoICDR.nome = (
                "D" + str(numeroICDR) + "/" + str(datetime.now().strftime("%Y"))
            )
            ultimoICDR.save()

        novoICDR = ICDR()
        novoICDR.aberturaICDR = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        novoICDR.ageing = "0"
        novoICDR.nAno = numeroAno
        novoICDR.fornecedor = fornecedor
        novoICDR.partnumber = partNumber
        novoICDR.quantidade = quantidade
        novoICDR.tipo = tipo
        novoICDR.simNao = alfandegaSimNao
        novoICDR.responsavel = responsavel
        novoICDR.departamento = departamento
        novoICDR.comentarioFecho = comentario
        novoICDR.unCost = ""
        novoICDR.totalCost = ""
        novoICDR.rctUnpCheck = ""
        novoICDR.cycleCountCheck = ""
        novoICDR.consumption = ""
        novoICDR.po = ""
        novoICDR.comentarioFechoICDR = ""
        novoICDR.date = ""
        novoICDR.cycleCount = ""
        novoICDR.dataCycleCount = ""
        novoICDR.auditCheck = ""
        novoICDR.save()

        rctUnpCheck = ""
        cycleCountCheck = ""

        trigger = TriggerEnvioEmailsICDR.objects.get(nome="Criação")
        listTo = []

        for user in trigger.users.split(";"):
            if not user in listTo:
                if ListaUsersICDR.objects.filter(nome=user).exists():
                    lista = ListaUsersICDR.objects.get(nome=user)
                    for userListaBD in lista.user.split(";"):
                        if not userListaBD in listTo and not userListaBD == "":
                            listTo.append(userListaBD + "@visteon.com")
                else:
                    if not user == "":
                        listTo.append(user + "@visteon.com")

        if trigger.estado == "ativo":
            if novoICDR.rctUnpCheck == "false" or novoICDR.rctUnpCheck == "":
                rctUnpCheck = ""
            elif novoICDR.rctUnpCheck == "true":
                rctUnpCheck = "X"

            if novoICDR.cycleCountCheck == "false" or novoICDR.cycleCountCheck == "":
                cycleCountCheck = ""
            elif novoICDR.cycleCountCheck == "true":
                cycleCountCheck = "X"

            table = "<h3>User: <b>" + request.user.username + " </b></h3> "
            table += '</br><table class="display"><thead style="background-color: lightgray"><tr><th>DATA ABERTURA</th><th>AGEING (DIAS)</th><th>Nº/ANO</th><th>FORNECEDOR</th><th>PARTNUMBER</th><th>QT</th><th>MOTIVO</th><th>ALFANDEGA (S/N)</th><th>RESPONSÁVEL (NOME/DEPARTAMENTO)</th><th>COMENTÁRIOS (ABERTURA)</th><th>UN COST</th><th>TOTAL COST</th><th>RCT UNP</th><th>CYCLE COUNT</th><th>DATA FECHO</th><th>CYCLE COUNT</th><th>DATA CC</th><th>AUDIT CHECK</th></tr></thead><tbody>'
            table += (
                '<tr style="background-color: whitesmoke"><td style="padding:0 15px 0 15px;">'
                + novoICDR.aberturaICDR
                + '</td><td style="padding:0 15px 0 15px;">'
                + str(novoICDR.ageing)
                + '</td><td style="padding:0 15px 0 15px;">'
                + novoICDR.nAno
                + '</td><td style="padding:0 15px 0 15px;">'
                + novoICDR.fornecedor
                + '</td><td style="padding:0 15px 0 15px;">'
                + novoICDR.partnumber
                + '</td><td style="padding:0 15px 0 15px;">'
                + novoICDR.quantidade
                + '</td><td style="padding:0 15px 0 15px;">'
                + novoICDR.tipo
                + '</td><td style="padding:0 15px 0 15px;">'
                + novoICDR.simNao
                + '</td><td style="padding:0 15px 0 15px;">'
                + novoICDR.responsavel
                + "/"
                + novoICDR.departamento
                + '</td><td style="padding:0 15px 0 15px;">'
                + novoICDR.comentarioFecho
                + '</td><td style="padding:0 15px 0 15px;">'
                + novoICDR.unCost
                + '</td><td style="padding:0 15px 0 15px;">'
                + novoICDR.totalCost
                + '</td><td style="padding:0 15px 0 15px; text-align: center">'
                + rctUnpCheck
                + '</td><td style="padding:0 15px 0 15px; text-align: center">'
                + cycleCountCheck
                + '</td><td style="padding:0 15px 0 15px;">'
                + novoICDR.date
                + '</td><td style="padding:0 15px 0 15px;">'
                + novoICDR.cycleCount
                + '</td><td style="padding:0 15px 0 15px;">'
                + novoICDR.dataCycleCount
                + '</td><td style="padding:0 15px 0 15px;">'
                + novoICDR.auditCheck
                + "</td></tr>"
            )
            table += "</body></table>"

            subject, from_email, to = "Novo ICDR", "noreply@visteon.com", listTo
            msg = EmailMultiAlternatives(subject, table, from_email, to)
            msg.attach_alternative(table, "text/html")
            msg.send()

    return redirect("receiving:icdr")


def getDepartamento(request):
    if request.method == "GET":
        responsavel = request.GET["responsavel"]
        elemento = list(UserICDR.objects.filter(username=responsavel).values())
        return JsonResponse({"elemento": elemento})


def getUtilizadoresPorDepartamento(request):
    if request.method == "GET":
        departamento = request.GET["departamento"]
        elementos = list(UserICDR.objects.filter(area=departamento).values())
        return JsonResponse({"elementos": elementos})


def searchAllInfoUtilizadores(request):
    if request.method == "GET":
        resposta = []
        todos = UserICDR.objects.all()
        for elem in todos:
            row = {
                "username": elem.username,
                "nome": elem.nome,
                "area": elem.area,
                "email": elem.email,
            }
            resposta.append(row)
        return JsonResponse({"resposta": resposta})


def changeUserGroupsICDR(request):
    if request.method == "POST":
        user = User.objects.get(username=request.POST["username"])
        grupo = request.POST["paginas"]
        if User.objects.filter(
            username=request.POST["username"], groups__name="ICDR - read only"
        ):
            my_group = Group.objects.using("default").get(name="ICDR - read only")
            my_group.user_set.remove(user)
        if User.objects.filter(
            username=request.POST["username"], groups__name="ICDR - tipo1"
        ):
            my_group = Group.objects.using("default").get(name="ICDR - tipo1")
            my_group.user_set.remove(user)
        if User.objects.filter(
            username=request.POST["username"], groups__name="ICDR - tipo2"
        ):
            my_group = Group.objects.using("default").get(name="ICDR - tipo2")
            my_group.user_set.remove(user)
        if User.objects.filter(
            username=request.POST["username"], groups__name="ICDR - tipo3"
        ):
            my_group = Group.objects.using("default").get(name="ICDR - tipo3")
            my_group.user_set.remove(user)
        if grupo == "none":
            # message = 'User ' + user.username + ' perdeu acesso às páginas de Shipping.'
            # subject, from_email, to = 'Alteração em Receiving - Line Request - Configurations', 'noreply@visteon.com', [
            #     'aroque1@visteon.com']
            # msg = EmailMultiAlternatives(subject, message, from_email, to)
            # msg.attach_alternative(message, "text/html")
            # msg.send()
            return redirect("shippers:configurations")
        if grupo == "readOnly":
            my_group = Group.objects.using("default").get(name="ICDR - read only")
            my_group.user_set.add(user)
        if grupo == "tipo1":
            my_group = Group.objects.using("default").get(name="ICDR - tipo1")
            my_group.user_set.add(user)
        if grupo == "tipo2":
            my_group = Group.objects.using("default").get(name="ICDR - tipo2")
            my_group.user_set.add(user)
        if grupo == "tipo3":
            my_group = Group.objects.using("default").get(name="ICDR - tipo3")
            my_group.user_set.add(user)

        if grupo == "tipo1/tipo2":
            my_group = Group.objects.using("default").get(name="ICDR - tipo1")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="ICDR - tipo2")
            my_group.user_set.add(user)
        if grupo == "tipo1/tipo3":
            my_group = Group.objects.using("default").get(name="ICDR - tipo1")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="ICDR - tipo3")
            my_group.user_set.add(user)
        if grupo == "tipo2/tipo3":
            my_group = Group.objects.using("default").get(name="ICDR - tipo2")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="ICDR - tipo3")
            my_group.user_set.add(user)
        if grupo == "tipo1/tipo2/tipo3":
            my_group = Group.objects.using("default").get(name="ICDR - tipo1")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="ICDR - tipo2")
            my_group.user_set.add(user)
            my_group = Group.objects.using("default").get(name="ICDR - tipo3")
            my_group.user_set.add(user)
        return redirect("receiving:configurationsICDR")
        # message = 'User ' + user.username + ' com páginas acessiveis - ' + grupo.replace("/", " , ")
        # subject, from_email, to = 'Alteração em Shipping - Configurations', 'noreply@visteon.com', [
        #     'aroque1@visteon.com']
        # msg = EmailMultiAlternatives(subject, message, from_email, to)
        # msg.attach_alternative(message, "text/html")
        # msg.send()


def setDataHoraFechoICDR(request):
    if request.method == "POST":
        id = request.POST["id"]
        elem = ICDR.objects.get(id=id)
        elem.date = datetime.today().strftime("%Y-%m-%d %H:%M")
        elem.ageing = "-"
        elem.save()

        rctUnpCheck = ""
        cycleCountCheck = ""

        trigger = TriggerEnvioEmailsICDR.objects.get(nome="Fecho")
        listTo = []

        for user in trigger.users.split(";"):
            if not user in listTo:
                if ListaUsersICDR.objects.filter(nome=user).exists():
                    lista = ListaUsersICDR.objects.get(nome=user)
                    for userListaBD in lista.user.split(";"):
                        if not userListaBD in listTo and not userListaBD == "":
                            listTo.append(userListaBD + "@visteon.com")
                else:
                    if not user == "":
                        listTo.append(user + "@visteon.com")

        if trigger.estado == "ativo":

            if elem.rctUnpCheck == "false" or elem.rctUnpCheck == "":
                rctUnpCheck = ""
            elif elem.rctUnpCheck == "true":
                rctUnpCheck = "X"

            if elem.cycleCountCheck == "false" or elem.cycleCountCheck == "":
                cycleCountCheck = ""
            elif elem.cycleCountCheck == "true":
                cycleCountCheck = "X"

            trigger = TriggerEnvioEmailsICDR.objects.get(nome="Fecho")
            if trigger.estado == "ativo":
                table = "<h3>User: <b>" + request.user.username + " </b></h3> "
                table += '</br><table class="display"><thead style="background-color: lightgray"><tr><th>DATA ABERTURA</th><th>AGEING (DIAS)</th><th>Nº/ANO</th><th>FORNECEDOR</th><th>PARTNUMBER</th><th>QT</th><th>MOTIVO</th><th>ALFANDEGA (S/N)</th><th>RESPONSÁVEL (NOME/DEPARTAMENTO)</th><th>COMENTÁRIOS (ABERTURA)</th><th>UN COST</th><th>TOTAL COST</th><th>RCT UNP</th><th>CYCLE COUNT</th><th>DATA FECHO</th><th>CYCLE COUNT</th><th>DATA CC</th><th>AUDIT CHECK</th></tr></thead><tbody>'
                table += (
                    '<tr style="background-color: whitesmoke"><td style="padding:0 15px 0 15px;">'
                    + elem.aberturaICDR
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + str(elem.ageing)
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.nAno
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.fornecedor
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.partnumber
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.quantidade
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.tipo
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.simNao
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.responsavel
                    + "/"
                    + elem.departamento
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.comentarioFecho
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.unCost
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.totalCost
                    + '</td><td style="padding:0 15px 0 15px; text-align: center">'
                    + rctUnpCheck
                    + '</td><td style="padding:0 15px 0 15px; text-align: center">'
                    + cycleCountCheck
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.date
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.cycleCount
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.dataCycleCount
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.auditCheck
                    + "</td></tr>"
                )
                table += "</body></table>"

                subject, from_email, to = "Fecho de ICDR", "noreply@visteon.com", listTo
                msg = EmailMultiAlternatives(subject, table, from_email, to)
                msg.attach_alternative(table, "text/html")
                msg.send()
        return redirect("receiving:icdr")


def updateICDR(request):
    if request.method == "POST":
        id = request.POST["id"]
        poNumber = ""
        cycleCount = ""
        dataCycleCount = ""
        auditCheck = ""
        checkedCycleCount = request.POST["checkedCycleCount"]
        checkedRctUnp = request.POST["checkedRctUnp"]

        if request.POST["poNumber"] != "":
            poNumber = request.POST["poNumber"]
        if request.POST["cycleCount"] != "":
            cycleCount = request.POST["cycleCount"]
        if request.POST["dataCycleCount"] != "":
            dataCycleCount = request.POST["dataCycleCount"]
        if request.POST["auditCheck"] != "":
            auditCheck = request.POST["auditCheck"]

        elem = ICDR.objects.get(id=id)
        if poNumber != "":
            elem.po = poNumber
        if cycleCount != "":
            elem.cycleCount = cycleCount
        if dataCycleCount != "":
            elem.dataCycleCount = dataCycleCount
        if auditCheck != "":
            elem.auditCheck = auditCheck
        elem.cycleCountCheck = checkedCycleCount
        elem.rctUnpCheck = checkedRctUnp
        elem.save()
        return redirect("receiving:icdr")


def getElem(request):
    if request.method == "GET":
        id = request.GET["id"]
        atributo = request.GET["atributo"]
        elem = ICDR.objects.get(id=id)

        if atributo == "consumption":
            return JsonResponse({"response": elem.consumption})
        if atributo == "poNumber":
            return JsonResponse({"response": elem.po})
        if atributo == "comentariosFecho":
            return JsonResponse({"response": elem.comentarioFechoICDR})


def updateConsumption(request):
    if request.method == "POST":
        id = request.POST["openICDRElemID"]
        comentario = request.POST["novoOpenICDR"]
        diaCorrente = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")

        elem = ICDR.objects.get(id=id)
        comentarioAnterior = elem.consumption
        comentarioNovo = (
            comentarioAnterior
            + "\n\r- "
            + str(request.user.username)
            + ", dia "
            + diaCorrente
            + ": "
            + "\n"
            + comentario
        )
        elem.consumption = comentarioNovo
        elem.save()
        return redirect("receiving:icdr")


def updatePONumber(request):
    if request.method == "POST":
        id = request.POST["poNumberElemID"]
        comentario = request.POST["novoQADEntry"]
        diaCorrente = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")

        elem = ICDR.objects.get(id=id)
        comentarioAnterior = elem.po
        comentarioNovo = (
            comentarioAnterior
            + "\n\r- "
            + str(request.user.username)
            + ", dia "
            + diaCorrente
            + ": "
            + ": "
            + "\n"
            + comentario
        )
        elem.po = comentarioNovo
        elem.save()
        return redirect("receiving:icdr")


def updateComentarioFechoICDR(request):
    if request.method == "POST":
        id = request.POST["comentarioFechoElemID"]
        comentario = request.POST["novoComentarioFechoICDR"]
        diaCorrente = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")

        elem = ICDR.objects.get(id=id)
        comentarioAnterior = elem.comentarioFechoICDR
        comentarioNovo = (
            comentarioAnterior
            + "\n\r- "
            + str(request.user.username)
            + ", dia "
            + diaCorrente
            + ": "
            + "\n"
            + comentario
        )
        elem.comentarioFechoICDR = comentarioNovo
        elem.save()
        return redirect("receiving:icdr")


def mudaEstadoFiltroICDR(request):
    if request.method == "POST":
        id = ""
        estado = ""
        elemento = ""

        if "idConfirmarCC" in request.POST:
            id = request.POST["idConfirmarCC"]
        elif "idRetirarCC" in request.POST:
            id = request.POST["idRetirarCC"]
        else:
            id = request.POST["id"]

        if "estadoConfirmarCC" in request.POST:
            estado = request.POST["estadoConfirmarCC"]
        elif "estadoRetirarCC" in request.POST:
            estado = request.POST["estadoRetirarCC"]
        else:
            estado = request.POST["estado"]

        if "elementoConfirmarCC" in request.POST:
            elemento = request.POST["elementoConfirmarCC"]
        elif "elementoRetirarCC" in request.POST:
            elemento = request.POST["elementoRetirarCC"]
        else:
            elemento = request.POST["elemento"]

        elem = ICDR.objects.get(id=id)
        if elemento == "cycle":
            elem.cycleCountCheck = estado
            if elem.cycleCountCheck == "true":
                rctUnpCheck = ""
                cycleCountCheck = ""

                trigger = TriggerEnvioEmailsICDR.objects.get(nome="Check_Cycle_Count")
                listTo = []

                for user in trigger.users.split(";"):
                    if not user in listTo:
                        if ListaUsersICDR.objects.filter(nome=user).exists():
                            lista = ListaUsersICDR.objects.get(nome=user)
                            for userListaBD in lista.user.split(";"):
                                if not userListaBD in listTo and not userListaBD == "":
                                    listTo.append(userListaBD + "@visteon.com")
                        else:
                            if not user == "":
                                listTo.append(user + "@visteon.com")

                if trigger.estado == "ativo":
                    if elem.rctUnpCheck == "false" or elem.rctUnpCheck == "":
                        rctUnpCheck = ""
                    elif elem.rctUnpCheck == "true":
                        rctUnpCheck = "X"

                    if elem.cycleCountCheck == "false" or elem.cycleCountCheck == "":
                        cycleCountCheck = ""
                    elif elem.cycleCountCheck == "true":
                        cycleCountCheck = "X"

                    table = "<h3>User: <b>" + request.user.username + " </b></h3> "
                    table += '</br><table class="display"><thead style="background-color: lightgray"><tr><th>DATA ABERTURA</th><th>AGEING (DIAS)</th><th>Nº/ANO</th><th>FORNECEDOR</th><th>PARTNUMBER</th><th>QT</th><th>MOTIVO</th><th>ALFANDEGA (S/N)</th><th>RESPONSÁVEL (NOME/DEPARTAMENTO)</th><th>COMENTÁRIOS (ABERTURA)</th><th>UN COST</th><th>TOTAL COST</th><th>RCT UNP</th><th>CYCLE COUNT</th><th>DATA FECHO</th><th>CYCLE COUNT</th><th>DATA CC</th><th>AUDIT CHECK</th></tr></thead><tbody>'
                    table += (
                        '<tr style="background-color: whitesmoke"><td style="padding:0 15px 0 15px;">'
                        + elem.aberturaICDR
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + str(elem.ageing)
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.nAno
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.fornecedor
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.partnumber
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.quantidade
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.tipo
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.simNao
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.responsavel
                        + "/"
                        + elem.departamento
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.comentarioFecho
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.unCost
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.totalCost
                        + '</td><td style="padding:0 15px 0 15px; text-align: center">'
                        + rctUnpCheck
                        + '</td><td style="padding:0 15px 0 15px; text-align: center">'
                        + cycleCountCheck
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.date
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.cycleCount
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.dataCycleCount
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.auditCheck
                        + "</td></tr>"
                    )
                    table += '<tr style="background-color: lightgray"><td colspan="18"> </td></tr>'
                    table += "</body></table>"

                    subject, from_email, to = (
                        "Alteração de Cycle Count - ICDR",
                        "noreply@visteon.com",
                        listTo,
                    )
                    msg = EmailMultiAlternatives(subject, table, from_email, to)
                    msg.attach_alternative(table, "text/html")
                    msg.send()
            elif elem.cycleCountCheck == "false":
                rctUnpCheck = ""
                cycleCountCheck = ""

                trigger = TriggerEnvioEmailsICDR.objects.get(nome="Check_Cycle_Count")
                listTo = []

                for user in trigger.users.split(";"):
                    if not user in listTo:
                        if ListaUsersICDR.objects.filter(nome=user).exists():
                            lista = ListaUsersICDR.objects.get(nome=user)
                            for userListaBD in lista.user.split(";"):
                                if not userListaBD in listTo and not userListaBD == "":
                                    listTo.append(userListaBD + "@visteon.com")
                        else:
                            if not user == "":
                                listTo.append(user + "@visteon.com")

                if trigger.estado == "ativo":
                    if elem.rctUnpCheck == "false" or elem.rctUnpCheck == "":
                        rctUnpCheck = ""
                    elif elem.rctUnpCheck == "true":
                        rctUnpCheck = "X"

                    if elem.cycleCountCheck == "false" or elem.cycleCountCheck == "":
                        cycleCountCheck = ""
                    elif elem.cycleCountCheck == "true":
                        cycleCountCheck = "X"

                    table = "<h3>User: <b>" + request.user.username + " </b></h3> "
                    table += '</br><table class="display"><thead style="background-color: lightgray"><tr><th>DATA ABERTURA</th><th>AGEING (DIAS)</th><th>Nº/ANO</th><th>FORNECEDOR</th><th>PARTNUMBER</th><th>QT</th><th>MOTIVO</th><th>ALFANDEGA (S/N)</th><th>RESPONSÁVEL (NOME/DEPARTAMENTO)</th><th>COMENTÁRIOS (ABERTURA)</th><th>UN COST</th><th>TOTAL COST</th><th>RCT UNP</th><th>CYCLE COUNT</th><th>DATA FECHO</th><th>CYCLE COUNT</th><th>DATA CC</th><th>AUDIT CHECK</th></tr></thead><tbody>'
                    table += (
                        '<tr style="background-color: whitesmoke"><td style="padding:0 15px 0 15px;">'
                        + elem.aberturaICDR
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + str(elem.ageing)
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.nAno
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.fornecedor
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.partnumber
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.quantidade
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.tipo
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.simNao
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.responsavel
                        + "/"
                        + elem.departamento
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.comentarioFecho
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.unCost
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.totalCost
                        + '</td><td style="padding:0 15px 0 15px; text-align: center">'
                        + rctUnpCheck
                        + '</td><td style="padding:0 15px 0 15px; text-align: center">'
                        + cycleCountCheck
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.date
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.cycleCount
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.dataCycleCount
                        + '</td><td style="padding:0 15px 0 15px;">'
                        + elem.auditCheck
                        + "</td></tr>"
                    )
                    table += '<tr style="background-color: lightgray"><td colspan="18"> </td></tr>'
                    table += "</body></table>"

                    subject, from_email, to = (
                        "Alteração de Cycle Count - ICDR",
                        "noreply@visteon.com",
                        listTo,
                    )
                    msg = EmailMultiAlternatives(subject, table, from_email, to)
                    msg.attach_alternative(table, "text/html")
                    msg.send()
        if elemento == "rct":
            elem.rctUnpCheck = estado
        elem.save()
        return redirect("receiving:icdr")


def downloadExcel(request):
    if request.method == "GET":
        elementos = ICDR.objects

        caminho = "C:/visteon/media/receiving/icdr"
        if os.path.exists(caminho):
            for entry in os.listdir(caminho):
                if os.path.isfile(os.path.join(caminho, entry)):
                    os.remove(caminho + "/" + entry)

        wbProduction = Workbook()
        sheetProduction = wbProduction.add_sheet("Sheet 1")

        row = 0
        col = 0
        sheetProduction.write(row, col, "Data abertura")
        sheetProduction.write(row, col + 1, "Ageing (dias)")
        sheetProduction.write(row, col + 2, "Nº/Ano")
        sheetProduction.write(row, col + 3, "Fornecedor")
        sheetProduction.write(row, col + 4, "Partnumber")
        sheetProduction.write(row, col + 5, "Quantidade")
        sheetProduction.write(row, col + 6, "Motivo")
        sheetProduction.write(row, col + 7, "Alfandega")
        sheetProduction.write(row, col + 8, "Responsável")
        sheetProduction.write(row, col + 9, "Departamento")
        sheetProduction.write(row, col + 10, "Comentários (abertura)")
        sheetProduction.write(row, col + 11, "Un cost")
        sheetProduction.write(row, col + 12, "Total cost")
        sheetProduction.write(row, col + 13, "RCT UNP")
        sheetProduction.write(row, col + 14, "Cycle count")
        sheetProduction.write(row, col + 15, "Consumo")
        sheetProduction.write(row, col + 16, "QAD (PO nº)")
        sheetProduction.write(row, col + 17, "Comentários")
        sheetProduction.write(row, col + 18, "Data fecho")
        sheetProduction.write(row, col + 19, "Cycle count")
        sheetProduction.write(row, col + 20, "Data cc")
        sheetProduction.write(row, col + 21, "Audit check")
        row += 1

        for elem in elementos.all():
            sheetProduction.write(row, col, elem.aberturaICDR)
            sheetProduction.write(row, col + 1, elem.ageing)
            sheetProduction.write(row, col + 2, elem.nAno)
            sheetProduction.write(row, col + 3, elem.fornecedor)
            sheetProduction.write(row, col + 4, elem.partnumber)
            sheetProduction.write(row, col + 5, elem.quantidade)
            sheetProduction.write(row, col + 6, elem.tipo)
            sheetProduction.write(row, col + 7, elem.simNao)
            sheetProduction.write(row, col + 8, elem.responsavel)
            sheetProduction.write(row, col + 9, elem.departamento)
            sheetProduction.write(row, col + 10, elem.comentarioFecho)
            sheetProduction.write(row, col + 11, elem.unCost)
            sheetProduction.write(row, col + 12, elem.totalCost)
            sheetProduction.write(row, col + 13, elem.rctUnpCheck)
            sheetProduction.write(row, col + 14, elem.cycleCountCheck)
            sheetProduction.write(row, col + 15, elem.consumption)
            sheetProduction.write(row, col + 16, elem.po)
            sheetProduction.write(row, col + 17, elem.comentarioFechoICDR)
            sheetProduction.write(row, col + 18, elem.date)
            sheetProduction.write(row, col + 19, elem.cycleCount)
            sheetProduction.write(row, col + 20, elem.dataCycleCount)
            sheetProduction.write(row, col + 21, elem.auditCheck)
            row += 1
        wbProduction.save("C:\\visteon\\media\\receiving\\icdr\\workbookICDR.xls")

        return redirect("receiving:icdr")


def mudaEstadoSession(request):
    if request.method == "POST":
        estado = request.POST["estado"]

        if estado == "on":
            request.session["filtroDesativado"] = "filtroDesativado"
        else:
            del request.session["filtroDesativado"]

        return redirect("receiving:icdr")


def uploadDataICDR(request):
    if request.method == "POST":
        if request.FILES.get("ficheiro"):

            ficheiro = [request.FILES["ficheiro"]]

            workbook = openpyxl.load_workbook(ficheiro[0])
            worksheet = workbook["Sheet 1"]

            for element in worksheet:
                if element[0].value != None and element[0].value != "Data Abertura":
                    novoElemento = ICDR(
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
                    novoElemento.save()

        return redirect("receiving:icdr")


def uploadDataLineRequest(request):
    if request.method == "POST":
        if request.FILES.get("ficheiro"):

            ficheiro = [request.FILES["ficheiro"]]

            workbook = openpyxl.load_workbook(ficheiro[0])
            worksheet = workbook["Sheet1"]

            for element in worksheet:
                if element[0].value != None and element[0].value != "Request Date":
                    novoElemento = LineRequestFinished(
                        None,
                        element[0].value,
                        element[1].value,
                        element[2].value,
                        element[3].value,
                        element[4].value,
                        element[5].value,
                        element[6].value,
                    )
                    novoElemento.save()

        return redirect("receiving:lineRequest")


def criarUserICDR(request):
    if request.method == "POST":
        nome = request.POST["nomeUser"]
        area = request.POST["areaUser"]
        email = request.POST["emailUser"]
        username = email.split("@")[0]

        novoUser = UserICDR(None, username, nome, area, email)
        novoUser.save()

        if "_configurations" in request.POST:
            return redirect("receiving:configurationsICDR")
        return redirect("receiving:icdr")


def criarListaUsersICDR(request):
    if request.method == "POST":
        nomeLista = request.POST["nomeListaUser"]
        users = request.POST.getlist("listaDeUsers")
        novoUserLista = ""

        novaLista = ListaUsersICDR()
        novaLista.nome = nomeLista
        for user in users:
            novoUserLista += ";" + user
        novaLista.user = novoUserLista
        novaLista.save()
        return redirect("receiving:configurationsICDR")


def removerUtilizadorICDR(request):
    if request.method == "POST":
        username = request.POST["utilizador"]

        UserICDR.objects.get(username=username).delete()

        return redirect("receiving:configurationsICDR")


def adicionarUtilizadorListaICDR(request):
    if request.method == "POST":
        lista = ListaUsersICDR.objects.get(nome=request.POST["lista_adicionar"])
        users = request.POST.getlist("listaDeUsersDisponiveis")

        novoUserLista = ""
        if lista.user != None:
            novoUserLista = lista.user

        for user in users:
            novoUserLista += ";" + user

        lista.user = novoUserLista
        lista.save()
        return redirect("receiving:configurationsICDR")


def removerUtilizadorListaICDR(request):
    if request.method == "POST":
        nomeLista = ListaUsersICDR.objects.get(nome=request.POST["lista_remover"])
        users = request.POST.getlist("listaDeUsersRemover")

        novaStringUsers = ""

        lista = ListaUsersICDR.objects.get(nome=nomeLista)
        for elem in lista.user.split(";"):
            if not elem in users:
                novaStringUsers += ";" + elem
        novaStringUsers = novaStringUsers.replace(";;", "")
        lista.user = novaStringUsers
        lista.save()
        return redirect("receiving:configurationsICDR")


def alterarEstadoTriggerICDR(request):
    if request.method == "POST":
        trigger = request.POST["triggers"]
        nome = trigger.split("-")[0]
        estado = trigger.split("-")[1]

        triggerBD = TriggerEnvioEmailsICDR.objects.get(nome=nome)
        if estado == "ativo":
            triggerBD.estado = "inativo"
        elif estado == "inativo":
            triggerBD.estado = "ativo"
        triggerBD.save()

        return redirect("receiving:configurationsICDR")


def adicionarListaAlertaICDR(request):
    if request.method == "POST":
        trigger = request.POST["listaAlerta_adicionar"]
        listas = request.POST.getlist("listaEscolhidaAlerta")

        users = ""
        alerta = TriggerEnvioEmailsICDR.objects.get(nome=trigger)
        if alerta.users != None:
            users = alerta.users

        for user in listas:
            if not user in users:
                users += ";" + user
        users = users.replace(";;", "")
        alerta.users = users
        alerta.save()
        return redirect("receiving:configurationsICDR")


def removerListaAlertaICDR(request):
    if request.method == "POST":
        trigger = request.POST["listaAlerta_remover"]
        listas = request.POST.getlist("listaEscolhidaAlertaRemover")

        alerta = TriggerEnvioEmailsICDR.objects.get(nome=trigger)
        novaLista = ""

        for listaBD in alerta.users.split(";"):
            if not listaBD in listas:
                novaLista += ";" + listaBD
        novaLista = novaLista.replace(";;", "")
        alerta.users = novaLista
        alerta.save()
        return redirect("receiving:configurationsICDR")


def searchUsersPorLista(request):
    if request.method == "GET":
        lista = request.GET["lista"]
        listaResposta = []
        elementoLista = ""
        elementosRestantesLista = ""
        usersBD = UserICDR.objects

        if lista == "":
            for utilizador in usersBD.all():
                if utilizador.username != None:
                    elementoLista += ";" + utilizador.username
        else:
            listaBD = ListaUsersICDR.objects.get(nome=lista)
            elementoLista = listaBD.user
        listaResposta.append(elementoLista)

        if "utilizadoresRestantes" in request.GET:
            if lista == "":
                for utilizador in usersBD.all():
                    if utilizador.username != None:
                        elementosRestantesLista += ";" + utilizador.username
            else:
                listaBD = ListaUsersICDR.objects.filter(nome=lista).values_list(
                    "user", flat=True
                )
                if listaBD[0] != None:
                    elementosRestantes = listaBD[0].split(";")
                    for utilizador in usersBD.all():
                        if utilizador.username != None:
                            if not (utilizador.username in elementoLista) and not (
                                utilizador.username in elementosRestantesLista
                            ):
                                elementosRestantesLista += ";" + utilizador.username
                else:
                    for utilizador in usersBD.all():
                        elementosRestantesLista += ";" + utilizador.username
                listaResposta.append(elementosRestantesLista)

        return JsonResponse({"listaResposta": listaResposta}, safe=False)


def searchListasPorAlerta(request):
    if request.method == "GET":
        usersBD = UserICDR.objects
        listasBD = ListaUsersICDR.objects

        alerta = request.GET["alerta"]
        listaResposta = []
        elementoLista = ""

        if alerta == "":
            for lista in listasBD.all():
                elementoLista += ";" + lista.nome
            for utilizador in usersBD.all():
                elementoLista += ";" + utilizador.username
        else:
            alerta = TriggerEnvioEmailsICDR.objects.get(nome=alerta)
            elementoLista = alerta.users
        listaResposta.append(elementoLista)
        return JsonResponse({"listaResposta": listaResposta}, safe=False)


def reportICDR(request):
    if request.method == "POST":
        texto = request.POST["reportICDR"].replace("\n", "</br>")

        message = "<b>Report criado pelo User: " + request.user.username + "</b>"
        message += "</br></br>" + texto
        subject, from_email, to = (
            "Novo report na página Receiving -  ICDR",
            "noreply@visteon.com",
            ["aroque1@visteon.com", "npires2@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()
        return redirect("receiving:icdr")


def reportLineRequest(request):
    if request.method == "POST":
        texto = request.POST["reportICDR"].replace("\n", "</br>")

        message = "<b>Report criado pelo User: " + request.user.username + "</b>"
        message += "</br></br>" + texto
        subject, from_email, to = (
            "Novo report na página Receiving - Line Request",
            "noreply@visteon.com",
            ["aroque1@visteon.com", "npires2@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()
        return redirect("receiving:lineRequest")


def reportMNFGSupply(request):
    if request.method == "POST":
        texto = request.POST["reportICDR"].replace("\n", "</br>")

        message = "<b>Report criado pelo User: " + request.user.username + "</b>"
        message += "</br></br>" + texto
        subject, from_email, to = (
            "Novo report na página Receiving - MNFG Supply",
            "noreply@visteon.com",
            ["aroque1@visteon.com", "npires2@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()
        return redirect("receiving:mnfgSupply")


def reportTPM(request):
    if request.method == "POST":
        texto = request.POST["reportICDR"].replace("\n", "</br>")

        message = "<b>Report criado pelo User: " + request.user.username + "</b>"
        message += "</br></br>" + texto
        subject, from_email, to = (
            "Novo report na página Receiving - TPM",
            "noreply@visteon.com",
            ["aroque1@visteon.com", "npires2@visteon.com"],
        )
        msg = EmailMultiAlternatives(subject, message, from_email, to)
        msg.attach_alternative(message, "text/html")
        msg.send()
        return redirect("receiving:tpm")


def atualizarAgeing():
    elementosICDR = ICDR.objects
    actualDay = datetime.today()
    actualDayString = actualDay.strftime("%Y-%m-%d")

    if actualDay.strftime("%A") != "Saturday" and actualDay.strftime("%A") != "Sunday":
        for elem in elementosICDR.all():
            if elem.ageing != "-":
                elemDayString = elem.aberturaICDR[0:10]
                contador = np.busday_count(elemDayString, actualDayString)
                elem.ageing = contador
            elem.save()


def enviarEmailsICDR():
    elementosICDR = ICDR.objects

    for elem in elementosICDR.all():
        trigger = TriggerEnvioEmailsICDR.objects.get(nome="24H")
        listTo = []

        for user in trigger.users.split(";"):
            if not user in listTo:
                if ListaUsersICDR.objects.filter(nome=user).exists():
                    lista = ListaUsersICDR.objects.get(nome=user)
                    for userListaBD in lista.user.split(";"):
                        if not userListaBD in listTo and not userListaBD == "":
                            listTo.append(userListaBD + "@visteon.com")
                else:
                    if not user == "":
                        listTo.append(user + "@visteon.com")

        if trigger.estado == "ativo":
            if elem.ageing == "1":
                rctUnpCheck = ""
                cycleCountCheck = ""
                if elem.rctUnpCheck == "false" or elem.rctUnpCheck == "":
                    rctUnpCheck = ""
                elif elem.rctUnpCheck == "true":
                    rctUnpCheck = "X"

                if elem.cycleCountCheck == "false" or elem.cycleCountCheck == "":
                    cycleCountCheck = ""
                elif elem.cycleCountCheck == "true":
                    cycleCountCheck = "X"

                table = '</br><table class="display"><thead style="background-color: lightgray"><tr><th>DATA ABERTURA</th><th>AGEING (DIAS)</th><th>Nº/ANO</th><th>FORNECEDOR</th><th>PARTNUMBER</th><th>QT</th><th>MOTIVO</th><th>ALFANDEGA (S/N)</th><th>RESPONSÁVEL (NOME/DEPARTAMENTO)</th><th>COMENTÁRIOS (ABERTURA)</th><th>UN COST</th><th>TOTAL COST</th><th>RCT UNP</th><th>CYCLE COUNT</th><th>DATA FECHO</th><th>CYCLE COUNT</th><th>DATA CC</th><th>AUDIT CHECK</th></tr></thead><tbody>'
                table += (
                    '<tr style="background-color: whitesmoke"><td style="padding:0 15px 0 15px;">'
                    + elem.aberturaICDR
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + str(elem.ageing)
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.nAno
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.fornecedor
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.partnumber
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.quantidade
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.tipo
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.simNao
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.responsavel
                    + "/"
                    + elem.departamento
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.comentarioFecho
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.unCost
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.totalCost
                    + '</td><td style="padding:0 15px 0 15px; text-align: center">'
                    + rctUnpCheck
                    + '</td><td style="padding:0 15px 0 15px; text-align: center">'
                    + cycleCountCheck
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.date
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.cycleCount
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.dataCycleCount
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.auditCheck
                    + "</td></tr>"
                )
                table += '<tr style="background-color: lightgray"><td colspan="18"> </td></tr>'
                table += "</body></table>"

                subject, from_email, to = "Report ICDR", "noreply@visteon.com", listTo
                msg = EmailMultiAlternatives(subject, table, from_email, to)
                msg.attach_alternative(table, "text/html")
                msg.send()

        trigger2 = TriggerEnvioEmailsICDR.objects.get(nome="+48H")
        listTo2 = []

        for user in trigger2.users.split(";"):
            if not user in listTo2:
                if ListaUsersICDR.objects.filter(nome=user).exists():
                    lista = ListaUsersICDR.objects.get(nome=user)
                    for userListaBD in lista.user.split(";"):
                        if not userListaBD in listTo2 and not userListaBD == "":
                            listTo2.append(userListaBD + "@visteon.com")
                else:
                    if not user == "":
                        listTo2.append(user + "@visteon.com")

        if trigger2.estado == "ativo":
            if elem.ageing != "0" and elem.ageing != "-" and elem.ageing != "1":
                rctUnpCheck = ""
                cycleCountCheck = ""
                if elem.rctUnpCheck == "false" or elem.rctUnpCheck == "":
                    rctUnpCheck = ""
                elif elem.rctUnpCheck == "true":
                    rctUnpCheck = "X"

                if elem.cycleCountCheck == "false" or elem.cycleCountCheck == "":
                    cycleCountCheck = ""
                elif elem.cycleCountCheck == "true":
                    cycleCountCheck = "X"

                table = '</br><table class="display"><thead style="background-color: lightgray"><tr><th>DATA ABERTURA</th><th>AGEING (DIAS)</th><th>Nº/ANO</th><th>FORNECEDOR</th><th>PARTNUMBER</th><th>QT</th><th>MOTIVO</th><th>ALFANDEGA (S/N)</th><th>RESPONSÁVEL (NOME/DEPARTAMENTO)</th><th>COMENTÁRIOS (ABERTURA)</th><th>UN COST</th><th>TOTAL COST</th><th>RCT UNP</th><th>CYCLE COUNT</th><th>DATA FECHO</th><th>CYCLE COUNT</th><th>DATA CC</th><th>AUDIT CHECK</th></tr></thead><tbody>'
                table += (
                    '<tr style="background-color: whitesmoke"><td style="padding:0 15px 0 15px;">'
                    + elem.aberturaICDR
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + str(elem.ageing)
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.nAno
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.fornecedor
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.partnumber
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.quantidade
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.tipo
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.simNao
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.responsavel
                    + "/"
                    + elem.departamento
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.comentarioFecho
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.unCost
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.totalCost
                    + '</td><td style="padding:0 15px 0 15px; text-align: center">'
                    + rctUnpCheck
                    + '</td><td style="padding:0 15px 0 15px; text-align: center">'
                    + cycleCountCheck
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.date
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.cycleCount
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.dataCycleCount
                    + '</td><td style="padding:0 15px 0 15px;">'
                    + elem.auditCheck
                    + "</td></tr>"
                )
                table += '<tr style="background-color: lightgray"><td colspan="18"> </td></tr>'
                table += "</body></table>"

                subject, from_email, to = "Report ICDR", "noreply@visteon.com", listTo2
                msg = EmailMultiAlternatives(subject, table, from_email, to)
                msg.attach_alternative(table, "text/html")
                msg.send()


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d:%02d" % (hour, minutes, seconds)
