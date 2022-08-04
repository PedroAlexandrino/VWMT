from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import *

admin.site.site_title = "ADMIN | PWMS"
admin.site.site_header = "VISTEON PALMELA WAREHOUSE MANAGEMENT SYSTEM"
admin.site.index_title = ""

# admin.site.register(ArmazemChecklistQPS)
@admin.register(ArmazemChecklistQPS)
@admin.register(Produtos)
@admin.register(TipoEmbalagem)
@admin.register(ClientesOEM)
@admin.register(LinksShippingOperations)
@admin.register(ShippingOperation)
@admin.register(ReceivingOperation)
@admin.register(Others)
@admin.register(Procedimentos)
@admin.register(Crossdocking)
class ViewAdmin(ImportExportModelAdmin):
    pass
