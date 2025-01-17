from django.urls import path, include

from block_C.edit_config_handler import EditConfigHandler
from block_C.frames_sender_handler import FramesSenderHandler
from block_C.views import StateHandler

urlpatterns = [
    path('state/', StateHandler.as_view(), name='state'),
    path('edit-config/', EditConfigHandler.as_view(), name='edit-config'),
    path('frames-sender/', FramesSenderHandler.as_view(), name='frames-sender'),
]
