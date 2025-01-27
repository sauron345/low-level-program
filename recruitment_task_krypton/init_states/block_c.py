import threading

from block_C.arithmetic_operation import ArithmeticOperation


def init_block_c(device_a_stubs, device_b_emulators):
    chosen_dev_a_client = None
    chosen_dev_b_client = None

    for dev_a_client in device_a_stubs:
        if dev_a_client.is_reserved_for_block_c():
            chosen_dev_a_client = dev_a_client

    for dev_b_client in device_b_emulators:
        if dev_b_client.is_reserved_for_block_c():
            chosen_dev_b_client = dev_b_client

    arithmetic_operation_obj = ArithmeticOperation(chosen_dev_a_client, chosen_dev_b_client)
    arithmetic_operation = threading.Thread(target=arithmetic_operation_obj.execute)
    return arithmetic_operation_obj, arithmetic_operation
