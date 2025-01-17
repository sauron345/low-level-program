from django.shortcuts import render
from django.views import View


class FramesSenderHandler(View):

    _TEMPLATE_NAME = "block-c/frames-sender.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self._TEMPLATE_NAME,
            {'message': ''}
        )
