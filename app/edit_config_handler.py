from django.shortcuts import render
from django.views import View


class EditConfigHandler(View):

    _TEMPLATE_NAME = "app/edit-config.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self._TEMPLATE_NAME,
            {'message': ''}
        )
