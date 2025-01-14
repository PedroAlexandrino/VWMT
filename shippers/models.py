from django.db import models

# Create your models here.

class Teste_browse(models.Model):
    shipFrom = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    idBrowse = models.CharField(max_length=50, null=True)
    shipTo = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    shipDate = models.CharField(max_length=50, null=True)
    shipTime = models.CharField(max_length=50, null=True)
    carrier = models.CharField(max_length=50, null=True)
    shipVia = models.CharField(max_length=50, null=True)
    fob = models.CharField(max_length=50, null=True)
    modeOfTransport = models.CharField(max_length=50, null=True)
    vehicleID = models.CharField(max_length=50, null=True)
    mbol = models.CharField(max_length=50, null=True)
    preShipperID = models.CharField(max_length=50, null=True)
    totalMasterPacks = models.CharField(max_length=50, null=True)
    loadedMasterPacks = models.CharField(max_length=50, null=True)
    inProcess = models.CharField(max_length=50, null=True)
    confirmed = models.CharField(max_length=150, null=True)
    cancelled = models.CharField(max_length=150, null=True)
    invMov = models.CharField(max_length=150, null=True)

    # META CLASS
    class Meta:
        verbose_name = 'Teste Browse'
        verbose_name_plural = 'Teste Browse'

    # TO STRING METHOD
    def __str__(self):
        return f"{self.idBrowse}"


class Teste_detail(models.Model):
    shipFrom = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    preShipperShipper = models.CharField(max_length=50, null=True)
    sortName = models.CharField(max_length=50, null=True)
    shipTo = models.CharField(max_length=50, null=True)
    shipToDock = models.CharField(max_length=50, null=True)
    shipDate = models.CharField(max_length=50, null=True)
    itemNumber = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=100, null=True)
    quantityToShip = models.CharField(max_length=50, null=True)
    quantityShipped = models.CharField(max_length=50, null=True)
    um = models.CharField(max_length=50, null=True)
    site = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    lotSerial = models.CharField(max_length=50, null=True)
    reference = models.CharField(max_length=50, null=True)
    order = models.CharField(max_length=50, null=True)
    line = models.CharField(max_length=150, null=True)
    mbol = models.CharField(max_length=150, null=True)
    confirmed = models.CharField(max_length=150, null=True)
    invMov = models.CharField(max_length=150, null=True)
    idDetail = models.CharField(max_length=100, null=True)

    # META CLASS
    class Meta:
        verbose_name = 'Teste Detail'
        verbose_name_plural = 'Teste Detail'

    # TO STRING METHOD
    def __str__(self):
        return f"{self.idDetail}"


# tabela que resulta de filtros aplicados a Teste_detail e Teste_browse
class filteredTable(models.Model):
    idComum = models.CharField(max_length=50, null=True)
    shipDate = models.CharField(max_length=50, null=True)
    shipTime = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    carrier = models.CharField(max_length=50, null=True)
    modeOfTransport = models.CharField(max_length=50, null=True)
    vehicleID = models.CharField(max_length=50, null=True)
    itemNumber = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=150, null=True)
    quantityToShip = models.CharField(max_length=150, null=True)
    quantityShipped = models.CharField(max_length=150, null=True)
    inProcess = models.CharField(max_length=150, null=True)
    confirmed = models.CharField(max_length=150, null=True)

    # META CLASS
    class Meta:
        verbose_name = 'Tabela Shippers Filtrada'
        verbose_name_plural = 'Tabela Shippers Filtrada'

    # TO STRING METHOD
    def __str__(self):
        return f"{self.idComum}"

# tabela em uso no shippers tracking. tabela mae
class PreShipperBrowse(models.Model):
    shipFrom = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    idShipper = models.CharField(max_length=50, null=True)
    shipTo = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    shipDate = models.CharField(max_length=50, null=True)
    shipTime = models.CharField(max_length=50, null=True)
    carrier = models.CharField(max_length=50, null=True)
    shipVia = models.CharField(max_length=50, null=True)
    fob = models.CharField(max_length=150, null=True)
    transportMode = models.CharField(max_length=150, null=True)
    vehicleId = models.CharField(max_length=150, null=True)
    mbol = models.CharField(max_length=150, null=True)
    preShipper = models.CharField(max_length=150, null=True)
    totalMasterPacks = models.CharField(max_length=150, null=True)
    loadedMasterPacks = models.CharField(max_length=150, null=True)
    inProcess = models.CharField(max_length=150, null=True)
    confirmed = models.CharField(max_length=150, null=True)
    cancelled = models.CharField(max_length=150, null=True)
    invMov = models.CharField(max_length=150, null=True)

    # META CLASS
    class Meta:
        verbose_name = 'Pre-Shipper Browse'
        verbose_name_plural = 'Pre-Shipper Browse'

    # TO STRING METHOD
    def __str__(self):
        return f"{self.idShipper}"


# tabela em uso no shippers tracking. tabela filha
class PreShipperDetailBrowse(models.Model):
    shipFrom = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    idShipper = models.CharField(max_length=50, null=True)
    sortName = models.CharField(max_length=50, null=True)
    shipTo = models.CharField(max_length=50, null=True)
    shipToDock = models.CharField(max_length=50, null=True)
    shipDate = models.CharField(max_length=50, null=True)
    itemNumber = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    quantityToShip = models.CharField(max_length=50, null=True)
    quantityShipped = models.CharField(max_length=50, null=True)
    um = models.CharField(max_length=50, null=True)
    site = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    lotSerial = models.CharField(max_length=150, null=True)
    reference = models.CharField(max_length=150, null=True)
    order = models.CharField(max_length=150, null=True)
    line = models.CharField(max_length=150, null=True)
    mbol = models.CharField(max_length=150, null=True)
    confirmed = models.CharField(max_length=150, null=True)
    invMov = models.CharField(max_length=150, null=True)
    idGrande = models.CharField(max_length=150, null=True)

    # META CLASS
    class Meta:
        verbose_name = 'Pre-Shipper Detail Browse'
        verbose_name_plural = 'Pre-Shipper Detail Browse'

    # TO STRING METHOD
    def __str__(self):
        return f"{self.idShipper}"



# tabela em uso no shippers confirmation
class ficheiroShippers(models.Model):
    masterSerialID = models.CharField(max_length=50, null=True)
    preShipperShipper = models.CharField(max_length=50, null=True)
    packItem = models.CharField(max_length=50, null=True)
    numberOfPacks = models.CharField(max_length=50, null=True)

    # META CLASS
    class Meta:
        verbose_name = 'Tabela Shippers CONFIRMATION'
        verbose_name_plural = 'Tabela Shippers CONFIRMATION'

    # TO STRING METHOD
    def __str__(self):
        return f"{self.masterSerialID}"


# tabela em uso no shippers confirmation
class finalFicheiroShippers(models.Model):
    masterSerialID = models.CharField(max_length=50, null=True)
    preShipperShipper = models.CharField(max_length=50, null=True)
    packItem = models.CharField(max_length=50, null=True)
    numberOfPacks = models.CharField(max_length=50, null=True)

    # META CLASS
    class Meta:
        verbose_name = 'Tabela Shippers CONFIRMATION'
        verbose_name_plural = 'Tabela Shippers CONFIRMATION'

    # TO STRING METHOD
    def __str__(self):
        return f"{self.masterSerialID} - {self.packItem}"


class AbsMstrPriv(models.Model):
    abs_id_2 = models.CharField(max_length=100, null=True)
    abs_shp_date_2 = models.CharField(max_length=100, null=True)
    abs_shp_time_2 = models.CharField(max_length=100, null=True)
    abs_qad01_2 = models.CharField(max_length=150, null=True)
    oid_abs_mstr_2 = models.CharField(max_length=100, null=True)
    abs_status_2 = models.CharField(max_length=100, null=True)
    abs_shipto_2 = models.CharField(max_length=100, null=True)
    abs_item_2 = models.CharField(max_length=100, null=True)
    abs_domain_2 = models.CharField(max_length=100, null=True)

    # META CLASS
    class Meta:
        verbose_name = 'Abs mstr copy'
        verbose_name_plural = 'Abs mstr copy'
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.abs_id_2}"

class AdPriv(models.Model):
    ad_addr_2 = models.ForeignKey(AbsMstrPriv, on_delete=models.CASCADE)
    ad_city_2 = models.CharField(max_length=100, null=True)
    ad_country_2 = models.CharField(max_length=100, null=True)

    # META CLASS
    class Meta:
        verbose_name = 'Ad copy'
        verbose_name_plural = 'Ad copy'
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.ad_addr_2}"


class Abs2Priv(models.Model):
    abs_par_id_2 = models.CharField(max_length=100, null=True)
    abs_item_2 = models.CharField(max_length=100, null=True)
    abs_qty_2 = models.CharField(max_length=100, null=True)
    abs_ship_qty_2 = models.CharField(max_length=100, null=True)

    # META CLASS
    class Meta:
        verbose_name = 'Abs2 copy'
        verbose_name_plural = 'Abs2 copy'
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.abs_par_id_2}"


class AbscPriv(models.Model):
    absc_abs_id_2 = models.ForeignKey(Abs2Priv, on_delete=models.CASCADE)
    absc_carrier_2 = models.CharField(max_length=100, null=True)

    # META CLASS
    class Meta:
        verbose_name = 'Absc copy'
        verbose_name_plural = 'Absc copy'
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.absc_abs_id_2}"


class PtPriv(models.Model):
    pt_desc1_2 = models.CharField(max_length=100, null=True)
    pt_desc2_2 = models.CharField(max_length=100, null=True)
    pt_part_2 = models.ForeignKey(Abs2Priv, on_delete=models.CASCADE)

    # META CLASS
    class Meta:
        verbose_name = 'Pt copy'
        verbose_name_plural = 'Pt copy'
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.pt_part_2}"


class GatewayBackup(models.Model):
    dataHoraChegada = models.CharField(max_length=100, null=True)
    empresa = models.CharField(max_length=100, null=True)
    condutor = models.CharField(max_length=100, null=True)
    ident = models.CharField(max_length=100, null=True)
    contacto = models.CharField(max_length=100, null=True)
    primeiraMatricula = models.CharField(max_length=100, null=True)
    segundaMatricula = models.CharField(max_length=100, null=True)
    cargaDescarga = models.CharField(max_length=100, null=True)
    doca = models.CharField(max_length=100, null=True)
    destinoCarga = models.CharField(max_length=100, null=True)
    tipoViatura = models.CharField(max_length=100, null=True)
    dataHoraEntrada = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=100, null=True)
    abandono = models.CharField(max_length=100, null=True)
    comentEntrada = models.CharField(max_length=2000, null=True)
    dataHoraSaida = models.CharField(max_length=100, null=True)
    comentSaida = models.CharField(max_length=2000, null=True)

    # META CLASS
    class Meta:
        verbose_name = 'Gateway histórico - BACKUP'
        verbose_name_plural = 'Gateway histórico - BACKUP'
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.dataHoraChegada}"


class Gateway(models.Model):
    dataHoraChegada = models.CharField(max_length=100, null=True)
    empresa = models.CharField(max_length=100, null=True)
    condutor = models.CharField(max_length=100, null=True)
    ident = models.CharField(max_length=100, null=True)
    contacto = models.CharField(max_length=100, null=True)
    primeiraMatricula = models.CharField(max_length=100, null=True)
    segundaMatricula = models.CharField(max_length=100, null=True)
    cargaDescarga = models.CharField(max_length=100, null=True)
    doca = models.CharField(max_length=100, null=True)
    destinoCarga = models.CharField(max_length=100, null=True)
    tipoViatura = models.CharField(max_length=100, null=True)
    dataHoraEntrada = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=100, null=True)
    abandono = models.CharField(max_length=100, null=True)
    comentEntrada = models.CharField(max_length=2000, null=True)
    dataHoraSaida = models.CharField(max_length=100, null=True)
    comentSaida = models.CharField(max_length=2000, null=True)

    # META CLASS
    class Meta:
        verbose_name = 'Gateway histórico'
        verbose_name_plural = 'Gateway histórico'
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.dataHoraChegada}"
    def to_dict(self):
        return {
            "id": self.id,
            "dataHoraChegada": self.dataHoraChegada,
            "empresa": self.empresa,
            "condutor": self.condutor,
            "ident": self.ident,
            "contacto": self.contacto,
            "primeiraMatricula": self.primeiraMatricula,
            "segundaMatricula": self.segundaMatricula,
            "cargaDescarga": self.cargaDescarga,
            "doca": self.doca,
            "destinoCarga": self.destinoCarga,
            "tipoViatura": self.tipoViatura,
            "dataHoraEntrada": self.dataHoraEntrada,
            "estado": self.estado,
            "abandono": self.abandono,
            "comentEntrada": self.comentEntrada,
            "dataHoraSaida": self.dataHoraSaida,
            "comentSaida": self.comentSaida,

        }

class Security(models.Model):
    shipper = models.CharField(max_length=100, null=True)
    masterSerials = models.CharField(max_length=100, null=True)
    validacao = models.CharField(max_length=100, null=True)
    dataHoraSaida = models.CharField(max_length=100, null=True)
    comentarios = models.CharField(max_length=100, null=True)

    # META CLASS
    class Meta:
        verbose_name = 'Security histórico'
        verbose_name_plural = 'Security histórico'
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.shipper}"


class GatewayEmpresa(models.Model):
    nome = models.CharField(max_length=100, null=True)

    # META CLASS
    class Meta:
        verbose_name = 'Gateway Empresas'
        verbose_name_plural = 'Gateway Empresas'
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nome}"

class GatewayCondutor(models.Model):
    nome = models.CharField(max_length=100, null=True)

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nome}"

class GatewayCondutorID(models.Model):
    nome = models.CharField(max_length=100, null=True)

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nome}"

class GatewayContactoCondutor(models.Model):
    nome = models.CharField(max_length=100, null=True)

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nome}"

class GatewayInfoCondutor(models.Model):
    condutor = models.ForeignKey(GatewayCondutor, on_delete=models.CASCADE, null=True)
    condutorID = models.ForeignKey(GatewayCondutorID, on_delete=models.CASCADE, null=True)
    contacto = models.ForeignKey(GatewayContactoCondutor, on_delete=models.CASCADE, null=True)
    empresa = models.ForeignKey(GatewayEmpresa, on_delete=models.CASCADE, null=True)

    # TO STRING METHOD
    def __str__(self):
        return f"{self.condutor}"

class GatewayPrimeiraMatricula(models.Model):
    nome = models.CharField(max_length=100, null=True)
    empresa = models.ForeignKey(GatewayEmpresa, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f"{self.nome}"

class GatewaySegundaMatricula(models.Model):
    nome = models.CharField(max_length=100, null=True)

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nome}"

class GatewayCargaDescarga(models.Model):
    nome = models.CharField(max_length=100, null=True)

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nome}"

class GatewayDoca(models.Model):
    nome = models.CharField(max_length=100, null=True)

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nome}"

class GatewayDestinoCarga(models.Model):
    nome = models.CharField(max_length=100, null=True)

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nome}"

class GatewayTipoViatura(models.Model):
    nome = models.CharField(max_length=100, null=True)

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nome}"

class SecurityShipper(models.Model):
    nome = models.CharField(max_length=100, null=True)

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nome}"

class TrackingPage(models.Model):
    nShipper = models.CharField(max_length=10, null=True, blank=True)
    qtyCaixas = models.CharField(null=True, blank=True, max_length=15)
    inicioPrep = models.DateTimeField(null=True, blank=True)
    fimPrep= models.DateTimeField(null=True, blank=True)
    confirmacao = models.DateTimeField(null=True, blank=True)
    comentarios = models.CharField(max_length=100, null=True, blank=True)
    #dados do QAD(Estao ja a ser importados na pasta Qad)
    ship_date = models.CharField(max_length=20, null=True, blank=True)
    ship_time = models.CharField(max_length=20, null=True, blank=True)
    ship_carrier = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):

        return f"{self.nShipper}"


class LastUpdatePortaria(models.Model):
    dataUpdate = models.DateTimeField(max_length=20, null=True, blank=True)

# TO STRING METHOD
def __str__(self):
    return f"{self.dataUpdate}"





class Gateway_View(models.Model):
    dataHoraChegada = models.CharField(max_length=200, null=True)
    empresa = models.CharField(max_length=200, null=True)
    condutor = models.CharField(max_length=200, null=True)
    ident = models.CharField(max_length=200, null=True)
    contacto = models.CharField(max_length=200, null=True)
    primeiraMatricula = models.CharField(max_length=200, null=True)
    segundaMatricula = models.CharField(max_length=200, null=True)
    cargaDescarga = models.CharField(max_length=200, null=True)
    doca = models.CharField(max_length=200, null=True)
    destinoCarga = models.CharField(max_length=200, null=True)
    tipoViatura = models.CharField(max_length=200, null=True)
    dataHoraEntrada = models.CharField(max_length=200, null=True)
    estado = models.CharField(max_length=200, null=True)
    abandono = models.CharField(max_length=200, null=True)
    comentEntrada = models.CharField(max_length=600, null=True)
    dataHoraSaida = models.CharField(max_length=100, null=True)
    comentSaida = models.CharField(max_length=600, null=True)

    # META CLASS
    class Meta:
        managed = False
        db_table ="gateway_View"

    # TO STRING METHOD
    def __str__(self):
        return f"{self.dataHoraChegada}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "dataHoraChegada": self.dataHoraChegada,
            "empresa": self.empresa,
            "condutor": self.condutor,
            "ident": self.ident,
            "contacto": self.contacto,
            "primeiraMatricula": self.primeiraMatricula,
            "segundaMatricula": self.segundaMatricula,
            "cargaDescarga": self.cargaDescarga,
            "doca": self.doca,
            "destinoCarga": self.destinoCarga,
            "tipoViatura": self.tipoViatura,
            "dataHoraEntrada": self.dataHoraEntrada,
            "estado": self.estado,
            "abandono": self.abandono,
            "comentEntrada": self.comentEntrada,
            "dataHoraSaida": self.dataHoraSaida,
            "comentSaida": self.comentSaida,

        }
    
class Tracking_ShippersPage_Sub_Items(models.Model):
    abs_id = models.CharField(max_length=200, null=True)
    abs_status  = models.CharField(max_length=200, null=True)
    abs_shipfrom = models.CharField(max_length=200, null=True)
    abs_item = models.CharField(max_length=200, null=True)
    abs_qty = models.CharField(max_length=200, null=True)
    abs_ship_qty = models.CharField(max_length=200, null=True)

    
    # TO STRING METHOD
    def __str__(self):
        return f"{self.dataHoraChegada}"
    
    def to_dict(self):
        return {
            "abs_id": self.abs_id,
            "abs_status": self.abs_status,
            "abs_shipfrom": self.abs_shipfrom,
            "abs_item": self.abs_item,
            "abs_qty": self.abs_qty,
            "abs_ship_qty": self.abs_ship_qty,
        }
    

          
class Tracking_ShippersPage(models.Model):
    abs_id = models.CharField(max_length=200, null=True)
    ship_date = models.CharField(max_length=200, null=True)
    ship_time = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    carrier = models.CharField(max_length=200, null=True)
    fob = models.CharField(max_length=200, null=True)
    mode_of_transport = models.CharField(max_length=200, null=True)
    #vehicle_id = models.ForeignKey(Gateway, on_delete=models.CASCADE,default=None,null=True)
    vehicle_id = models.CharField(max_length=200, null=True)
    total_master_packs = models.CharField(max_length=200, null=True)
    confirmed = models.CharField(max_length=200, null=True)
    estado =  models.CharField(max_length=50, null=True) #fazer alteração na bd
    timestamp = models.CharField(max_length=200, null=True)
    comentarios = models.CharField(max_length=200, null=True, blank=True, default='')
    date_validation = models.CharField(max_length=50, null=True)
    tracking_shipperspage_sub_items = models.ManyToManyField(Tracking_ShippersPage_Sub_Items)
    sub_item_flag = models.CharField(max_length=50, null=True)
    
    # TO STRING METHOD
    def __str__(self):
        return f"{self.abs_id}"
    
    def to_dict(self):
        sub_items = []
        for item in self.tracking_shipperspage_sub_items.all():
            sub_items.append(item.to_dict())
        sub_items_ids = list(self.tracking_shipperspage_sub_items.values_list('id', flat=True))
        return {
            "id": self.id,
            "abs_id": self.abs_id,
            "ship_date": self.ship_date,
            "ship_time": self.ship_time,
            "city": self.city,
            "country": self.country,
            "carrier": self.carrier,
            "fob": self.fob,
            "mode_of_transport": self.mode_of_transport,
            "vehicle_id": self.vehicle_id,
            "total_master_packs": self.total_master_packs,
            "confirmed": self.confirmed,
            "estado": self.estado,
            "timestamp": self.timestamp,
            "comentarios": self.comentarios,
            "date_validation": self.date_validation,
            "sub_item_flag": self.sub_item_flag,
            "tracking_shipperspage_sub_items": sub_items,
            "tracking_shipperspage_sub_items_ids": sub_items_ids
        }
    def to_dictTimestamp(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp,
        }
    

class Tracking_ShippersPage_View(models.Model):
    abs_id = models.CharField(max_length=200, null=True)
    ship_date = models.CharField(max_length=200, null=True)
    ship_time = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    carrier = models.CharField(max_length=200, null=True)
    fob = models.CharField(max_length=200, null=True)
    mode_of_transport = models.CharField(max_length=200, null=True)
    #vehicle_id = models.ForeignKey(Gateway, on_delete=models.CASCADE,default=None,null=True)
    vehicle_id = models.CharField(max_length=200, null=True)
    total_master_packs = models.CharField(max_length=200, null=True)
    confirmed = models.CharField(max_length=200, null=True)
    estado =  models.CharField(max_length=50, null=True) #fazer alteração na bd
    timestamp = models.CharField(max_length=200, null=True)
    comentarios = models.CharField(max_length=200, null=True, blank=True, default='')
    date_validation = models.CharField(max_length=50, null=True)
    tracking_shipperspage_sub_items = models.ManyToManyField(Tracking_ShippersPage_Sub_Items)
    sub_item_flag = models.CharField(max_length=50, null=True)
    # TO STRING METHOD
    def __str__(self):
        return f"{self.abs_id}"
    class Meta:
        managed = False
        db_table ="shippers_tracking_shipperspage_view"
    
    def to_dict(self):
        sub_items = []
        for item in self.tracking_shipperspage_sub_items.all():
            sub_items.append(item.to_dict())
        sub_items_ids = list(self.tracking_shipperspage_sub_items.values_list('id', flat=True))
        return {
            "id": self.id,
            "abs_id": self.abs_id,
            "ship_date": self.ship_date,
            "ship_time": self.ship_time,
            "city": self.city,
            "country": self.country,
            "carrier": self.carrier,
            "fob": self.fob,
            "mode_of_transport": self.mode_of_transport,
            "vehicle_id": self.vehicle_id,
            "total_master_packs": self.total_master_packs,
            "confirmed": self.confirmed,
            "estado": self.estado,
            "timestamp": self.timestamp,
            "comentarios": self.comentarios,
            "date_validation": self.date_validation,
            "sub_item_flag": self.sub_item_flag,
            "tracking_shipperspage_sub_items": sub_items,
            "tracking_shipperspage_sub_items_ids": sub_items_ids
        }
    


    
    
class Tracking_ShippersPage_Refresh(models.Model):
    lastUpdate = models.CharField(max_length=200, null=True)
    
    # TO STRING METHOD
    def __str__(self):
        return f"{self.lastUpdate}"
    

""" ESTA TABELA SÂO DO MAIN """

class UpdatesProj(models.Model):
    update = models.CharField(max_length=200, null=True)
    date = models.CharField(max_length=30, null=True)
    def __str__(self):
        return f"{self.text}"
    class Meta:
        managed = False

    def to_dict(self):
        return {
            "id": self.id,
            "update": self.update,
            "date": self.date,
        }