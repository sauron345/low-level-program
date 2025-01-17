from django.shortcuts import render
from django.views import View


class StateHandler(View):

    _TEMPLATE_NAME = "block-c/state.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self._TEMPLATE_NAME,
            {'message': ''}
        )
