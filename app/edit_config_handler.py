from django.shortcuts import render
from django.views import View

from app.arithmetic_operator_form import ArithmeticOperatorForm
from app.reset_frame_form import ResetFrameForm
from block_C.arithmetic_operation import ArithmeticOperation
from recruitment_task_krypton.string_frame_converter import StringFrameConverter


class EditConfigHandler(View):

    _TEMPLATE_NAME = "app/edit-config.html"

    def get(self, request, *args, **kwargs):
        forms = [ResetFrameForm(), ArithmeticOperatorForm()]

        return render(
            request,
            self._TEMPLATE_NAME,
            {'forms': forms}
        )

    def post(self, request):
        reset_frame_form = ResetFrameForm(request.POST)
        arithmetic_operator_form = ArithmeticOperatorForm(request.POST)

        if reset_frame_form.is_valid() and arithmetic_operator_form.is_valid():
            self._set_reset_frame_if_valid(reset_frame_form)
            self._arithmetic_operation(arithmetic_operator_form)

            forms = [ResetFrameForm(), ArithmeticOperatorForm()]

            return render(request, self._TEMPLATE_NAME, {'forms': forms})

        return render(request, self._TEMPLATE_NAME, {
            'forms': [reset_frame_form, arithmetic_operator_form]
        })

    def _set_reset_frame_if_valid(self, reset_frame_form):
        reset_frame = reset_frame_form.cleaned_data['reset_frame_form']
        str_frame_converter = StringFrameConverter(reset_frame)

        bytes_frame = str_frame_converter.get_in_bytes()
        if bytes_frame:
            from recruitment_task_krypton.startup import watchdog_obj
            watchdog_obj.reset_frame = bytes_frame
        else:
            print("Passed invalid frame")

    def _arithmetic_operation(self, arithmetic_operator_form):
        arithmetic_operator = arithmetic_operator_form.cleaned_data['arithmetic_operator_form']

        if arithmetic_operator in ['+', '-', '*', '/', '**']:
            ArithmeticOperation.operator = arithmetic_operator
        else:
            print("Passed invalid char for arithmetic operator")
