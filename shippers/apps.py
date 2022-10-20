from django.apps import AppConfig


class ShippersConfig(AppConfig):
    name = "shippers"
    
    def ready(self):
        from .scheduler import beginSchedule    
        beginSchedule()

