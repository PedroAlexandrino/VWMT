from datetime import datetime
from unicodedata import name
from apscheduler.schedulers.background import BackgroundScheduler

from .views import (
    enviarEmailSchedule,
    updateSchedule,
    updateProductionDia1,
    updateLineRequestDia1,
    updatePortariaDia1,
    updateICDRDia1,
    updatePortariaDia15,
    sendFicheiroDiarioAutomatico,
)
from shippers.views import populate_shippers_trackingPage
from receiving.views import adiciona_val_vermelhos_automatico_Supply




def beginSchedule():
    scheduler = BackgroundScheduler({"apscheduler.timezone": "Europe/London"})
    scheduler.add_job(
        enviarEmailSchedule, "cron", hour="8", max_instances=1, misfire_grace_time=None
    )
    #scheduler.add_job(populate_shippers_trackingPage, 'interval', minutes = 10, max_instances=1, misfire_grace_time=None)
    #scheduler.add_job(guardaFicheiroHistorico, "cron", day="1", hour="1", max_instances=1, misfire_grace_time=None)
    #scheduler.add_job(guardaFicheiroHistorico, 'interval', seconds = 5, max_instances=1, misfire_grace_time=None)
    # enviarEmailSchedule()
    # updateSchedule()
    # updatePortariaDia1()
    # updateLineRequestDia1()
    # updateICDRDia1()

    #scheduler.add_job(sendFicheiroDiarioAutomatico, 'interval', seconds = 15, max_instances=1, misfire_grace_time=None)

    # T*A A FUNCIONAR (enviarEmailSchedule)
    scheduler.add_job(
        enviarEmailSchedule,
        "cron",
        hour="16",
        minute="30",
        max_instances=1,
        misfire_grace_time=None,
    )
    scheduler.add_job(
        enviarEmailSchedule, "cron", hour="22", max_instances=1, misfire_grace_time=None
    )
    # LOOP de 5 em 5 segundos da func "enviarEmailSchedule"
    #scheduler.add_job(enviarEmailSchedule, 'interval', seconds = 10, max_instances=1, misfire_grace_time=None)
    """ teste para ver se ele não sai aos fds 
    fazer uma calendarização que faz de domingo a sexta que vai buscar os dados ao QAD para popular as tabelas para o email"""
    """ scheduler.add_job(
        sendFicheiroDiarioAutomatico, day_of_week='mon-fri', hour="22", max_instances=1, misfire_grace_time=None
    ) """
    #FUNC QUE VAI CORRER MENSALMENTE, CRIA/EDITA EXEL DAS MEDIAS POR EMPRESA
    """ scheduler.add_job(
        createExcelMediaEmpresaMensal,
        "cron",
        day="1",
        hour="1",
        max_instances=1,
        misfire_grace_time=None,
    ) 
    scheduler.add_job(
        sendFicheiroDiarioAutomatico, "cron",
        hour="9",
        minute="02",
        max_instances=1,
        misfire_grace_time=None,    
    ) """
    """ scheduler.add_job(
        sendFicheiroDiarioAutomatico, "cron",day_of_week='mon-fri',
        hour="9",
        max_instances=1,
        misfire_grace_time=None,
    ) """

    scheduler.add_job(
        updateSchedule, "cron", hour="1", max_instances=1, misfire_grace_time=None
    ) #TENS DE VER COM O NUNO SE ESTA FUNC AINDA TEM UTILIDADE
    # LOOP de 5 em 5 segundos da func "enviarEmailSchedule"
    # scheduler.add_job(updateSchedule, 'interval', seconds = 5, max_instances=1, misfire_grace_time=None)


    scheduler.add_job(
        updateLineRequestDia1,
        "cron",
        day="1",
        hour="1",
        max_instances=1,
        misfire_grace_time=None,
    )
    # LOOP de 5 em 5 segundos da func updateLineRequestDia1 NAO ESTÀ OK
    # updateLineRequestDia1()
    # scheduler.add_job(updateLineRequestDia1, 'interval', seconds = 5, max_instances=1, misfire_grace_time=None)

    scheduler.add_job(
        updatePortariaDia1,
        "cron",
        day="1",
        hour="1",
        max_instances=1,
        misfire_grace_time=None,
    )
    # scheduler.add_job(updatePortariaDia1, 'interval', seconds = 5, max_instances=1, misfire_grace_time=None)

    scheduler.add_job(
        updatePortariaDia15,
        "cron",
        day="15",
        hour="1",
        max_instances=1,
        misfire_grace_time=None,
    )
    # scheduler.add_job(updatePortariaDia15, 'interval', seconds = 5, max_instances=1, misfire_grace_time=None)

    scheduler.add_job(
        updateProductionDia1,
        "cron",
        day="1",
        hour="1",
        max_instances=1,
        misfire_grace_time=None,
    )
    """ scheduler.add_job( 
        adiciona_val_vermelhos_automatico_Supply,
        "interval",
        minutes="10",
        max_instances=1,
        misfire_grace_time=None,
    ) """
    # scheduler.add_job(updateProductionDia1, 'interval', seconds = 5, max_instances=1, misfire_grace_time=None)

    # scheduler.add_job(updateTPMDia1, 'cron', day='1', hour='1', max_instances=1, misfire_grace_time=None)
    scheduler.add_job(
        updateICDRDia1,
        "cron",
        day="1",
        hour="1",
        max_instances=1,
        misfire_grace_time=None,
    )
    # scheduler.add_job(updateICDRDia1, 'interval', seconds = 5, max_instances=1, misfire_grace_time=None)
    for job in scheduler.get_jobs():
        print("-> ", job.name)
    scheduler.start()
