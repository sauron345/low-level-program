from django.core.signals import request_started

from django.apps import AppConfig

from recruitment_task_krypton.startup import main_start


class Gateways(AppConfig):
    name = 'app'

    def ready(self):

        def start_gateway(**kwargs):
            main_start()

        request_started.connect(start_gateway)
