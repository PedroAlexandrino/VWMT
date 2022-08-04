from . import views
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url
from django.urls import path

app_name = "receiving"

urlpatterns = [
    # TENDA
    path("tenda/", views.tenda, name="tenda"),
    path("updateTenda/", views.updateTenda, name="updateTenda"),
    path("uploadTendaCosts/", views.uploadTendaCosts, name="uploadTendaCosts"),
    # LINE REQUEST
    path("lineRequest/", views.lineRequest, name="lineRequest"),
    path(
        "uploadDataLineRequest/",
        views.uploadDataLineRequest,
        name="uploadDataLineRequest",
    ),
    path("configurations/", views.configurations, name="configurations"),
    path("createLine/", views.createLine, name="createLine"),
    path("deleteLine/", views.deleteLine, name="deleteLine"),
    path("deleteJustification/", views.deleteJustification, name="deleteJustification"),
    path("createJustification/", views.createJustification, name="createJustification"),
    # MNFG SUPPLY
    path("mnfgSupply/", views.mnfgSupply, name="mnfgSupply"),
    path("configurationMNFG/", views.configurationMNFG, name="configurationMNFG"),
    path("faSupply/", views.faSupply, name="faSupply"),
    path("uploadTaskBrowse/", views.uploadTaskBrowse, name="uploadTaskBrowse"),
    # path('getTaskBrowse/', views.getTaskBrowse, name='getTaskBrowse'),
    path("bpDropinSupply/", views.bpDropinSupply, name="bpDropinSupply"),
    path("bpSMDSupply/", views.bpSMDSupply, name="bpSMDSupply"),
    path("errorLog/", views.errorLog, name="errorLog"),
    path("pending/", views.pending, name="pending"),
    # TPM
    path("tpm/", views.tpm, name="tpm"),
    path("configurationsTPM/", views.configurationsTPM, name="configurationsTPM"),
    path("createAreaA/", views.createAreaA, name="createAreaA"),
    path("createAreaB/", views.createAreaB, name="createAreaB"),
    path("createKardex/", views.createKardex, name="createKardex"),
    path("deleteAreaA/", views.deleteAreaA, name="deleteAreaA"),
    path("deleteAreaB/", views.deleteAreaB, name="deleteAreaB"),
    path("deleteKardex/", views.deleteKardex, name="deleteKardex"),
    # OPERATION ANALYSE
    path("operationAnalyse/", views.operationAnalyse, name="operationAnalyse"),
    path("addRequest/", views.addRequest, name="addRequest"),
    path("updatePending/", views.updatePending, name="updatePending"),
    path("updateTimers/", views.updateTimers, name="updateTimers"),
    path(
        "addNewItemReceivingPos/",
        views.addNewItemReceivingPos,
        name="addNewItemReceivingPos",
    ),
    path("addNewSubItem/", views.addNewSubItem, name="addNewSubItem"),
    path("deleteSelectedItems/", views.deleteSelectedItems, name="deleteSelectedItems"),
    # path('deleteItemReceivingPos1/', views.deleteItemReceivingPos1, name='deleteItemReceivingPos1'),
    # path('editItemReceivingPos1/', views.editItemReceivingPos1, name='editItemReceivingPos1'),
    path("deleteSelectedItems/", views.deleteSelectedItems, name="deleteSelectedItems"),
    path("getPosicao1Data/", views.getPosicao1Data, name="getPosicao1Data"),
    path("getPosicao2Data/", views.getPosicao2Data, name="getPosicao2Data"),
    path("getBodyInfo/", views.getBodyInfo, name="getBodyInfo"),
    path("getPosicao3Data/", views.getPosicao3Data, name="getPosicao3Data"),
    path("getPosicao4Data/", views.getPosicao4Data, name="getPosicao4Data"),
    path("getPosicao5Data/", views.getPosicao5Data, name="getPosicao5Data"),
    path("getPosicao6Data/", views.getPosicao6Data, name="getPosicao6Data"),
    path("getPosicao7Data/", views.getPosicao7Data, name="getPosicao7Data"),
    path("getPosicao8Data/", views.getPosicao8Data, name="getPosicao8Data"),
    path(
        "submitDataFinalTurno/", views.submitDataFinalTurno, name="submitDataFinalTurno"
    ),
    path(
        "submitDataInicioTurno/",
        views.submitDataInicioTurno,
        name="submitDataInicioTurno",
    ),
    path(
        "submitDataFinalTurno2/",
        views.submitDataFinalTurno2,
        name="submitDataFinalTurno2",
    ),
    path(
        "submitDataInicioTurno2/",
        views.submitDataInicioTurno2,
        name="submitDataInicioTurno2",
    ),
    path(
        "submitDataFinalTurno3/",
        views.submitDataFinalTurno3,
        name="submitDataFinalTurno3",
    ),
    path(
        "submitDataInicioTurno3/",
        views.submitDataInicioTurno3,
        name="submitDataInicioTurno3",
    ),
    path(
        "submitDataFinalTurno4/",
        views.submitDataFinalTurno4,
        name="submitDataFinalTurno4",
    ),
    path(
        "submitDataInicioTurno4/",
        views.submitDataInicioTurno4,
        name="submitDataInicioTurno4",
    ),
    path(
        "submitDataFinalTurno5/",
        views.submitDataFinalTurno5,
        name="submitDataFinalTurno5",
    ),
    path(
        "submitDataInicioTurno5/",
        views.submitDataInicioTurno5,
        name="submitDataInicioTurno5",
    ),
    path(
        "submitDataFinalTurno6/",
        views.submitDataFinalTurno6,
        name="submitDataFinalTurno6",
    ),
    path(
        "submitDataInicioTurno6/",
        views.submitDataInicioTurno6,
        name="submitDataInicioTurno6",
    ),
    path(
        "submitDataFinalTurno7/",
        views.submitDataFinalTurno7,
        name="submitDataFinalTurno7",
    ),
    path(
        "submitDataInicioTurno7/",
        views.submitDataInicioTurno7,
        name="submitDataInicioTurno7",
    ),
    path(
        "submitDataFinalTurno8/",
        views.submitDataFinalTurno8,
        name="submitDataFinalTurno8",
    ),
    path(
        "submitDataInicioTurno8/",
        views.submitDataInicioTurno8,
        name="submitDataInicioTurno8",
    ),
    path("submitSubItems/", views.submitSubItems, name="submitSubItems"),
    path("getSubItems/", views.getSubItems, name="getSubItems"),
    path("changeUserGroups/", views.changeUserGroups, name="changeUserGroups"),
    path("habilitarQuadrados/", views.habilitarQuadrados, name="habilitarQuadrados"),
    path("definirTempos/", views.definirTempos, name="definirTempos"),
    path(
        "changeUserGroupsICDR/", views.changeUserGroupsICDR, name="changeUserGroupsICDR"
    ),
    path("configurationsICDR/", views.configurationsICDR, name="configurationsICDR"),
    # ICDR
    path("icdr/", views.icdr, name="icdr"),
    path("updateICDR/", views.updateICDR, name="updateICDR"),
    path("reportICDR/", views.reportICDR, name="reportICDR"),
    path("reAbrirICDR/", views.reAbrirICDR, name="reAbrirICDR"),
    path("criarListaUsersICDR/", views.criarListaUsersICDR, name="criarListaUsersICDR"),
    path(
        "mudaEstadoFiltroICDR/", views.mudaEstadoFiltroICDR, name="mudaEstadoFiltroICDR"
    ),
    path("criarICDR/", views.criarICDR, name="criarICDR"),
    path(
        "searchAllInfoUtilizadores/",
        views.searchAllInfoUtilizadores,
        name="searchAllInfoUtilizadores",
    ),
    path(
        "getUtilizadoresPorDepartamento/",
        views.getUtilizadoresPorDepartamento,
        name="getUtilizadoresPorDepartamento",
    ),
    path("criarUserICDR/", views.criarUserICDR, name="criarUserICDR"),
    path(
        "removerListaAlertaICDR/",
        views.removerListaAlertaICDR,
        name="removerListaAlertaICDR",
    ),
    path(
        "adicionarListaAlertaICDR/",
        views.adicionarListaAlertaICDR,
        name="adicionarListaAlertaICDR",
    ),
    path(
        "alterarEstadoTriggerICDR/",
        views.alterarEstadoTriggerICDR,
        name="alterarEstadoTriggerICDR",
    ),
    path(
        "removerUtilizadorICDR/",
        views.removerUtilizadorICDR,
        name="removerUtilizadorICDR",
    ),
    path("uploadDataICDR/", views.uploadDataICDR, name="uploadDataICDR"),
    path(
        "searchListasPorAlerta/",
        views.searchListasPorAlerta,
        name="searchListasPorAlerta",
    ),
    path("searchUsersPorLista/", views.searchUsersPorLista, name="searchUsersPorLista"),
    path(
        "adicionarUtilizadorListaICDR/",
        views.adicionarUtilizadorListaICDR,
        name="adicionarUtilizadorListaICDR",
    ),
    path(
        "removerUtilizadorListaICDR/",
        views.removerUtilizadorListaICDR,
        name="removerUtilizadorListaICDR",
    ),
    path("updatePONumber/", views.updatePONumber, name="updatePONumber"),
    path(
        "updateComentarioFechoICDR/",
        views.updateComentarioFechoICDR,
        name="updateComentarioFechoICDR",
    ),
    path("updateConsumption/", views.updateConsumption, name="updateConsumption"),
    path(
        "setDataHoraFechoICDR/", views.setDataHoraFechoICDR, name="setDataHoraFechoICDR"
    ),
    path("getElem/", views.getElem, name="getElem"),
    path("mudaEstadoSession/", views.mudaEstadoSession, name="mudaEstadoSession"),
    path("downloadExcel/", views.downloadExcel, name="downloadExcel"),
    path("getDepartamento/", views.getDepartamento, name="getDepartamento"),
    # REPORT
    path("reportLineRequest/", views.reportLineRequest, name="reportLineRequest"),
    path("reportTPM/", views.reportTPM, name="reportTPM"),
    path("reportMNFGSupply/", views.reportMNFGSupply, name="reportMNFGSupply"),
    url(r"^download/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
