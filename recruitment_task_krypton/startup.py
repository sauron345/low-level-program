import threading

from django.core.cache import cache

from block_C.arithmetic_operation import ArithmeticOperation
from device_B.watchdog import Watchdog
from recruitment_task_krypton.device_a_gateway_controller import DeviceAGatewayController
from recruitment_task_krypton.device_b_gateway_controller import DeviceBGatewayController
from recruitment_task_krypton.device_gateway_runner import DeviceGatewayRunner
from django.conf import settings
from recruitment_task_krypton.storage_handler import StorageHandler


device_a_gateway = None
device_b_gateway = None
device_a_gateway_controller = None
device_b_gateway_controller = None
dev_a_storage_handler = None
dev_b_storage_handler = None
block_c_storage_handler = None
dev_a_clients_storage = None
dev_b_clients_storage = None
watchdog = None
watchdog_obj = None
arithmetic_operation = None


def main_start():
    if not cache.get('main_start_executed'):
        cache.set('main_start_executed', True, None)
    elif cache.get('main_start_executed'):
       return

    global device_a_gateway
    global device_b_gateway
    global device_a_gateway_controller
    global device_b_gateway_controller
    global dev_a_storage_handler
    global dev_b_storage_handler
    global block_c_storage_handler
    global dev_a_clients_storage
    global dev_b_clients_storage
    global watchdog
    global watchdog_obj
    global arithmetic_operation

    dev_a_storage_handler = StorageHandler(settings.BASE_DIR / 'logs_storages/device_a.json')
    dev_b_storage_handler = StorageHandler(settings.BASE_DIR / 'logs_storages/device_b.json')
    block_c_storage_handler = StorageHandler(settings.BASE_DIR / 'logs_storages/block_c.json')

    device_gateway_a_runner = DeviceGatewayRunner()
    device_gateway_b_runner = DeviceGatewayRunner(port=4000)

    device_a_gateway_controller = DeviceAGatewayController(device_gateway_a_runner)
    device_b_gateway_controller = DeviceBGatewayController(device_gateway_b_runner)

    device_a_gateway = threading.Thread(target=device_a_gateway_controller.run, daemon=True)
    device_b_gateway = threading.Thread(target=device_b_gateway_controller.run, daemon=True)

    watchdog_obj = Watchdog()
    watchdog = threading.Thread(target=watchdog_obj.reset, daemon=True)

    # arithmetic_operation_obj = ArithmeticOperation()
    # arithmetic_operation = threading.Thread(target=ArithmeticOperation.execute, daemon=True)

    device_a_gateway.start()
    device_b_gateway.start()
    watchdog.start()
    # arithmetic_operation.start()


def main_close():
    if not cache.get('main_start_executed'):
        return

    device_a_gateway_controller.close()
    device_b_gateway_controller.close()
    watchdog_obj.close()
    # arithmetic_operation.close()

    dev_a_storage_handler.close()
    dev_b_storage_handler.close()
    block_c_storage_handler.close()
