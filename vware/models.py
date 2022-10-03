from distutils.command.clean import clean
from django.db import models
from enum import Enum

# from pManagement.models import StockPackage


class ArmazemChecklistQPS(models.Model):
    choices_oem = [
        ("PSA", "PSA"),
        ("DAIMLER", "DAIMLER"),
        ("FORD", "FORD"),
        ("NISSAN", "NISSAN"),
        ("JLR", "JLR"),
        ("PORSCHE", "PORSCHE"),
        ("RENAULT", "RENAULT"),
        ("SKODA | VOLKWAGEN", "SKODA | VOLKWAGEN"),
        ("SCANIA", "SCANIA"),
        ("VOLVO", "VOLVO"),
        ("MASERATI", "MASERATI"),
    ]
    # insere um produto com os seguintes parametros na BD
    oem = models.CharField(max_length=40, choices=choices_oem, unique=True)
    qpsShipping = models.FileField(upload_to="qpsShipping/", blank="true", null="true")
    qpsPacking = models.FileField(upload_to="qpsPacking/", blank="true", null="true")
    checklist = models.FileField(upload_to="checklist/", blank="true", null="true")
    inspecaoDedicada = models.FileField(
        upload_to="procInspDelicado/", blank="true", null="true"
    )
    crossDocking = models.FileField(
        upload_to="crossDocking/", blank="true", null="true"
    )
    engenharia = models.FileField(upload_to="e  ngenharia/", blank="true", null="true")
    servicos = models.FileField(upload_to="servicos/", blank="true", null="true")
    guideLines = models.FileField(upload_to="guideLines/", blank="true", null="true")

    # produto = models.CharField(max_length=40)
    # descricao = models.CharField(max_length=240)
    # checklist = models.FileField(upload_to='media/', default='test')
    # qps = models.CharField(max_length=2000, null=True, blank=True)

    # META CLASS
    class Meta:
        verbose_name = "Clientes Shipping"
        verbose_name_plural = "Clientes Shipping"

    # TO STRING METHOD
    def __str__(self):
        return str(self.oem)


class SupplyPackage(models.Model):
    part_number = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank="true", null=True)
    comment = models.CharField(max_length=255, blank="true", null=True)
    supply_time = models.IntegerField(default=60, blank="true", null=True)
    stock = models.IntegerField(default=0, blank="true", null=True)
    inventario = models.IntegerField(default=0, blank="true", null=True)
    link = models.FileField(upload_to="SupplyPackage/",max_length=200, blank="true", null="true")
    #cliente_produto = models.ForeignKey("vware.ClienteProduto", on_delete=models.CASCADE, default=None,blank="true", null="true")


class Meta:
    verbose_name = "Supply Package"
    verbose_name_plural = "Supply Package"
    indexes = [models.Index(fields=["part_number"])]


# TO STRING METHOD
def __str__(self):
    return f"{self.part_number}"


class PackageType(Enum):
    EXP = "Expendable"
    RET = "Returnable"


class   StockPackage(models.Model):
    pn = models.CharField(max_length=50, null=False, db_index=True, blank=False)
    # produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, default=None,blank="true", null="true")
    suplyPackage = models.ManyToManyField(SupplyPackage)
    descricao = models.CharField(max_length=150, null=True)
    link = models.FileField(null=True, upload_to="StockPackage/")
    quantidade = models.CharField(max_length=50, null=True)
    inventario = models.CharField(max_length=50, null=True)
    comentario = models.CharField(max_length=255, null=True)

    # part_number_tipoEmbalagem = models.ManyToManyField(TipoEmbalagem)
    # part_number_tipoEmbalagem = models.ManyToManyField('vware.TipoEmbalagem',through='vware.TipoEmbalagem',through_fields=('part_number'))
    # part_number_produtos = models.ManyToManyField('vware.Produtos',through='vware.Produtos',through_fields=('part_number'))

    # part_number_produtos = models.ManyToManyField(Produtos)
    tipo = models.CharField(
        max_length=20,
        default=None,
        null=False,
        blank=False,
        choices=[(tag, tag.value) for tag in PackageType],
    )


# bd que é mostrada na tabela do Supply Package
class TipoEmbalagem(models.Model):
    # part_number = models.ForeignKey(StockPackage, on_delete=models.CASCADE,blank="true", null="true")
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0, blank="true", null=True)
    tempoSupply = models.IntegerField(default=60, blank="true", null=True)
    link = models.FileField(upload_to="embalagemLink/", blank="true", null="true")
    """    partNumberExpendable = models.CharField(max_length=250, null=True)
    partNumberReturnable = models.CharField(max_length=250, null=True) """
    # dois campos em cima vao virar apenas 1, que vai ser uma fk da table do StockPacka
    # BUG

    def save(self, *args, **kwargs):
        if isinstance(self.nome, str):
            self.nome = self.nome.upper()
        return super(TipoEmbalagem, self).save(*args, **kwargs)

    # META CLASS
    class Meta:
        verbose_name = "Tipo embalagem"
        verbose_name_plural = "Tipo embalagem"

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nome}"


# C:\Users\PMARTI30\Desktop\visteon\DownloadedLink


# META CLASS
class Meta:
    verbose_name = "Stock Package"
    verbose_name_plural = "Stock Package"
    indexes = [models.Index(fields=["pn"])]


# TO STRING METHOD
def __str__(self):
    return f"{self.pn}"


#
class ClientesOEM(models.Model):
    oem = models.CharField(max_length=40, unique=True)
    suplyPackage = models.ManyToManyField(SupplyPackage)
    #Aqui à de ser para por uma chave estranja 
    # cliente_prod = models.ForeignKey(ClienteProduto, on_delete=models.CASCADE, default=None,blank="true", null="true")
    # produto = models.ManyToManyField(Produtos)

    # META CLASS
    class Meta:
        verbose_name = "Clientes_OEM"
        verbose_name_plural = "Clientes_OEM"

    # TO STRING METHOD
    def __str__(self):
        return str(self.oem)


class Produtos(models.Model):
    cliente = models.ForeignKey(ClientesOEM, null=True, on_delete=models.SET_NULL)#ITS IN SERVER AND ITS NEEDED
    tipo = models.ForeignKey(
        "vware.TipoEmbalagem", on_delete=models.CASCADE, default=None, null=True
    )
    nome = models.CharField(max_length=100)

    # META CLASS
    class Meta:
        verbose_name = "Produtos"
        verbose_name_plural = "Produtos"

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nome}"

class ClienteProduto(models.Model):
    cliente = models.ForeignKey(ClientesOEM, on_delete=models.CASCADE,default=None)
    comment = models.CharField(max_length=200, default=None, blank=True, null=True)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE,default=None)
    supply_pkg = models.ManyToManyField(SupplyPackage)


class Prodlines(models.Model):
    nome = models.CharField(max_length=100)

    # META CLASS
    class Meta:
        verbose_name = "Prodline"
        verbose_name_plural = "Prodline"

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nome}"


class LinksShippingOperations(models.Model):
    link1 = models.CharField(max_length=150)
    link2 = models.CharField(max_length=150)
    link3 = models.CharField(max_length=150)
    link4 = models.CharField(max_length=150)
    link5 = models.CharField(max_length=150)
    link6 = models.CharField(max_length=150)
    link7 = models.CharField(max_length=150)
    link8 = models.CharField(max_length=150)
    others = models.CharField(max_length=150)
    requestShippers = models.CharField(max_length=150)

    # META CLASS
    class Meta:
        verbose_name = "Link Operation"
        verbose_name_plural = "Link Operation"


class ShippingOperation(models.Model):
    one = models.FileField(upload_to="shipping/one/", blank="true", null="true")
    two = models.FileField(upload_to="shipping/two/", blank="true", null="true")
    three = models.FileField(upload_to="shipping/three/", blank="true", null="true")
    four = models.FileField(upload_to="shipping/four/", blank="true", null="true")
    five = models.FileField(upload_to="shipping/five/", blank="true", null="true")
    six = models.FileField(upload_to="shipping/six/", blank="true", null="true")
    seven = models.FileField(upload_to="shipping/seven/", blank="true", null="true")
    eight = models.FileField(upload_to="shipping/eight/", blank="true", null="true")
    checklist = models.FileField(
        upload_to="shipping/checklist/", blank="true", null="true"
    )
    others = models.FileField(upload_to="shipping/others/", blank="true", null="true")
    requestShippers = models.FileField(
        upload_to="shipping/requestShippers/", blank="true", null="true"
    )

    # META CLASS
    class Meta:
        verbose_name = "Shipping Operation"
        verbose_name_plural = "Shipping Operation"


class ReceivingOperation(models.Model):
    one = models.FileField(upload_to="receiving/one/", blank="true", null="true")
    two = models.FileField(upload_to="receiving/two/", blank="true", null="true")
    three = models.FileField(upload_to="receiving/three/", blank="true", null="true")
    four = models.FileField(upload_to="receiving/four/", blank="true", null="true")
    five = models.FileField(upload_to="receiving/five/", blank="true", null="true")
    six = models.FileField(upload_to="receiving/six/", blank="true", null="true")
    seven = models.FileField(upload_to="receiving/seven/", blank="true", null="true")
    eight = models.FileField(upload_to="receiving/eight/", blank="true", null="true")
    nine = models.FileField(upload_to="receiving/nine/", blank="true", null="true")

    # META CLASS
    class Meta:
        verbose_name = "Receiving Operation"
        verbose_name_plural = "Receiving Operation"


class Crossdocking(models.Model):
    ford = models.FileField(upload_to="crossdocking/ford/", blank="true", null="true")
    psa = models.FileField(upload_to="crossdocking/psa/", blank="true", null="true")
    scania = models.FileField(
        upload_to="crossdocking/scania/", blank="true", null="true"
    )
    volvo = models.FileField(upload_to="crossdocking/volvo/", blank="true", null="true")

    # META CLASS
    class Meta:
        verbose_name = "Crossdocking"
        verbose_name_plural = "Crossdocking"


class Procedimentos(models.Model):
    docOne = models.FileField(
        upload_to="procedimentos/documentacao/one/", blank="true", null="true"
    )
    docTwo = models.FileField(
        upload_to="procedimentos/documentacao/two/", blank="true", null="true"
    )
    docThree = models.FileField(
        upload_to="procedimentos/documentacao/three/", blank="true", null="true"
    )
    docFour = models.FileField(
        upload_to="procedimentos/documentacao/four/", blank="true", null="true"
    )
    docFive = models.FileField(
        upload_to="procedimentos/documentacao/five/", blank="true", null="true"
    )
    docSix = models.FileField(
        upload_to="procedimentos/documentacao/six/", blank="true", null="true"
    )
    docSeven = models.FileField(
        upload_to="procedimentos/documentacao/seven/", blank="true", null="true"
    )
    docEight = models.FileField(
        upload_to="procedimentos/documentacao/eight/", blank="true", null="true"
    )
    docNine = models.FileField(
        upload_to="procedimentos/documentacao/nine/", blank="true", null="true"
    )
    anexoOne = models.FileField(
        upload_to="procedimentos/anexos/one/", blank="true", null="true"
    )
    anexoTwo = models.FileField(
        upload_to="procedimentos/anexos/two/", blank="true", null="true"
    )
    anexoThree = models.FileField(
        upload_to="procedimentos/anexos/three/", blank="true", null="true"
    )
    anexoFour = models.FileField(
        upload_to="procedimentos/anexos/four/", blank="true", null="true"
    )
    anexoFive = models.FileField(
        upload_to="procedimentos/anexos/five/", blank="true", null="true"
    )
    anexoSix = models.FileField(
        upload_to="procedimentos/anexos/six/", blank="true", null="true"
    )
    anexoSeven = models.FileField(
        upload_to="procedimentos/anexos/seven/", blank="true", null="true"
    )
    anexoEight = models.FileField(
        upload_to="procedimentos/anexos/eight/", blank="true", null="true"
    )
    anexoNine = models.FileField(
        upload_to="procedimentos/anexos/nine/", blank="true", null="true"
    )
    qpsOne = models.FileField(
        upload_to="procedimentos/qps/one/", blank="true", null="true"
    )
    qpsTwo = models.FileField(
        upload_to="procedimentos/qps/two/", blank="true", null="true"
    )
    qpsThree = models.FileField(
        upload_to="procedimentos/qps/three/", blank="true", null="true"
    )
    qpsFour = models.FileField(
        upload_to="procedimentos/qps/four/", blank="true", null="true"
    )
    qpsFive = models.FileField(
        upload_to="procedimentos/qps/five/", blank="true", null="true"
    )
    qpsSix = models.FileField(
        upload_to="procedimentos/qps/six/", blank="true", null="true"
    )
    qpsSeven = models.FileField(
        upload_to="procedimentos/qps/seven/", blank="true", null="true"
    )
    qpsEight = models.FileField(
        upload_to="procedimentos/qps/eight/", blank="true", null="true"
    )
    qpsNine = models.FileField(
        upload_to="procedimentos/qps/nine/", blank="true", null="true"
    )

    # META CLASS
    class Meta:
        verbose_name = "Procedimentos"
        verbose_name_plural = "Procedimentos"


class Others(models.Model):
    one = models.FileField(upload_to="others/one/", blank="true", null="true")
    two = models.FileField(upload_to="others/two/", blank="true", null="true")
    three = models.FileField(upload_to="others/three/", blank="true", null="true")
    four = models.FileField(upload_to="others/four/", blank="true", null="true")
    five = models.FileField(upload_to="others/five/", blank="true", null="true")

    # META CLASS
    class Meta:
        verbose_name = "Others"
        verbose_name_plural = "Others"
