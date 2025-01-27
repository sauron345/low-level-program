from django.urls import path

from device_A.state_handler import StateHandler

urlpatterns = [
    path('state/', StateHandler.as_view(), name='device-a-state'),
]
