from django.db import models


class LineRequestProcessing(models.Model):
    horaPedido = models.CharField(max_length=50, null=True)
    partNumber = models.CharField(max_length=50, null=True)
    linha = models.CharField(max_length=50, null=True)
    requisitante = models.CharField(max_length=50, null=True)
    receiver = models.CharField(max_length=50, null=True)
    justificacao = models.CharField(max_length=50, null=True)
    comentario = models.CharField(max_length=250, null=True)

    # META CLASS
    class Meta:
        verbose_name = "Line Request Processing"
        verbose_name_plural = "Line Request Processing"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.partNumber}"


class LineRequestFinished(models.Model):
    horaPedido = models.CharField(max_length=50, null=True)
    partNumber = models.CharField(max_length=50, null=True)
    linha = models.CharField(max_length=50, null=True)
    requisitante = models.CharField(max_length=50, null=True)
    receiver = models.CharField(max_length=50, null=True)
    justificacao = models.CharField(max_length=50, null=True)
    comentario = models.CharField(max_length=250, null=True)

    # META CLASS
    class Meta:
        verbose_name = "Line Request Finished"
        verbose_name_plural = "Line Request Finished"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.horaPedido + ' part-number: ' + self.partNumber}"


class LineRequestFinishedHistory(models.Model):
    horaPedido = models.CharField(max_length=50, null=True)
    partNumber = models.CharField(max_length=50, null=True)
    linha = models.CharField(max_length=50, null=True)
    requisitante = models.CharField(max_length=50, null=True)
    receiver = models.CharField(max_length=50, null=True)
    justificacao = models.CharField(max_length=50, null=True)
    comentario = models.CharField(max_length=250, null=True)

    # META CLASS
    class Meta:
        verbose_name = "Line Request Finished - History"
        verbose_name_plural = "Line Request Finished - History"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.horaPedido + ' part-number: ' + self.partNumber}"


class Line(models.Model):
    linha = models.CharField(max_length=50, null=True)

    # META CLASS
    class Meta:
        verbose_name = "Lines"
        verbose_name_plural = "Lines"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.linha}"


class Justification(models.Model):
    justificacao = models.CharField(max_length=150, null=True)

    # META CLASS
    class Meta:
        verbose_name = "Justifications"
        verbose_name_plural = "Justifications"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.justificacao}"


class LastUpdate(models.Model):
    data = models.CharField(max_length=50, null=True)
    redHour = models.IntegerField(null=True)
    yellowHour = models.IntegerField(null=True)
    lastUpdateRed = models.IntegerField(null=True)

    # META CLASS
    class Meta:
        verbose_name = "Last Update Date"
        verbose_name_plural = "Last Update Date"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.data}"


class TaskBrowse(models.Model):
    taskID = models.CharField(max_length=50, null=True)
    waveID = models.CharField(max_length=50, null=True)
    taskType = models.CharField(max_length=50, null=True)
    fromPart = models.CharField(max_length=50, null=True)
    fromStorageZone = models.CharField(max_length=50, null=True)
    toLocation = models.CharField(max_length=50, null=True)
    createdDate = models.CharField(max_length=50, null=True)
    createdTime = models.CharField(max_length=50, null=True)

    # META CLASS
    class Meta:
        verbose_name = "Task Browse"
        verbose_name_plural = "Task Browse"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.taskID}"


class AreaA(models.Model):
    storageZone = models.CharField(max_length=50, null=True)

    # META CLASS
    class Meta:
        verbose_name = "Area A - Storage Zone"
        verbose_name_plural = "Area A - Storage Zone"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.storageZone}"


class AreaB(models.Model):
    storageZone = models.CharField(max_length=50, null=True)

    # META CLASS
    class Meta:
        verbose_name = "Area B - Storage Zone"
        verbose_name_plural = "Area B - Storage Zone"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.storageZone}"


class Kardex(models.Model):
    storageZone = models.CharField(max_length=50, null=True)

    # META CLASS
    class Meta:
        verbose_name = "Kardex - Storage Zone"
        verbose_name_plural = "Kardex - Storage Zone"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.storageZone}"


class ReceivingPosicao1Items(models.Model):
    item = models.CharField(max_length=150, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)
    posicao = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 1 - Items"
        verbose_name_plural = "Receiving Posicao 1 - Items"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.item}"


class ReceivingPosicao2Items(models.Model):
    item = models.CharField(max_length=150, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)
    posicao = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 2 - Items"
        verbose_name_plural = "Receiving Posicao 2 - Items"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.item}"


class ReceivingPosicao3Items(models.Model):
    item = models.CharField(max_length=150, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)
    posicao = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 3 - Items"
        verbose_name_plural = "Receiving Posicao 3 - Items"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.item}"


class ReceivingPosicao4Items(models.Model):
    item = models.CharField(max_length=150, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)
    posicao = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 4 - Items"
        verbose_name_plural = "Receiving Posicao 4 - Items"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.item}"


class ReceivingPosicao5Items(models.Model):
    item = models.CharField(max_length=150, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)
    posicao = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 5 - Items"
        verbose_name_plural = "Receiving Posicao 5 - Items"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.item}"


class ReceivingPosicao6Items(models.Model):
    item = models.CharField(max_length=150, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)
    posicao = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 6 - Items"
        verbose_name_plural = "Receiving Posicao 6 - Items"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.item}"


class ReceivingPosicao7Items(models.Model):
    item = models.CharField(max_length=150, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)
    posicao = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 7 - Items"
        verbose_name_plural = "Receiving Posicao 7 - Items"
        managed = True

    # TO STRING METHODmodels
    def __str__(self):
        return f"{self.item}"


class ReceivingPosicao8Items(models.Model):
    item = models.CharField(max_length=150, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)
    posicao = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 8 - Items"
        verbose_name_plural = "Receiving Posicao 8 - Items"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.item}"


class ReceivingSubItems(models.Model):
    item = models.CharField(max_length=150, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)
    usar = models.CharField(max_length=50, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving - Sub items"
        verbose_name_plural = "Receiving - Sub items"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.item}"


class ReceivingSubItemsTipo(models.Model):
    tipo = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving - Sub items - Tipos"
        verbose_name_plural = "Receiving - Sub items - Tipos"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.tipo}"


class ReceivingPosicao1SubItems(models.Model):
    idDia = models.CharField(max_length=150, blank="true", null=True)
    item = models.CharField(max_length=150, blank="true", null=True)
    ok = models.BooleanField(default=None, blank="true", null=True)
    nok = models.BooleanField(default=None, blank="true", null=True)
    comentario = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 1 - Sub items"
        verbose_name_plural = "Receiving Posicao 1 - Sub items"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.idDia}"


class ReceivingPosicao2SubItems(models.Model):
    idDia = models.CharField(max_length=150, blank="true", null=True)
    item = models.CharField(max_length=150, blank="true", null=True)
    ok = models.BooleanField(default=None, blank="true", null=True)
    nok = models.BooleanField(default=None, blank="true", null=True)
    comentario = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 2 - Sub items"
        verbose_name_plural = "Receiving Posicao 2 - Sub items"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.idDia}"


class ReceivingPosicao3SubItems(models.Model):
    idDia = models.CharField(max_length=150, blank="true", null=True)
    item = models.CharField(max_length=150, blank="true", null=True)
    ok = models.BooleanField(default=None, blank="true", null=True)
    nok = models.BooleanField(default=None, blank="true", null=True)
    comentario = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 3 - Sub items"
        verbose_name_plural = "Receiving Posicao 3 - Sub items"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.idDia}"


class ReceivingPosicao4SubItems(models.Model):
    idDia = models.CharField(max_length=150, blank="true", null=True)
    item = models.CharField(max_length=150, blank="true", null=True)
    ok = models.BooleanField(default=None, blank="true", null=True)
    nok = models.BooleanField(default=None, blank="true", null=True)
    comentario = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 4 - Sub items"
        verbose_name_plural = "Receiving Posicao 4 - Sub items"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.idDia}"


class ReceivingPosicao5SubItems(models.Model):
    idDia = models.CharField(max_length=150, blank="true", null=True)
    item = models.CharField(max_length=150, blank="true", null=True)
    ok = models.BooleanField(default=None, blank="true", null=True)
    nok = models.BooleanField(default=None, blank="true", null=True)
    comentario = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 5 - Sub items"
        verbose_name_plural = "Receiving Posicao 5 - Sub items"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.idDia}"


class ReceivingPosicao6SubItems(models.Model):
    idDia = models.CharField(max_length=150, blank="true", null=True)
    item = models.CharField(max_length=150, blank="true", null=True)
    ok = models.BooleanField(default=None, blank="true", null=True)
    nok = models.BooleanField(default=None, blank="true", null=True)
    comentario = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 6 - Sub items"
        verbose_name_plural = "Receiving Posicao 6 - Sub items"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.idDia}"


class ReceivingPosicao7SubItems(models.Model):
    idDia = models.CharField(max_length=150, blank="true", null=True)
    item = models.CharField(max_length=150, blank="true", null=True)
    ok = models.BooleanField(default=None, blank="true", null=True)
    nok = models.BooleanField(default=None, blank="true", null=True)
    comentario = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 7 - Sub items"
        verbose_name_plural = "Receiving Posicao 7 - Sub items"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.idDia}"


class ReceivingPosicao8SubItems(models.Model):
    idDia = models.CharField(max_length=150, blank="true", null=True)
    item = models.CharField(max_length=150, blank="true", null=True)
    ok = models.BooleanField(default=None, blank="true", null=True)
    nok = models.BooleanField(default=None, blank="true", null=True)
    comentario = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 8 - Sub items"
        verbose_name_plural = "Receiving Posicao 8 - Sub items"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.idDia}"


class ReceivingPosicao1Historico(models.Model):
    dataPosicao = models.CharField(max_length=150, blank="true", null=True)
    item = models.CharField(max_length=150, blank="true", null=True)
    comentarioFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    comentarioInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    responsavelInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    responsavelFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    dataFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    dataInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    horaFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    horaInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    fimTurnoOk = models.BooleanField(default=None, blank="true", null=True)
    fimTurnoNok = models.BooleanField(default=None, blank="true", null=True)
    inicioTurnoOk = models.BooleanField(default=None, blank="true", null=True)
    inicioTurnoNok = models.BooleanField(default=None, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 1 - Historic"
        verbose_name_plural = "Receiving Posicao 1 - Historic"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.dataPosicao}"


class ReceivingPosicao2Historico(models.Model):
    dataPosicao = models.CharField(max_length=150, blank="true", null=True)
    item = models.CharField(max_length=150, blank="true", null=True)
    comentarioFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    comentarioInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    responsavelInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    responsavelFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    dataFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    dataInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    horaFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    horaInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    fimTurnoOk = models.BooleanField(default=None, blank="true", null=True)
    fimTurnoNok = models.BooleanField(default=None, blank="true", null=True)
    inicioTurnoOk = models.BooleanField(default=None, blank="true", null=True)
    inicioTurnoNok = models.BooleanField(default=None, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 2 - Historic"
        verbose_name_plural = "Receiving Posicao 2 - Historic"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.dataPosicao}"


class ReceivingPosicao3Historico(models.Model):
    dataPosicao = models.CharField(max_length=150, blank="true", null=True)
    item = models.CharField(max_length=150, blank="true", null=True)
    comentarioFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    comentarioInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    responsavelInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    responsavelFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    dataFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    dataInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    horaFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    horaInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    fimTurnoOk = models.BooleanField(default=None, blank="true", null=True)
    fimTurnoNok = models.BooleanField(default=None, blank="true", null=True)
    inicioTurnoOk = models.BooleanField(default=None, blank="true", null=True)
    inicioTurnoNok = models.BooleanField(default=None, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 3 - Historic"
        verbose_name_plural = "Receiving Posicao 3 - Historic"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.dataPosicao}"


class ReceivingPosicao4Historico(models.Model):
    dataPosicao = models.CharField(max_length=150, blank="true", null=True)
    item = models.CharField(max_length=150, blank="true", null=True)
    comentarioFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    comentarioInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    responsavelInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    responsavelFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    dataFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    dataInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    horaFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    horaInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    fimTurnoOk = models.BooleanField(default=None, blank="true", null=True)
    fimTurnoNok = models.BooleanField(default=None, blank="true", null=True)
    inicioTurnoOk = models.BooleanField(default=None, blank="true", null=True)
    inicioTurnoNok = models.BooleanField(default=None, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 4 - Historic"
        verbose_name_plural = "Receiving Posicao 4 - Historic"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.dataPosicao}"


class ReceivingPosicao5Historico(models.Model):
    dataPosicao = models.CharField(max_length=150, blank="true", null=True)
    item = models.CharField(max_length=150, blank="true", null=True)
    comentarioFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    comentarioInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    responsavelInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    responsavelFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    dataFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    dataInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    horaFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    horaInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    fimTurnoOk = models.BooleanField(default=None, blank="true", null=True)
    fimTurnoNok = models.BooleanField(default=None, blank="true", null=True)
    inicioTurnoOk = models.BooleanField(default=None, blank="true", null=True)
    inicioTurnoNok = models.BooleanField(default=None, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 5 - Historic"
        verbose_name_plural = "Receiving Posicao 5 - Historic"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.dataPosicao}"


class ReceivingPosicao6Historico(models.Model):
    dataPosicao = models.CharField(max_length=150, blank="true", null=True)
    item = models.CharField(max_length=150, blank="true", null=True)
    comentarioFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    comentarioInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    responsavelInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    responsavelFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    dataFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    dataInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    horaFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    horaInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    fimTurnoOk = models.BooleanField(default=None, blank="true", null=True)
    fimTurnoNok = models.BooleanField(default=None, blank="true", null=True)
    inicioTurnoOk = models.BooleanField(default=None, blank="true", null=True)
    inicioTurnoNok = models.BooleanField(default=None, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 6 - Historic"
        verbose_name_plural = "Receiving Posicao 6 - Historic"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.dataPosicao}"


class ReceivingPosicao7Historico(models.Model):
    dataPosicao = models.CharField(max_length=150, blank="true", null=True)
    item = models.CharField(max_length=150, blank="true", null=True)
    comentarioFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    comentarioInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    responsavelInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    responsavelFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    dataFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    dataInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    horaFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    horaInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    fimTurnoOk = models.BooleanField(default=None, blank="true", null=True)
    fimTurnoNok = models.BooleanField(default=None, blank="true", null=True)
    inicioTurnoOk = models.BooleanField(default=None, blank="true", null=True)
    inicioTurnoNok = models.BooleanField(default=None, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 7 - Historic"
        verbose_name_plural = "Receiving Posicao 7 - Historic"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.dataPosicao}"


class ReceivingPosicao8Historico(models.Model):
    dataPosicao = models.CharField(max_length=150, blank="true", null=True)
    item = models.CharField(max_length=150, blank="true", null=True)
    comentarioFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    comentarioInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    responsavelInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    responsavelFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    dataFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    dataInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    horaFinalTurno = models.CharField(max_length=150, blank="true", null=True)
    horaInicioTurno = models.CharField(max_length=150, blank="true", null=True)
    fimTurnoOk = models.BooleanField(default=None, blank="true", null=True)
    fimTurnoNok = models.BooleanField(default=None, blank="true", null=True)
    inicioTurnoOk = models.BooleanField(default=None, blank="true", null=True)
    inicioTurnoNok = models.BooleanField(default=None, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving Posicao 8 - Historic"
        verbose_name_plural = "Receiving Posicao 8 - Historic"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.dataPosicao}"


class HabilitarQuadrados(models.Model):
    posicao = models.CharField(max_length=150, blank="true", null=True)
    valor = models.CharField(max_length=50, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving - TPM - Configuration"
        verbose_name_plural = "Receiving - TPM - Configuration"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.posicao}"


class DefinirTempos(models.Model):
    turno = models.CharField(max_length=150, blank="true", null=True)
    inicio = models.CharField(max_length=150, blank="true", null=True)
    final = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving - TPM - Configuration - tempos"
        verbose_name_plural = "Receiving - TPM - Configuration - tempos"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.turno}"


class ICDR(models.Model):
    aberturaICDR = models.CharField(max_length=150, blank="true", null=True)
    ageing = models.CharField(max_length=150, blank="true", null=True)
    nAno = models.CharField(max_length=150, blank="true", null=True)
    fornecedor = models.CharField(max_length=150, blank="true", null=True)
    partnumber = models.CharField(max_length=150, blank="true", null=True)
    quantidade = models.CharField(max_length=150, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)
    simNao = models.CharField(max_length=150, blank="true", null=True)
    responsavel = models.CharField(max_length=150, blank="true", null=True)
    departamento = models.CharField(max_length=150, blank="true", null=True)
    comentarioFecho = models.CharField(max_length=2000, blank="true", null=True)
    rctUnpCheck = models.CharField(max_length=50, blank="true", null=True)
    cycleCountCheck = models.CharField(max_length=50, blank="true", null=True)
    consumption = models.CharField(max_length=500, blank="true", null=True)
    po = models.CharField(max_length=2000, blank="true", null=True)
    date = models.CharField(max_length=150, blank="true", null=True)
    comentarioFechoICDR = models.CharField(max_length=2000, blank="true", null=True)
    cycleCount = models.CharField(max_length=150, blank="true", null=True)
    dataCycleCount = models.CharField(max_length=150, blank="true", null=True)
    unCost = models.CharField(max_length=150, blank="true", null=True)
    totalCost = models.CharField(max_length=150, blank="true", null=True)
    comentarioReporting = models.CharField(max_length=150, blank="true", null=True)
    auditCheck = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving - ICDR"
        verbose_name_plural = "Receiving - ICDR"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nAno}"


class ICDRBackup(models.Model):
    aberturaICDR = models.CharField(max_length=150, blank="true", null=True)
    ageing = models.CharField(max_length=150, blank="true", null=True)
    nAno = models.CharField(max_length=150, blank="true", null=True)
    fornecedor = models.CharField(max_length=150, blank="true", null=True)
    partnumber = models.CharField(max_length=150, blank="true", null=True)
    quantidade = models.CharField(max_length=150, blank="true", null=True)
    tipo = models.CharField(max_length=150, blank="true", null=True)
    simNao = models.CharField(max_length=150, blank="true", null=True)
    responsavel = models.CharField(max_length=150, blank="true", null=True)
    departamento = models.CharField(max_length=150, blank="true", null=True)
    comentarioFecho = models.CharField(max_length=2000, blank="true", null=True)
    rctUnpCheck = models.CharField(max_length=50, blank="true", null=True)
    cycleCountCheck = models.CharField(max_length=50, blank="true", null=True)
    consumption = models.CharField(max_length=500, blank="true", null=True)
    po = models.CharField(max_length=2000, blank="true", null=True)
    date = models.CharField(max_length=150, blank="true", null=True)
    comentarioFechoICDR = models.CharField(max_length=2000, blank="true", null=True)
    cycleCount = models.CharField(max_length=150, blank="true", null=True)
    dataCycleCount = models.CharField(max_length=150, blank="true", null=True)
    unCost = models.CharField(max_length=150, blank="true", null=True)
    totalCost = models.CharField(max_length=150, blank="true", null=True)
    comentarioReporting = models.CharField(max_length=150, blank="true", null=True)
    auditCheck = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving - ICDR - BACKUP"
        verbose_name_plural = "Receiving - ICDR - BACKUP"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nAno}"


class ICDRmotivo(models.Model):
    motivo = models.CharField(max_length=250, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving - ICDR - motivo"
        verbose_name_plural = "Receiving - ICDR - motivo"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.motivo}"


class ICDRultimoValor(models.Model):
    valor = models.IntegerField(blank="true", null=True)
    nome = models.CharField(max_length=150, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving - ICDR - Ultimo elemento"
        verbose_name_plural = "Receiving - ICDR - Ultimo elemento"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nome}"


class UserICDR(models.Model):
    username = models.CharField(max_length=150, blank="true", null=True)
    nome = models.CharField(max_length=150, blank="true", null=True)
    area = models.CharField(max_length=100, blank="true", null=True)
    email = models.CharField(max_length=100, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving - ICDR - Users"
        verbose_name_plural = "Receiving - ICDR - Users"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nome}"


class ListaUsersICDR(models.Model):
    nome = models.CharField(max_length=150, blank="true", null=True)
    user = models.CharField(max_length=2000, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving - ICDR - Lista Users"
        verbose_name_plural = "Receiving - ICDR - Lista Users"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nome}"


class TriggerEnvioEmailsICDR(models.Model):
    nome = models.CharField(max_length=150, blank="true", null=True)
    estado = models.CharField(max_length=150, blank="true", null=True)
    users = models.CharField(max_length=3000, blank="true", null=True)

    # META CLASS
    class Meta:
        verbose_name = "Receiving - ICDR - Alerta envio email"
        verbose_name_plural = "Receiving - ICDR - Alerta envio email"
        managed = True

    # TO STRING METHOD
    def __str__(self):
        return f"{self.nome}"
