from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from .views import atualizarAgeing, enviarEmailsICDR


def beginSchedule():
    scheduler = BackgroundScheduler({"apscheduler.timezone": "Europe/London"})
    scheduler.add_job(
        atualizarAgeing,
        "cron",
        hour="7",
        minute="25",
        max_instances=1,
        misfire_grace_time=None,
    )
    scheduler.add_job(
        enviarEmailsICDR,
        "cron",
        hour="7",
        minute="30",
        max_instances=1,
        misfire_grace_time=None,
    )
    # scheduler.add_job(atualizarAgeing, 'cron', hour='1', minute='10', max_instances=1, misfire_grace_time=None)
    scheduler.start()
