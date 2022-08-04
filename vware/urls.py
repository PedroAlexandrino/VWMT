from . import views
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url
from django.urls import path
from .decorators import MetaRoutes


app_name = "vware"


urlpatterns = [
    #   # inutilizados
    #   path('create/', views.create, name='create'),
    #   path('qpsPacking/', views.qpsPacking, name='qpsPacking'),
    #   path('qpsShipping/', views.qpsShipping, name='qpsShipping'),
    #   path('tabela/', views.tabela, name='tabela'),
    #   path('', views.armazem, name='armazem'),
    #   path('reportOperations', views.reportOperations, name='reportOperations'),
    #   path('reportNonProduction', views.reportNonProduction, name='reportNonProduction'),
    #   path('configurationShippingOperation/', views.configurationShippingOperation,
    #        name='configurationShippingOperation'),
    #   path('configurationReceivingOperation/', views.configurationReceivingOperation,
    #        name='configurationReceivingOperation'),
    #   path('configurationCrossdockingOperation/', views.configurationCrossdockingOperation,
    #        name='configurationCrossdockingOperation'),
    #   path('configurationDocumentacao/', views.configurationDocumentacao, name='configurationDocumentacao'),
    #   path('configurationOthers/', views.configurationOthers, name='configurationOthers'),
    #   path('configurationAnexos/', views.configurationAnexos, name='configurationAnexos'),
    #   path('configurationQps/', views.configurationQps, name='configurationQps'),
    #   path('operations/', views.operations, name='operations'),
    #   path('qpsPackingPage/', views.qpsPackingPage, name='qpsPackingPage'),
    #   path('shippingOperation/', views.shippingOperation, name='shippingOperation'),
    #   path('receivingOperation/', views.receivingOperation, name='receivingOperation'),
    #   path('nonProductionOperation/', views.nonProductionOperation, name='nonProductionOperation'),
    #   path('armazem/tabelaParent/', views.armazem_tabelaParent, name='armazem_tabelaParent'),
    url(r"^download/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print(f"Foram adicionadas {len(MetaRoutes.routes)} rotas")

#

print(MetaRoutes.routes)


urlpatterns.extend(MetaRoutes.routes)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
