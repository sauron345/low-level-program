from low_level_program.gateways.device_a_gateway_controller import DeviceAGatewayController
from low_level_program.utils.device_clients_storage import DeviceClientsStorage

dev_b_clients_storage = DeviceClientsStorage()


class DeviceBGatewayController(DeviceAGatewayController):

    def __init__(self, device_gateway):
        DeviceAGatewayController.__init__(self, device_gateway)

    def send(self, data):
        for client in dev_b_clients_storage:
            client.sendall(data)

    def _count_active_clients(self):
        return dev_b_clients_storage.count()

    def _add_new_client(self):
        dev_b_clients_storage.add(self._client_socket)

    def _store_client_storage_handler(self):
        from low_level_program.startup import dev_b_storages_handlers

        index = len(self._clients_sockets_storage)
        client_ip, _ = self._client_socket.getsockname()
        self._clients_sockets_storage[client_ip] = dev_b_storages_handlers[index]

    def _count_clients(self):
        return dev_b_clients_storage.count()

    def _discard_client(self, client_socket):
        dev_b_clients_storage.discard(client_socket)
