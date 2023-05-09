from pickle import GET
from . import views
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.urls import path, re_path

app_name = "shippers"

urlpatterns = [
    path("teste_table/", lambda r: __import__("django").shortcuts.render(r, "shippers/teste.html"), name="teste_table"),
    path("shippersTracking/", views.shippersTracking, name="shippersTracking"), 
    path("json_gateway/", views.json_gateway, name="json"), 
    #Shippers Tracking
    path("reportPortariaTracking/", views.reportPortariaTracking, name="reportPortariaTracking"),
    path("downloadExcelShippersTracking/", views.downloadExcelShippersTracking, name="downloadExcelShippersTracking"),
    path("json_trackingShippers/", views.json_trackingShippers, name="json_trackingShippers"), 
    path("historicoTabelaShippersTracking/", views.historicoTabelaShippersTracking, name="historicoTabelaShippersTracking"), 
    path("json_trackingShippersUpdate/", views.json_trackingShippersUpdate, name="json_trackingShippersUpdate"), 
    path("shippersTrackingPage/", views.shippers_trackingPage, name="shippersTrackingPage"),
    path("addCommentShippersTracking/", views.addCommentShippersTracking, name="addCommentShippersTracking"),
    path("getSubItemsShippersTracking/", views.getSubItemsShippersTracking, name="getSubItemsShippersTracking"),

    path("getIdToRefreshShippersTracking/", views.getIdToRefreshShippersTracking, name="getIdToRefreshShippersTracking"), 
    path("populate_shippers_trackingPage/", views.populate_shippers_trackingPage, name="populate_shippers_trackingPage"), 
    path("hojeTabelaShippersTracking/", views.hojeTabelaShippersTracking, name="hojeTabelaShippersTracking"), 

    #-------------------------------------------------------------------------------------------------------------------
    path("getIdForChandedItemPortaria/", views.getIdForChandedItemPortaria, name="getIdForChandedItemPortaria"),
    
    path("deleteRowTracking/", views.deleteRowTracking, name="deleteRowTracking"),
    path(
        "shippersConfirmation/", views.shippersConfirmation, name="shippersConfirmation"
    ),
    path("searchCondutorExistente/", views.searchCondutorExistente, name="searchCondutorExistente"),
    #Medias  
    path("downloadPortaria/", views.mediaMensalEmpresa, name="mediaMensalEmpresa"),
    path("mediaMensalPortaria/", views.mediaMensalPortaria, name="mediaMensalPortaria"),
    path("createExcelPortaria/", views.createExcelPortaria, name="createExcelPortaria"),
    #Nova PaginaTrackingPage
    path("trackingPage/", views.trackingPage, name="trackingPage"),
    path("addLine/", views.addLine, name="addLine"),
    path("addNewRowTracking/", views.addNewRowTracking, name="addNewRowTracking"),
    path("botaoDadosQAD/", views.botaoDadosQAD, name="botaoDadosQAD"),
    path("downloadExcelHistoricoTracking/", views.downloadExcelHistoricoTracking, name="downloadExcelHistoricoTracking"),
    path("temporizadorEntradasPortaria/", views.temporizadorEntradasPortaria, name="temporizadorEntradasPortaria"),
    path("definicaoTempoEmailAtraso/", views.definicaoTempoEmailAtraso, name="definicaoTempoEmailAtraso"),
    #Fim d path("vware/", include("vware.urls")),o TrackingPage
    path("tracking/", views.tracking, name="tracking"),
    path("tracking2/", views.tracking2, name="tracking2"),
    path("security/", views.security, name="security"),
    path("portaria/", views.portaria, name="portaria"),
    path("configurations/", views.configurations, name="configurations"),
    path("changeUserGroups/", views.changeUserGroups, name="changeUserGroups"),
    path("comparaMatriculas/", views.comparaMatriculas, name="comparaMatriculas"),
    path("deleteLinhaPortaria/", views.deleteLinhaPortaria, name="deleteLinhaPortaria"),
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
    re_path(r"^download/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
