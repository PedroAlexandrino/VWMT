from enum import Enum
from django.db import models


class extraProductTable(models.Model):
    cliente = models.CharField(max_length=50, null=True)
    produto = models.CharField(max_length=50, null=True)
    embalagem = models.CharField(max_length=50, null=True)
    quantidade = models.CharField(max_length=50, null=True)
    startTime = models.CharField(max_length=50, null=True)
    dataPedido = models.CharField(max_length=50, null=True)
    dataTerminado = models.CharField(max_length=50, null=True)
    link = models.CharField(max_length=50, null=True)
    estado = models.CharField(max_length=50, null=True)
    autor = models.CharField(max_length=50, null=True)
    tempoSupply = models.IntegerField(default=0, blank="true", null=True)
    tempoSupplyRestante = models.IntegerField(default=0, blank="true", null=True)
    tempoLimite = models.CharField(max_length=50, null=True)
    ultimosDez = models.CharField(max_length=50, null=True)

    # META CLASS
    class Meta:
        verbose_name = "Request Table"
        verbose_name_plural = "Request Table"

    # TO STRING METHOD
    def __str__(self):
        return f"{self.embalagem}"


class buttonAuthorHistory(models.Model):
    embalagem = models.ForeignKey(extraProductTable, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, null=True)
    autor = models.CharField(max_length=50, null=True)
    horaAlteracao = models.CharField(max_length=50, null=True)
    horaPedido = models.CharField(max_length=50, null=True)

    # META CLASS
    class Meta:
        verbose_name = "Request History Authors"
        verbose_name_plural = "Request History Authors"

    # TO STRING METHOD
    def __str__(self):
        return f"{self.embalagem}"


class extraProductHistoric(models.Model):
    cliente = models.CharField(max_length=50, null=True)
    produto = models.CharField(max_length=50, null=True)
    embalagem = models.CharField(max_length=50, null=True)
    quantidade = models.CharField(max_length=50, null=True)
    startTime = models.CharField(max_length=50, null=True)
    dataPedido = models.CharField(max_length=50, null=True)
    dataTerminado = models.CharField(max_length=50, null=True)
    comentario = models.CharField(max_length=250, null=True)
    estado = models.CharField(max_length=50, null=True)

    # META CLASS
    class Meta:
        verbose_name = "Historic Table"
        verbose_name_plural = "Historic Table"

    # TO STRING METHOD
    def __str__(self):
        return f"{self.embalagem}"


class PartNumbersExpendable(models.Model):
    pn = models.CharField(max_length=50, null=True)
    descricao = models.CharField(max_length=150, null=True)
    link = models.CharField(max_length=50, null=True)
    quantidade = models.CharField(max_length=50, null=True)

    # META CLASS
    class Meta:
        verbose_name = "Part Numbers Expendable"
        verbose_name_plural = "Part Numbers Expendable"

    # TO STRING METHOD
    def __str__(self):
        return f"{self.pn}"


class PackageType(Enum):
    EXP = "Expendable"
    RET = "Returnable"


# C:\Users\PMARTI30\Desktop\visteon\DownloadedLink
""" class StockPackage(models.Model):
    pn = models.CharField(max_length=50, null=False, db_index=True, blank=False)
    descricao = models.CharField(max_length=150, null=True)
    link = models.FileField(null=True, upload_to="Users\PMARTI30\Downloads")
    quantidade = models.CharField(max_length=50, null=True)
    inventario = models.CharField(max_length=50, null=True)
    comentario = models.CharField(max_length=255, null=True)
    #part_number_tipoEmbalagem = models.ManyToManyField(TipoEmbalagem)
    #part_number_produtos = models.ManyToManyField(Produtos)
    tipo = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        choices=[(tag, tag.value) for tag in PackageType],
    )

    # META CLASS
    class Meta:
        verbose_name = "Stock Package"
        verbose_name_plural = "Stock Package"
        indexes = [models.Index(fields=["pn"])]

    # TO STRING METHOD
    def __str__(self):
        return f"{self.pn}" """


class PartNumbersReturnable(models.Model):
    pn = models.CharField(max_length=50, null=True)
    descricao = models.CharField(max_length=150, null=True)
    link = models.CharField(max_length=50, null=True)
    quantidade = models.CharField(max_length=50, null=True)

    # META CLASS
    class Meta:
        verbose_name = "Part Numbers Returnable"
        verbose_name_plural = "Part Numbers Returnable"

    # TO STRING METHOD
    def __str__(self):
        return f"{self.pn}"


class StockElements(models.Model):
    partNumber = models.CharField(max_length=150, null=True)
    descricao = models.CharField(max_length=150, null=True)
    link = models.CharField(max_length=150, null=True)
    expendable = models.CharField(max_length=150, null=True)
    returnable = models.CharField(max_length=150, null=True)
    quantidadeStock = models.CharField(max_length=150, null=True)

    # META CLASS
    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stock"

    # TO STRING METHOD
    def __str__(self):
        return f"{self.partNumber}"
