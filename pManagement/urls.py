from . import views
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url
from django.urls import path

app_name = "pManagement"

urlpatterns = [
    # Packing
    # Request

    path("requests/", views.requests, name="requests"),
    path("takeQuantity/", views.takeQuantity, name="takeQuantity"),
    path("supplyPackage/", views.supplyPackage, name="supplyPackage"),
    path("updateSupplyPackage/", views.updateSupplyPackage, name="updateSupplyPackage"),
    path("deleteSuplyPackage/", views.deleteSuplyPackage, name="deleteSuplyPackage"),
    path(
        "updateInventorySupplyPackage/",
        views.updateInventorySupplyPackage,
        name="updateInventorySupplyPackage",
    ),
    path("updateSupplyStock", views.updateSupplyStock, name="updateSupplyStock"),
    path(
        "updateAllStockSupplyPackage/",
        views.updateAllStockSupplyPackage,
        name="updateAllStockSupplyPackage",
    ),
    path(
        "deleteLinhaClienteProduto/",
        views.deleteLinhaClienteProduto,
        name="deleteLinhaClienteProduto",
    ),
    path(
        "updateClienteProduto/", views.updateClienteProduto, name="updateClienteProduto"
    ),
    path("atualizaTempo/", views.atualizaTempo, name="atualizaTempo"),
    path("upload", views.upload, name="upload"),
    path("clients-json/", views.get_json_client_data, name="clients-json"),
    path("products-json/", views.get_json_product_data, name="products-json"),
    path(
        "products-json/<str:client>/", views.get_json_product_data, name="products-json"
    ),
    path("type-json/<str:product>/", views.get_json_type_data, name="type-json"),
    # Pedido extra Packing
    path("createExtra/", views.create, name="pedidoExtra"),
    path("getPNClienteProduto/", views.getPNClienteProduto, name="getPNClienteProduto"),
    path("get_cliente_produto/", views.get_cliente_produto, name="get_cliente_produto"),
    path("get_cliente_produto_rel/", views.get_cliente_produto_rel, name="get_cliente_produto_rel"),
    path("get_stock_package_rel/", views.get_stock_package_rel, name="get_stock_package_rel"),
    # Supply
    path("supply/", views.supply, name="supply"),
    path("atualizaEstado", views.atualizaEstado, name="atualizaEstado"),
    path("clienteProduto/", views.clienteProduto, name="clienteProduto"),
    path("downloadExcelClienteProduto/", views.downloadExcelClienteProduto, name="downloadExcelClienteProduto"),
    path(
        "deleteLinhaClienteProduto/",
        views.deleteLinhaClienteProduto,
        name="deleteLinhaClienteProduto",
    ),
    path(
        "downloadExcelSupplyPackage/",
        views.downloadExcelSupplyPackage,
        name="downloadExcelSupplyPackage",
    ),
    # path("clienteProduto1/", views.clienteProduto1, name="clienteProduto1"),
    # path('pesquisaHistorico', views.pesquisaHistorico, 'pesquisaHistorico'),
    path("addHistoric/", views.addHistoric, name="addHistoric"),
    path("updateLinhaSupply/", views.updateLinhaSupply, name="updateLinhaSupply"),
    path("deleteLinhaSupply/", views.deleteLinhaSupply, name="deleteLinhaSupply"),
    path("addRowSupplyPackage/", views.addRowSupplyPackage, name="addRowSupplyPackage"),
    # stock
    path("stock/", views.stock, name="stock"),
    path("updateStock/", views.updateStock, name="updateStock"),
    path("criarElementoStock/", views.criarElementoStock, name="criarElementoStock"),
    path("updateLinhaStock/", views.updateLinhaStock, name="updateLinhaStock"),
    path("deleteLinhaStock/", views.deleteLinhaStock, name="deleteLinhaStock"),
    # Expendable
    path("expendablePacking/", views.expendablePacking, name="expendablePacking"),
    path("createExpendable/", views.createExpendable, name="createExpendable"),
    # path("uploadExpendable", views.uploadExpendable, name="uploadExpendable"),
    path("savePNExpendable", views.savePNExpendable, name="savePNExpendable"),
    path("getPNExpendable", views.getPNExpendable, name="getPNExpendable"),
    path(
        "updateLinhaExpendable",
        views.updateLinhaExpendable,
        name="updateLinhaExpendable",
    ),
    path(
        "deleteLinhaExpendable/",
        views.deleteLinhaExpendable,
        name="deleteLinhaExpendable",
    ),
    path("deleteLinhaPacking/", views.deleteLinhaPacking, name="deleteLinhaPacking"),
    # STOCKPACKAGE
    path("stockPackage/", views.stockPackage, name="stockPackage"),
    path("updateAllStock/", views.updateAllStock, name="updateAllStock"),
    path("updateInventory/", views.updateInventory, name="updateInventory"),
    path("createStockPackage/", views.createStockPackage, name="createStockPackage"),
    path("updateStockPackage/", views.updateStockPackage, name="updateStockPackage"),
    path(
        "deleteLinhaStockPackage/",
        views.deleteLinhaStockPackage,
        name="deleteLinhaStockPackage",
    ),
    path(
        "downloadExcelStockPackage/",
        views.downloadExcelStockPackage,
        name="downloadExcelStockPackage",
    ),
    url(r"^view-pdf/$", views.pdf_view, name="pdf_view"),
    url(r"^view1-pdf/$", views.pdf_view1, name="pdf_view1"),
    path("uploadStockFile/", views.uploadStockFile, name="uploadStockFile"),
    path(
        "uploadStockFileStock/", views.uploadStockFileStock, name="uploadStockFileStock"
    ),
    # Returnable
    path("returnablePacking/", views.returnablePacking, name="returnablePacking"),
    path("createReturnable/", views.createReturnable, name="createReturnable"),
    path(
        "updateLinhaReturnable",
        views.updateLinhaReturnable,
        name="updateLinhaReturnable",
    ),
    path("savePNReturnable", views.savePNReturnable, name="savePNReturnable"),
    path("getPNReturnable", views.getPNReturnable, name="getPNReturnable"),
    path("uploadReturnable", views.uploadReturnable, name="uploadReturnable"),
    path(
        "deleteLinhaReturnable/",
        views.deleteLinhaReturnable,
        name="deleteLinhaReturnable",
    ),
    # Reports
    path(
        "reportReturnablePackage",
        views.reportReturnablePackage,
        name="reportReturnablePackage",
    ),
    path("reportSupplyPackage", views.reportSupplyPackage, name="reportSupplyPackage"),
    path(
        "createClienteProduto/", views.createClienteProduto, name="createClienteProduto"
    ),
    path(
        "reportExpendablePackage",
        views.reportExpendablePackage,
        name="reportExpendablePackage",
    ),
    path(
        "reportCustomerPacking",
        views.reportCustomerPacking,
        name="reportCustomerPacking",
    ),
    path(
        "returnListaProdutos",
        views.returnListaProdutos,
        name="returnListaProdutos"
    ),
    # Configurations
    path("changeUserGroups/", views.changeUserGroups, name="changeUserGroups"),
    path("configurations/", views.configurations, name="configurations"),
    url(r"^download/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
