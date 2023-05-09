from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

from .views import atualizarAgeing, enviarEmailsICDR, adiciona_val_vermelhos_automatico_Supply, testeSchedule,sendRelatorioDiarioSupply
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

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
    """ scheduler.add_job(
        adiciona_val_vermelhos_automatico_Supply,
        "interval",
        minutes="10",
        max_instances=1,
        misfire_grace_time=None,
    ) """
    
    scheduler.add_job(adiciona_val_vermelhos_automatico_Supply, 'interval', minutes = 10, max_instances=1, misfire_grace_time=None)
    #scheduler.add_job(sendRelatorioDiarioSupply, 'interval', minutes = 5, max_instances=1, misfire_grace_time=None)
    scheduler.add_job(testeSchedule, 'interval', minutes = 20, max_instances=1, misfire_grace_time=None)
    # scheduler.add_job(atualizarAgeing, 'cron', hour='1', minute='10', max_instances=1, misfire_grace_time=None)
    scheduler.start()
