from __future__ import annotations

import django_tables2 as django_tables

from shippers.models import Gateway_View
from typing import TYPE_CHECKING, Callable, Any, Optional

if TYPE_CHECKING:
    from typing_extensions import Self

class EllipsisColumn(django_tables.Column):
    def render(self, value):
        if len(value) > 15:
            return value[:12] + "..."
        return value

class FilterableColumn(django_tables.Column):
    def __init__(self, *args, **kwds) -> None:
        self.render_callback: Callable[[Self, Any], Any] = kwds.pop("render_cb", lambda self, value: value)
        super().__init__(*args, **kwds)

    def render(self, value):
        """Wrapper of render but it executes a render callback"""
        return self.render_callback(self, value)

    @property
    def style(self) -> str | None:
        return self.attrs.get("style")

    @style.setter
    def style(self, value: str) -> None:
        self.attrs["style"] = value

class GatewayTable(django_tables.Table):
    class Meta:
        model = Gateway_View
        attrs = {
            'class': 'stripe hover cell-border',
            'id': 'gateway',
            'style': 'width: 100%; margin: 0 auto;',
            'data-page-length': '25',
            'data-order': '[[3, "desc"], [11, "desc"]]',
            'data-info': 'false',
            'data-select': '{\'style\': \'os\'}',
        }
        #attrs = {"style": "height: 400px; overflow-y: auto;","id": lambda: "gateway"}

    def get_style_state(self: FilterableColumn, value: Any):
        print("In callback", value)
        self.style = "background-color: limegreen" if value.estado == "verde" else None
        return value

    id = django_tables.Column(visible=False)
    dataHoraChegada = FilterableColumn(verbose_name="Data/hora chegada")
    condutor = FilterableColumn(verbose_name="Condutor")
    ident = FilterableColumn(verbose_name="ID")
    contacto = django_tables.Column(verbose_name="Contacto")
    empresa  = django_tables.Column(verbose_name="Empresa")
    primeiraMatricula  = django_tables.Column(verbose_name="1ªMatrícula")
    segundaMatricula = django_tables.Column(verbose_name="2ªMatrícula")
    cargaDescarga= django_tables.Column(verbose_name="Carga/ Descarga")
    doca = django_tables.Column(verbose_name="Doca")
    destinoCarga = django_tables.Column(verbose_name="Destino carga")
    tipoViatura = django_tables.Column(verbose_name="Tipo de Viatura")
    dataHoraEntrada = django_tables.Column(verbose_name="Data/Hora de entrada")
    estado = django_tables.Column(verbose_name="Estado")
    abandono = django_tables.Column(verbose_name="Abandono")
    comentEntrada = django_tables.Column(verbose_name="Comentários entrada")
    dataHoraSaida = django_tables.Column(verbose_name="Data/hora de saída")
    comentSaida = django_tables.Column(verbose_name="Comentários saída")

    @classmethod
    def render_paginated_table(cls, request) -> Self:
        """Render paginated table"""
        table = cls(order_by = '-dataHoraChegada',data=Gateway_View.objects.all())
        table.paginate(page=request.GET.get("page", 1), per_page=30)
        return table


class GatewayRecorrenteTable(django_tables.Table):
    class Meta:
        model = Gateway_View
        template_name = 'django_tables2/bootstrap.html'
        attrs = {
            'class': 'stripe hover cell-border',
            'id': 'gatewayRecorrente',
            'style': 'width: 100%; margin: 0 auto;',
            'data-page-length': '25',
            'data-order': '[[3, "desc"], [11, "desc"]]',
            'data-info': 'false',
            'data-select': '{\'style\': \'os\'}',
            
        }
        """ attrs = {
            "style": "height: 400px; overflow-y: auto;cursor: pointer;","id": lambda: "gatewayRecorrente"}
        """
 
    id = django_tables.Column(visible=False, attrs={ "style": "background-color: black" })
    dataHoraChegada = django_tables.Column(verbose_name="Data/hora chegada")
    condutor = django_tables.Column(verbose_name="Condutor")
    ident = django_tables.Column(verbose_name="ID")
    contacto = django_tables.Column(verbose_name="Contacto")
    empresa  = django_tables.Column(verbose_name="Empresa")
    primeiraMatricula  = django_tables.Column(verbose_name="1ªMatrícula")
    segundaMatricula = django_tables.Column(verbose_name="2ªMatrícula")

    cargaDescarga= django_tables.Column(visible=False)
    doca = django_tables.Column(visible=False)
    destinoCarga = django_tables.Column(visible=False)
    tipoViatura = django_tables.Column(visible=False)
    dataHoraEntrada = django_tables.Column(visible=False)
    estado = django_tables.Column(visible=False)
    abandono = django_tables.Column(visible=False )
    comentEntrada = django_tables.Column(visible=False)
    dataHoraSaida = django_tables.Column(visible=False)
    comentSaida = django_tables.Column(visible=False)


    @classmethod
    def render_paginated_table(cls, request,pagination=False) -> Self:
        """Render paginated table"""
        values = Gateway_View.objects.all()
        tableRecorrente = cls(order_by = '-dataHoraChegada', data=values.values('id','dataHoraChegada','condutor','ident',
            'contacto','empresa','primeiraMatricula','segundaMatricula'))
        #tableRecorrente.paginate(page=request.GET.get("page", 1), per_page=50)
        
        return tableRecorrente
