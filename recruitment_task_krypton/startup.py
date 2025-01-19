import threading

from recruitment_task_krypton.device_gateway_runner import DeviceGatewayRunner
from recruitment_task_krypton.device_gateway_controller import DeviceGatewayController
from django.conf import settings
from recruitment_task_krypton.storage_handler import StorageHandler

device_a_gateway = None
device_b_gateway = None
device_a_gateway_controller = None
device_b_gateway_controller = None
dev_a_storage_handler = None
dev_b_storage_handler = None


def open_gateways():
    global device_a_gateway
    global device_b_gateway
    global device_a_gateway_controller
    global device_b_gateway_controller
    global dev_a_storage_handler
    global dev_b_storage_handler

    dev_a_storage_handler = StorageHandler(settings.BASE_DIR / 'logs_storages/device_a.json')
    dev_b_storage_handler = StorageHandler(settings.BASE_DIR / 'logs_storages/device_b.json')

    device_gateway_a_runner = DeviceGatewayRunner(device_type='A')
    device_gateway_b_runner = DeviceGatewayRunner(device_type='B', port=4000)

    device_a_gateway_controller = DeviceGatewayController(device_gateway_a_runner)
    device_b_gateway_controller = DeviceGatewayController(device_gateway_b_runner)

    device_a_gateway = threading.Thread(target=device_a_gateway_controller.run, daemon=True)
    device_b_gateway = threading.Thread(target=device_b_gateway_controller.run, daemon=True)

    device_a_gateway.start()
    device_b_gateway.start()


def close_gateways():
    device_a_gateway_controller.close()
    device_b_gateway_controller.close()

    dev_a_storage_handler.close()
    dev_b_storage_handler.close()
