import socket
import time
from threading import Lock


class DeviceAStub:

    _DEFAULT_PORT = 5000
    _DEFAULT_INTERVAL = 0.1

    def __init__(self,
        ip,
        port=_DEFAULT_PORT,
        can_frame=b'\x01\x23\x45\x67\x89\xAB\xCD\xEF',
        interval=_DEFAULT_INTERVAL,
        block_c_reserved=False
    ):
        self._IP = ip
        self._PORT = port
        self._can_frame = can_frame
        self._INTERVAL = interval
        self._block_c_reserved = block_c_reserved
        self._running = True
        self._lock = Lock()
        self._tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        try:
            self._tcp_client.connect((self._IP, self._PORT))

            while self._running:
                self._tcp_client.sendall(self._can_frame)

                time.sleep(self._INTERVAL)
        except ConnectionRefusedError:
            print(f"Cannot connect with device A server on port: {self._PORT}")

    def is_reserved_for_block_c(self):
        return self._block_c_reserved

    @property
    def can_frame(self):
        return self._can_frame

    @property
    def ip(self):
        return self._IP

    def close(self):
        with self._lock:
            self._running = False
