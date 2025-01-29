import time
from threading import Lock

from low_level_program.gateways.device_b_gateway_controller import dev_b_clients_storage
from low_level_program.utils.singleton_meta import SingletonMeta


class Watchdog(metaclass=SingletonMeta):

    _INTERVAL = 0.5  # 500ms

    def __init__(self, reset_can_frame):
        self._reset_can_frame = reset_can_frame
        self._lock = Lock()
        self._running = True

    def reset(self):
        while self._running:
            time.sleep(self._INTERVAL)
            with self._lock:
                reset_frame = self._reset_can_frame

            for client in dev_b_clients_storage:
                try:
                    client.sendall(reset_frame)
                except (BrokenPipeError, ConnectionResetError):
                    self._remove_client(client)

    def _remove_client(self, client):
        dev_b_clients_storage.discard(client)

    @property
    def reset_frame(self):
        with self._lock:
            return self._reset_can_frame

    @reset_frame.setter
    def reset_frame(self, frame):
        with self._lock:
            self._reset_can_frame = frame

    def close(self):
        with self._lock:
            self._running = False
