from device_A.device_a_stub import DeviceAStub


def init_device_a_stubs():
    dev_a_emulator_for_block_c = DeviceAStub(
        ip='127.0.0.5',  # for example
        can_frame=b'...',
        block_c_reserved=True,  # for example
        interval=0.1  # for example
    )

    dev_a_emulator_2 = DeviceAStub(
        ip='127.0.0.6',
        can_frame=b'...',
        interval=0.3
    )

    dev_a_emulator_3 = DeviceAStub(
        ip='127.0.0.7',
        can_frame=b'...',
        interval=0.5
    )

    dev_a_emulator_4 = DeviceAStub(
        ip='127.0.0.8',
        can_frame=b'...',
        interval=0.7
    )

    return [dev_a_emulator_for_block_c, dev_a_emulator_2, dev_a_emulator_3, dev_a_emulator_4]
