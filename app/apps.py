from django.apps import AppConfig

from recruitment_task_krypton.startup import open_gateways


class Gateways(AppConfig):
    name = 'app'

    def ready(self):
        open_gateways()
