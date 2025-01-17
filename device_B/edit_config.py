from django.shortcuts import render
from django.views import View


class EditConfig(View):

    _TEMPLATE_NAME = "device-b/edit-config.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self._TEMPLATE_NAME,
            {'message': ''}
        )
