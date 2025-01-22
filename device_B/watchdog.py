import time
from threading import Lock

from recruitment_task_krypton.device_b_gateway_controller import dev_b_clients_storage
from recruitment_task_krypton.singleton_meta import SingletonMeta


class Watchdog(metaclass=SingletonMeta):

    _INTERVAL = 0.5  # 500ms
    _DEFAULT_RESET_FRAME = b'\x00\x00\x00\x00'

    def __init__(self):
        self._reset_frame = self._DEFAULT_RESET_FRAME
        self._lock = Lock()
        self._running = True

    def reset(self):
        while self._running:
            time.sleep(self._INTERVAL)
            with self._lock:
                reset_frame = self._reset_frame
            for client in dev_b_clients_storage:
                try:
                    client.sendall(reset_frame)
                except (BrokenPipeError, ConnectionResetError):
                    with self._lock:
                        dev_b_clients_storage.discard(client)

    @property
    def reset_frame(self):
        with self._lock:
            return self._reset_frame

    @reset_frame.setter
    def reset_frame(self, frame):
        with self._lock:
            self._reset_frame = frame

    def close(self):
        with self._lock:
            self._running = False
