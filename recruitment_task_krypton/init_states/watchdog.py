import threading

from device_B.watchdog import Watchdog


def init_watchdog():
    watchdog_obj = Watchdog(reset_can_frame=b'...')
    watchdog = threading.Thread(target=watchdog_obj.reset)
    return watchdog_obj, watchdog
