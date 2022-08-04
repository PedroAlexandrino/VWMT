from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

from .settings import *
from django.conf.urls.static import static
from django.conf import settings

app_name = "vproject"


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "admini/", RedirectView.as_view(url=reverse_lazy("admin:index")), name="admin"
    ),
    path("vware/", include("vware.urls")),
    path("accounts/", include("accounts.urls")),
    path("packing/", include("pManagement.urls")),
    path("inqueritos/", include("inqueritos.urls")),
    path("main/", include("main.urls")),
    path("crossdocking/", include("crossdocking.urls")),
    path("shippers/", include("shippers.urls")),
    path("receiving/", include("receiving.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
