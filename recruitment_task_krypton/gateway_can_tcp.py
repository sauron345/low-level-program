import socket
import can


class GatewayCanTcp:

    _DEFAULT_TCP_IP = "0.0.0.0"
    _DEFAULT_TCP_PORT = 5000
    _DEFAULT_BUFFER_SIZE = 1024
    _MAX_ALLOWED_CLIENTS = 4

    def __init__(
        self,
        ip=_DEFAULT_TCP_IP,
        port=_DEFAULT_TCP_PORT,
        buffer_size=_DEFAULT_BUFFER_SIZE
    ):
        self._IP = ip
        self._PORT = port
        self._BUFFER_SIZE = buffer_size
        self._client_socket = None

    def open(self):
        self._CAN_config()
        tcp_server = self._tcp_server_init()
        print(self._server_listening_msg())
        self._client_socket, client_address = tcp_server.accept()
        print(self._client_connected_msg(client_address))

    def _CAN_config(self):
        # can_interface = "can0"
        # bus = can.interface.Bus(channel=can_interface, interface='pcan')
        self._bus = can.interface.Bus(channel='virtual', interface='virtual')

    def _tcp_server_init(self):
        tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server.bind((self._IP, self._PORT))
        tcp_server.listen(self._MAX_ALLOWED_CLIENTS)
        return tcp_server

    def _server_listening_msg(self):
        return f"TCP Server listening on {self._IP}: {self._PORT}"

    def _client_connected_msg(self, client_address):
        return f"Connected with client: {client_address}"

    def close(self):
        self._client_socket.close()
        self._bus.shutdown()
