from django.apps import AppConfig


class ReceivingConfig(AppConfig):
    name = "receiving"

    def ready(self):
        from .scheduler import beginSchedule

        beginSchedule()
