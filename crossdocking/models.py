from django.db import models


class ProdlineTable(models.Model):
    day = models.CharField(max_length=50, null=True)
    line = models.CharField(max_length=50, null=True)
    site = models.CharField(max_length=50, null=True)
    due_date = models.CharField(max_length=50, null=True)
    item_number = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    to_complete = models.CharField(max_length=50, null=True)
    receiving = models.BooleanField(default=None, blank="true", null=True)
    comentarioReceiving = models.CharField(max_length=350, null=True)
    shipping = models.BooleanField(default=None, blank="true", null=True)
    comentarioShipping = models.CharField(max_length=350, null=True)
    allOkReceiving = models.BooleanField(default=None, blank="true", null=True)
    allOkShipping = models.BooleanField(default=None, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Warehouse - Production"
        verbose_name_plural = "Warehouse - Production"

    # TO STRING METHOD
    def __str__(self):
        return f"{self.day + ' ' + self.line}"


class Prodlines(models.Model):
    nome = models.CharField(max_length=100, null=True)

    # META CLASS
    class Meta:
        verbose_name = "Prodlines"
        verbose_name_plural = "Prodlines"

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nome}"


class ProdlineTableHistory(models.Model):
    day = models.CharField(max_length=50, null=True)
    line = models.CharField(max_length=50, null=True)
    site = models.CharField(max_length=50, null=True)
    due_date = models.CharField(max_length=50, null=True)
    item_number = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    to_complete = models.CharField(max_length=50, null=True)
    receiving = models.BooleanField(default=None, blank="true", null=True)
    allOkReceiving = models.BooleanField(default=None, blank="true", null=True)
    comentarioReceiving = models.CharField(max_length=350, null=True)
    shipping = models.BooleanField(default=None, blank="true", null=True)
    allOkShipping = models.BooleanField(default=None, blank="true", null=True)
    comentarioShipping = models.CharField(max_length=350, null=True)

    # META CLASS
    class Meta:
        verbose_name = "Warehouse - Production - History"
        verbose_name_plural = "Warehouse - Production - History"

    # TO STRING METHOD
    def __str__(self):
        return f"{self.day + ' ' + self.line}"


class ProdlineHistoryAllTime(models.Model):
    day = models.CharField(max_length=50, null=True)
    line = models.CharField(max_length=50, null=True)
    site = models.CharField(max_length=50, null=True)
    due_date = models.CharField(max_length=50, null=True)
    item_number = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    to_complete = models.CharField(max_length=50, null=True)
    receiving = models.BooleanField(default=None, blank="true", null=True)
    allOkReceiving = models.BooleanField(default=None, blank="true", null=True)
    comentarioReceiving = models.CharField(max_length=350, null=True)
    shipping = models.BooleanField(default=None, blank="true", null=True)
    allOkShipping = models.BooleanField(default=None, blank="true", null=True)
    comentarioShipping = models.CharField(max_length=350, null=True)

    # META CLASS
    class Meta:
        verbose_name = "Warehouse - Production - History All Time"
        verbose_name_plural = "Warehouse - Production - History All Time"

    # TO STRING METHOD
    def __str__(self):
        return f"{self.day + ' ' + self.line}"


class EmailDiarioInformacao(models.Model):
    ficheiro = models.FileField(null=True, upload_to="ConfigurationsEmail/")
    data_guardado = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return f"{self.ficheiro}"



class EmailDiarioSchedule(models.Model):
    line = models.CharField(max_length=50, null=True)
    site = models.CharField(max_length=50, null=True)
    due_date = models.CharField(max_length=50, null=True)
    item_number = models.CharField(max_length=50, null=True)
    to_complete = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)
    qty_completed = models.CharField(max_length=50, null=True)
    timeStamp = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.line}"



class EmailDiarioSchedule_view(models.Model):
    line = models.CharField(max_length=50, null=True)
    site = models.CharField(max_length=50, null=True)
    due_date = models.CharField(max_length=50, null=True)
    item_number = models.CharField(max_length=50, null=True)
    to_complete = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)
    qty_completed = models.CharField(max_length=50, null=True)
    timeStamp = models.CharField(max_length=200, null=True)

    class Meta:
        managed = False
        db_table ="informacao_email_schedule"

    # TO STRING METHOD
    def __str__(self):
        return f"{self.line}"

class KarboxSubItem(models.Model):
    pn = models.CharField(max_length=50, null=True)
    nmr_carro = models.CharField(max_length=50, null=True) 
    serial_number = models.CharField(max_length=50, null=True) 
    class Meta:
        managed = False
    # TO STRING METHOD
    def __str__(self):
        return f"{self.pn}"


class Karbox(models.Model):
    pn = models.CharField(max_length=50, null=True)
    nmr_carro = models.CharField(max_length=50, null=True) 
    serial_number = models.CharField(max_length=50, null=True) 
    subItem = models.ManyToManyField(KarboxSubItem) #models.ForeignKey(KarboxSubItem, on_delete=models.CASCADE)
    #N TENHO CERTEZA
    estado = models.CharField(max_length=50, null=True)
    class Meta:
        managed = False
    # TO STRING METHOD
    def __str__(self):
        return f"{self.pn}"
    







        