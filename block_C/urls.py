from django.urls import path

from block_C.views import StateHandler

urlpatterns = [
    path('state/', StateHandler.as_view(), name='state'),
]
