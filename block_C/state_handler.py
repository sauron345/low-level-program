from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class StateHandler(APIView):

    def get(self, request, *args, **kwargs):
        from low_level_program.startup import block_c_storage_handler

        results = block_c_storage_handler.get_data()
        if results:
            return Response(results, status=status.HTTP_200_OK)
        return Response({'error': 'Arithmetic operations not found'}, status=status.HTTP_404_NOT_FOUND)
