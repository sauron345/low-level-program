import threading

from django.core.cache import cache

from low_level_program.init_states.globals import *
from low_level_program.init_states.gateways import init_gateways
from low_level_program.init_states.storage_handlers import init_storage_handlers
from low_level_program.init_states.watchdog import init_watchdog
from low_level_program.init_states.block_c import init_block_c
from low_level_program.init_states.device_a_stubs import init_device_a_stubs
from low_level_program.init_states.device_b_emulators import init_device_b_emulators


def main_start():
    if not cache.get('main_start_executed'):
        cache.set('main_start_executed', True, None)
    elif cache.get('main_start_executed'):
       return

    global device_a_gateway, device_b_gateway
    global device_a_gateway_controller, device_b_gateway_controller, device_gateway_a_runner, device_gateway_b_runner
    global dev_a_storages_handlers, dev_b_storages_handlers, block_c_storage_handler
    global dev_a_clients_storage, dev_b_clients_storage
    global watchdog, watchdog_obj
    global device_b_clients, device_a_clients
    global arithmetic_operation_obj, arithmetic_operation

    device_b_clients = init_device_b_emulators()
    device_a_clients = init_device_a_stubs()
    device_gateway_a_runner, device_gateway_b_runner, device_a_gateway_controller, device_b_gateway_controller, device_a_gateway, device_b_gateway = init_gateways()
    dev_a_storages_handlers, dev_b_storages_handlers, block_c_storage_handler = init_storage_handlers(device_a_clients, device_b_clients)
    watchdog_obj, watchdog = init_watchdog()
    arithmetic_operation_obj, arithmetic_operation = init_block_c(device_a_clients, device_b_clients)

    device_a_gateway.start()
    device_b_gateway.start()

    for client in device_b_clients:
        threading.Thread(target=client.run).start()

    for client in device_a_clients:
        threading.Thread(target=client.run).start()

    watchdog.start()
    arithmetic_operation.start()


def main_close():
    if not cache.get('main_start_executed'):
        return

    device_a_gateway_controller.close()
    device_b_gateway_controller.close()

    arithmetic_operation_obj.close()
    watchdog_obj.close()

    for client in device_b_clients:
        client.close()

    for client in device_a_clients:
        client.close()

    block_c_storage_handler.close()

    for storage_handler in dev_a_storages_handlers:
        storage_handler.close()

    for storage_handler in dev_b_storages_handlers:
        storage_handler.close()
