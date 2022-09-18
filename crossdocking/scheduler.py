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
)

from shippers.views import portaria


def beginSchedule():
    scheduler = BackgroundScheduler({"apscheduler.timezone": "Europe/London"})
    scheduler.add_job(
        enviarEmailSchedule, "cron", hour="8", max_instances=1, misfire_grace_time=None
    )
    # enviarEmailSchedule()
    # updateSchedule()
    # updatePortariaDia1()
    # updateLineRequestDia1()
    # updateICDRDia1()

    #scheduler.add_job(enviarEmailSchedule, 'interval', seconds = 10, max_instances=1, misfire_grace_time=None)

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
    #scheduler.add_job(enviarEmailSchedule, 'interval', seconds = 5, max_instances=1, misfire_grace_time=None)

    # PARECE OK
    scheduler.add_job(
        updateSchedule, "cron", hour="1", max_instances=1, misfire_grace_time=None
    )
    # LOOP de 5 em 5 segundos da func "enviarEmailSchedule"
    # scheduler.add_job(updateSchedule, 'interval', seconds = 5, max_instances=1, misfire_grace_time=None)

    # BUG DE FORMATAÇÂO
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
    # BUG DE FORMATAÇÂO
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

    # BUG DE FORMATAÇÂO
    scheduler.add_job(
        updateProductionDia1,
        "cron",
        day="1",
        hour="1",
        max_instances=1,
        misfire_grace_time=None,
    )
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
