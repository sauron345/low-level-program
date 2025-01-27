from device_B.device_b_emulator import DeviceBEmulator


def init_device_b_emulators():
    dev_b_emulator_for_block_c = DeviceBEmulator(
        ip='127.0.0.1',  # for example
        can_frame=b'...',
        block_c_reserved=True,  # for example
        interval=0.1  # for example
    )
    dev_b_emulator_2 = DeviceBEmulator(
        ip='127.0.0.2',
        can_frame=b'...',
        interval=0.3
    )

    dev_b_emulator_3 = DeviceBEmulator(
        ip='127.0.0.3',
        can_frame=b'...',
        interval=0.5
    )

    dev_b_emulator_4 = DeviceBEmulator(
        ip='127.0.0.4',
        can_frame=b'...',
        interval=0.7
    )

    return [dev_b_emulator_for_block_c, dev_b_emulator_2, dev_b_emulator_3, dev_b_emulator_4]
