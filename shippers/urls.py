from pickle import GET
from . import views
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url
from django.urls import path

app_name = "shippers"

urlpatterns = [
    path("shippersTracking/", views.shippersTracking, name="shippersTracking"),
    path(
        "shippersConfirmation/", views.shippersConfirmation, name="shippersConfirmation"
    ),
    path("tracking/", views.tracking, name="tracking"),
    path("tracking2/", views.tracking2, name="tracking2"),
    path("security/", views.security, name="security"),
    path("portaria/", views.portaria, name="portaria"),
    path("configurations/", views.configurations, name="configurations"),
    path("changeUserGroups/", views.changeUserGroups, name="changeUserGroups"),
    path("comparaMatriculas/", views.comparaMatriculas, name="comparaMatriculas"),
    # path('shippersConfirmation/data', views.getInfoConfirmationData, name='shippersConfirmation_data'),
    path("downloadExcel/", views.downloadExcel, name="downloadExcel"),
    path("uploadDataPortaria/", views.uploadDataPortaria, name="uploadDataPortaria"),
    path("uploadDataExcel/", views.uploadDataExcel, name="uploadDataExcel"),
    path("uploadFiles/", views.uploadFiles, name="uploadFiles"),
    path("resetVeiculoDB/", views.resetVeiculoDB, name="resetVeiculoDB"),
    path("submitViatura/", views.submitViatura, name="submitViatura"),
    path(
        "submitGatewayRowUpdate/",
        views.submitGatewayRowUpdate,
        name="submitGatewayRowUpdate",
    ),
    path("submitGateway/", views.submitPortaria, name="submitGateway"),
    path("getChildValues/", views.getChildValues, name="getChildValues"),
    path("getDataFicheiro/", views.getDataFicheiro, name="getDataFicheiro"),
    path("searchCondutor/", views.searchCondutor, name="searchCondutor"),
    path("searchContacto/", views.searchContacto, name="searchContacto"),
    path("setDataHoraEntrada/", views.setDataHoraEntrada, name="setDataHoraEntrada"),
    path("setDataHoraSaida/", views.setDataHoraSaida, name="setDataHoraSaida"),
    path("searchCondutorID/", views.searchCondutorID, name="searchCondutorID"),
    path("searchEmpresa/", views.searchEmpresa, name="searchEmpresa"),
    path("searchAllInfo/", views.searchAllInfo, name="searchAllInfo"),
    path("reportSecurity/", views.reportSecurity, name="reportSecurity"),
    path("reportPortaria/", views.reportPortaria, name="reportPortaria"),
    path("reportTracking/", views.reportTracking, name="reportTracking"),
    path("reportConfirmation/", views.reportConfirmation, name="reportConfirmation"),
    path("mudaEstadoFiltro/", views.mudaEstadoFiltro, name="mudaEstadoFiltro"),
    path(
        "uploadShippersConfirmation/",
        views.uploadShippersConfirmation,
        name="uploadShippersConfirmation",
    ),
    url(r"^download/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
