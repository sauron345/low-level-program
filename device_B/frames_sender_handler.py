from django.shortcuts import render
from django.views import View

from device_B.frames_sender_form import FramesSenderForm
from recruitment_task_krypton.string_frame_converter import StringFrameConverter


class FramesSenderHandler(View):

    _TEMPLATE_NAME = "device-b/frames-sender.html"

    def get(self, request):
        form = FramesSenderForm()
        return render(request, self._TEMPLATE_NAME, {'form': form})

    def post(self, request):
        form = FramesSenderForm(request.POST)

        if form.is_valid():
            frames = form.cleaned_data['frames']
            frames = frames.replace('\r', '')
            for frame_str in frames.split('\n'):
                self._send_frame_to_dev_b_if_valid(frame_str)
            form = FramesSenderForm()
            return render(request, self._TEMPLATE_NAME, {'form': form})

        return render(request, self._TEMPLATE_NAME, {'form': form})

    def _send_frame_to_dev_b_if_valid(self, frame_str):
        str_frame_converter = StringFrameConverter(frame_str)
        bytes_frame = str_frame_converter.get_in_bytes()
        if bytes_frame:
            self._send_to_client_if_valid(bytes_frame)
        else:
            print(f"Passed frame {frame_str} is invalid")

    def _send_to_client_if_valid(self, str_bytes):
        from recruitment_task_krypton.startup import device_b_gateway_controller

        if str_bytes != 'Invalid':
            device_b_gateway_controller.send(str_bytes)
        else:
            print("Passed invalid bytes")
