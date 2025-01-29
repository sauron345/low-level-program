from device_A.device_a_stub import DeviceAStub


def init_device_a_stubs():
    dev_a_emulator_for_block_c = DeviceAStub(
        ip='127.0.0.5',  # for example
        can_frame=b'\x85\x12\x34\x56\x78\x12\x34\x56\x78\x00\x00\x00\x00',
        block_c_reserved=True,  # for example
        interval=0.1  # for example
    )
    dev_a_emulator_2 = DeviceAStub(
        ip='127.0.0.6',
        can_frame=b'\xDE\xAD\xBE\xEF\xCA\xFE\xBA\xBE\x00\x11\x22\x33\x99',
        interval=0.3
    )

    dev_a_emulator_3 = DeviceAStub(
        ip='127.0.0.7',
        can_frame=b'\x01\x23\x45\x67\x89\xAB\xCD\xEF\x00\x11\x22\x33\x44',
        interval=0.5
    )

    dev_a_emulator_4 = DeviceAStub(
        ip='127.0.0.8',
        can_frame=b'\xAA\xBB\xCC\xDD\xEE\xFF\x00\x11\x22\x33\x44\x55\x66',
        interval=0.7
    )

    return [dev_a_emulator_for_block_c, dev_a_emulator_2, dev_a_emulator_3, dev_a_emulator_4]
