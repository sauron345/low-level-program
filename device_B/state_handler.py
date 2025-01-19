from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class StateHandler(APIView):

    def get(self, request, *args, **kwargs):
        from recruitment_task_krypton.startup import dev_b_storage_handler

        frames_data = dev_b_storage_handler.get_data()

        return Response(frames_data, status=status.HTTP_200_OK)
