from apscheduler.schedulers.background import BackgroundScheduler

from .views import guardaFicheiroHistorico

def beginSchedule():
    
    scheduler = BackgroundScheduler({"apscheduler.timezone": "Europe/London"})
    #scheduler.add_job(guardaFicheiroHistorico, 'interval', seconds = 5, max_instances=1, misfire_grace_time=None) #5 em 5 secs
    #scheduler.add_job(guardaFicheiroHistorico, "cron", day="1", hour="1", max_instances=1, misfire_grace_time=None) #primeiro dia do mês
    scheduler.start()
 
    """ for job in scheduler.get_jobs():        
        print("-> ", job.name) """
 
