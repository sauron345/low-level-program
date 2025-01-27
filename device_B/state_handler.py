from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class StateHandler(APIView):

    def get(self, request, *args, **kwargs):
        from recruitment_task_krypton.startup import dev_b_storages_handlers

        frames_data = []
        for storage_handler in dev_b_storages_handlers:
            frames_data.extend(storage_handler.get_data())
        if frames_data:
            return Response(frames_data, status=status.HTTP_200_OK)
        return Response({'error': 'Frames are not passed to the server'}, status=status.HTTP_404_NOT_FOUND)
