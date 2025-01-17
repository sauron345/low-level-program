from recruitment_task_krypton.gateway_can_tcp import GatewayCanTcp

device_a_gateway = None
device_b_gateway = None


def open_gateways():
    global device_a_gateway
    global device_b_gateway

    device_a_gateway = GatewayCanTcp()
    device_b_gateway = GatewayCanTcp()

    device_a_gateway.open()
    device_b_gateway.open()


def close_gateways():
    device_a_gateway.close()
    device_b_gateway.close()
