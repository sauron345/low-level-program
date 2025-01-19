from django.urls import path

from device_B.frames_sender_handler import FramesSenderHandler
from device_B.state_handler import StateHandler

urlpatterns = [
    path('state/', StateHandler.as_view(), name='state'),
    path('frames-sender/', FramesSenderHandler.as_view(), name='frames-sender'),
    path('edit-config/', FramesSenderHandler.as_view(), name='edit-config'),
]
