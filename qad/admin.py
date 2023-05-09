from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *

@admin.register(WtskhHist)
@admin.register(WtskMstr)
@admin.register(XxusrwWkfl)

class ViewAdmin(ImportExportModelAdmin):
    pass
