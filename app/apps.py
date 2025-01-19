from django.core.signals import request_started

from django.apps import AppConfig

from recruitment_task_krypton.startup import open_gateways


class Gateways(AppConfig):
    name = 'app'

    def ready(self):
        def start_gateway(**kwargs):
            open_gateways()

        request_started.connect(start_gateway)
