from django.urls import path, include

from app import views
from app.edit_config_handler import EditConfigHandler

urlpatterns = [
    path('', views.control_panel, name='control-panel'),
    path('edit-config/', EditConfigHandler.as_view(), name='app-edit-config'),
    path('device-a/', include('device_A.urls')),
    path('device-b/', include('device_B.urls')),
    path('block-c/', include('block_C.urls')),
]
