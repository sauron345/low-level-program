import threading

from device_B.watchdog import Watchdog


def init_watchdog():
    watchdog_obj = Watchdog(reset_can_frame=b'\x85\x12\x34\x56\x78\x12\x34\x56\x78\x00\x00\x00\x00')
    watchdog = threading.Thread(target=watchdog_obj.reset)
    return watchdog_obj, watchdog
