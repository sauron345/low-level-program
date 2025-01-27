from django.shortcuts import render
from django.views import View

from app.forms.arithmetic_operator_form import ArithmeticOperatorForm
from app.forms.reset_frame_form import ResetFrameForm
from block_C.arithmetic_operation import ArithmeticOperation
from recruitment_task_krypton.utils.string_frame_converter import StringFrameConverter


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
            reset_frame = reset_frame_form.cleaned_data['reset_frame_form']
            arithmetic_operator = arithmetic_operator_form.cleaned_data['arithmetic_operator_form']

            if reset_frame:
                self._set_reset_frame_if_valid(reset_frame)
            if arithmetic_operator:
                self._set_arithmetic_operation_if_valid(arithmetic_operator)

            forms = [ResetFrameForm(), ArithmeticOperatorForm()]

            return render(request, self._TEMPLATE_NAME, {'forms': forms})

        return render(request, self._TEMPLATE_NAME, {
            'forms': [reset_frame_form, arithmetic_operator_form]
        })

    def _set_reset_frame_if_valid(self, reset_frame):
        str_frame_converter = StringFrameConverter(reset_frame)

        bytes_frame = str_frame_converter.get_in_bytes()
        if bytes_frame:
            from recruitment_task_krypton.startup import watchdog_obj
            watchdog_obj.reset_frame = bytes_frame
        else:
            print("Passed invalid frame")

    def _set_arithmetic_operation_if_valid(self, arithmetic_operator):
        from recruitment_task_krypton.startup import arithmetic_operation_obj

        if arithmetic_operator in ArithmeticOperation.allowed_operators():
            arithmetic_operation_obj.operator = arithmetic_operator
        else:
            print("Passed invalid char for arithmetic operator")
