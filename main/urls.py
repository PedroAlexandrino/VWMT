from . import views
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.urls import path, re_path

# tentar ir ao main pelo decorator
app_name = "main"


urlpatterns = [
    path("", views.home, name="main"),
    path("updatesJson/", views.updatesJson, name="updatesJson"),
    path("addUpdate/", views.addUpdate, name="addUpdate"),
    re_path(r"^download/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
