from recruitment_task_krypton.device_a_gateway_controller import DeviceAGatewayController
from recruitment_task_krypton.device_clients_storage import DeviceClientsStorage

dev_b_clients_storage = DeviceClientsStorage()


class DeviceBGatewayController(DeviceAGatewayController):

    def __init__(self, device_gateway):
        DeviceAGatewayController.__init__(self, device_gateway)

    def _assign_storage_handler(self):
        from recruitment_task_krypton.startup import dev_b_storage_handler
        self._dev_storage_handler = dev_b_storage_handler

    def send(self, data):
        with self._lock:
            for client in dev_b_clients_storage:
                client.sendall(data)

    def _count_active_clients(self):
        return dev_b_clients_storage.count()

    def _add_new_client(self):
        dev_b_clients_storage.add(self._client_socket)

    def _count_clients(self):
        return dev_b_clients_storage.count()

    def _discard_client(self, client_socket):
        dev_b_clients_storage.discard(client_socket)
