from device_B.device_b_emulator import DeviceBEmulator


def init_device_b_emulators():
    dev_b_emulator_for_block_c = DeviceBEmulator(
        ip='127.0.0.1',  # for example
        can_frame=b'\x85\x12\x34\x56\x78\x12\x34\x56\x78\x00\x00\x00\x00',
        block_c_reserved=True,  # for example
        interval=0.1  # for example
    )
    dev_b_emulator_2 = DeviceBEmulator(
        ip='127.0.0.2',
        can_frame=b'\xDE\xAD\xBE\xEF\xCA\xFE\xBA\xBE\x00\x11\x22\x33\x99',
        interval=0.3
    )

    dev_b_emulator_3 = DeviceBEmulator(
        ip='127.0.0.3',
        can_frame=b'\x01\x23\x45\x67\x89\xAB\xCD\xEF\x00\x11\x22\x33\x44',
        interval=0.5
    )

    dev_b_emulator_4 = DeviceBEmulator(
        ip='127.0.0.4',
        can_frame=b'\xAA\xBB\xCC\xDD\xEE\xFF\x00\x11\x22\x33\x44\x55\x66',
        interval=0.7
    )

    return [dev_b_emulator_for_block_c, dev_b_emulator_2, dev_b_emulator_3, dev_b_emulator_4]
