import threading


class DeviceClientsStorage(set):

    def __init__(self):
        super().__init__()
        self._lock = threading.Lock()

    def add(self, client):
        with self._lock:
            super().add(client)

    def discard(self, client):
        with self._lock:
            super().discard(client)

    def count(self):
        return len(self)
