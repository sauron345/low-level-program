import threading

from recruitment_task_krypton.device_clients_storage import DeviceClientsStorage
from recruitment_task_krypton.extractor_can_tcp_data import ExtractorCanTcpData
from recruitment_task_krypton.singleton_meta import SingletonMeta

dev_a_clients_storage = DeviceClientsStorage()


class DeviceAGatewayController(threading.Thread, metaclass=SingletonMeta):

    def __init__(self, device_gateway):
        super().__init__()
        self._init_state(device_gateway)

    def _init_state(self, device_gateway):
        self._assign_storage_handler()
        self._device_gateway = device_gateway
        self._device_gateway.open()
        self._running = True
        self._lock = threading.Lock()

    def _assign_storage_handler(self):
        from recruitment_task_krypton.startup import dev_a_storage_handler
        self._dev_storage_handler = dev_a_storage_handler

    def run(self):
        try:
            self._check_if_new_client_occurred()
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            self._device_gateway.close()
            print("Server is closed")

    def _check_if_new_client_occurred(self):
        while self._running:
            if self._count_active_clients() < self._max_allowed_clients:
                self._accept_and_communicate_with_client()

    def _count_active_clients(self):
        return dev_a_clients_storage.count()

    def _accept_and_communicate_with_client(self):
        self._device_gateway.accept_client()

        self._add_new_client()

        client_thread = threading.Thread(
            target=self._handle_client,
            args=(self._client_socket,),
            daemon=True
        )
        client_thread.start()

    def _add_new_client(self):
        dev_a_clients_storage.add(self._client_socket)

    def _handle_client(self, client_socket):
        try:
            while self._running:
                data = client_socket.recv(1024)  # Odbieranie danych od klienta
                if not data or self._count_clients() < 1:
                    break
                print(f"Received data: {data.hex()}")
                extracted_data = self._get_in_readable_way(data)
                self._dev_storage_handler.add_new(extracted_data)
        except ConnectionError:
            print(f"Connection with client{self._client_address} is interrupted")
        finally:
            self._discard_client(client_socket)
            client_socket.close()
            print(f"Connection with client{self._client_address} is finished.")

    def _count_clients(self):
        return dev_a_clients_storage.count()

    def _discard_client(self, client_socket):
        dev_a_clients_storage.discard(client_socket)

    def _get_in_readable_way(self, data):
        extractor_can_tcp_data = ExtractorCanTcpData(data)
        extractor_can_tcp_data.execute()
        return extractor_can_tcp_data.get_extracted_data()

    @property
    def _client_socket(self):
        return self._device_gateway.client_socket

    @property
    def _client_address(self):
        return self._device_gateway.client_address

    @property
    def _max_allowed_clients(self):
        return self._device_gateway.max_allowed_clients

    def close(self):
        with self._lock:
            self._running = False
