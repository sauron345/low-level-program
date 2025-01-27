from django.urls import path

from block_C.state_handler import StateHandler

urlpatterns = [
    path('state/', StateHandler.as_view(), name='block-c-state'),
]
