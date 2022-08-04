from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *


@admin.register(Teste_browse)
@admin.register(Teste_detail)
@admin.register(filteredTable)
@admin.register(PreShipperBrowse)
@admin.register(PreShipperDetailBrowse)
@admin.register(ficheiroShippers)
@admin.register(finalFicheiroShippers)
@admin.register(AbsMstrPriv)
@admin.register(AdPriv)
@admin.register(AbscPriv)
@admin.register(Abs2Priv)
@admin.register(PtPriv)
@admin.register(GatewayEmpresa)
@admin.register(GatewayCondutor)
@admin.register(GatewayCondutorID)
@admin.register(GatewayContactoCondutor)
@admin.register(GatewayInfoCondutor)
@admin.register(GatewayPrimeiraMatricula)
@admin.register(GatewaySegundaMatricula)
@admin.register(GatewayCargaDescarga)
@admin.register(GatewayDoca)
@admin.register(GatewayDestinoCarga)
@admin.register(GatewayTipoViatura)
@admin.register(Gateway)
@admin.register(GatewayBackup)
class ViewAdmin(ImportExportModelAdmin):
    pass
