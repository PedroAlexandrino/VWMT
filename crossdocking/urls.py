from . import views
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.urls import path, re_path

app_name = "crossdocking"

urlpatterns = [ 
    path("configurationsEmailDiario/", views.configurationsEmailDiario, name="configurationsEmailDiario"),
    #----------------------------------Rotas para envio de emails calendarizados-------------------------------------
    path("uploadFicheiroDiarioAutomatico/", views.uploadFicheiroDiarioAutomatico, name="uploadFicheiroDiarioAutomatico"),
    path("sendFicheiroDiarioAutomatico/", views.sendFicheiroDiarioAutomatico, name="sendFicheiroDiarioAutomatico"),
    #----------------------------------////////karbox////////-------------------------------------
    path("render_karbox/", views.render_karbox, name="render_karbox"),
    
    #----------------------------------////////END karbox////////-------------------------------------

    path("filter/", views.prodlineFilter, name="prodlineFilter"),
    path("reportCrossdocking/", views.reportCrossdocking, name="reportCrossdocking"),
    path("configurations/", views.configurations, name="configurations"),
    path(
        "updateComentReceiving/",
        views.updateComentReceiving,
        name="updateComentReceiving",
    ),
    path(
        "updateComentShipping/", views.updateComentShipping, name="updateComentShipping"
    ),
    path("create/", views.create, name="create"),
    path("changeCheckbox/", views.changeCheckbox, name="changeCheckbox"),
    path("schedulePlanning/", views.schedulePlanning, name="schedulePlanning"),
    path("delete/", views.delete, name="delete"),
    path("submitAll/", views.submitAll, name="submitAll"),
    path("changeUserGroups/", views.changeUserGroups, name="changeUserGroups"),
    re_path(r"^download/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
