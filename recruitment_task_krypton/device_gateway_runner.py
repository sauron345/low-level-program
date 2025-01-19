import socket

import can


class DeviceGatewayRunner:

    _DEFAULT_TCP_IP = "0.0.0.0"
    _DEFAULT_TCP_PORT = 5000
    _MAX_ALLOWED_CLIENTS = 4

    def __init__(
            self,
            device_type,
            ip=_DEFAULT_TCP_IP,
            port=_DEFAULT_TCP_PORT
    ):
        self._IP = ip
        self._PORT = port
        self._client_socket = None
        self._client_address = None
        self._device_type = device_type

    def accept_client(self):
        self._client_socket, self._client_address = self.server_socket.accept()
        print(self._client_connected_msg())

    @property
    def client_socket(self):
        return self._client_socket

    @property
    def client_address(self):
        return self._client_address

    @property
    def max_allowed_clients(self):
        return self._MAX_ALLOWED_CLIENTS

    @property
    def device_type(self):
        return self._device_type

    def open(self):
        self._CAN_config()
        self._tcp_server_init()
        print(self._server_listening_msg())

    def _CAN_config(self):
        # can_interface = "can0"
        # bus = can.interface.Bus(channel=can_interface, interface='pcan')
        self._bus = can.interface.Bus(channel='virtual', interface='virtual')

    def _tcp_server_init(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self._IP, self._PORT))
        self.server_socket.listen(self.max_allowed_clients)

    def _server_listening_msg(self):
        return f"TCP Server listening on {self._IP}: {self._PORT}"

    def _client_connected_msg(self):
        return f"Connected with client: {self.client_address}"

    def close(self):
        self._client_socket.close()
        self._bus.shutdown()
