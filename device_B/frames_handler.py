from django.shortcuts import render
from django.views import View

from recruitment_task_krypton.startup import device_a_gateway


class FramesSenderHandler(View):

    _TEMPLATE_NAME = "device-b/frames-sender.html"

    def get(self, request, *args, **kwargs):
        device_a_gateway
        return render(
            request,
            self._TEMPLATE_NAME,
            {'message': ''}
        )
