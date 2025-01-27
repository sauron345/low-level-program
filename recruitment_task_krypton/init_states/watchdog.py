import threading

from device_B.watchdog import Watchdog


def init_watchdog():
    watchdog_obj = Watchdog(reset_can_frame=b'\x01\x23\x45\x67\x89\xAB\xCD\xEF')
    watchdog = threading.Thread(target=watchdog_obj.reset)
    return watchdog_obj, watchdog
