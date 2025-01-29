import threading

from low_level_program.gateways.device_a_gateway_controller import DeviceAGatewayController
from low_level_program.gateways.device_b_gateway_controller import DeviceBGatewayController
from low_level_program.gateways.device_gateway_runner import DeviceGatewayRunner


def init_gateways():
    device_gateway_a_runner = DeviceGatewayRunner()
    device_gateway_b_runner = DeviceGatewayRunner(port=4000)

    device_a_gateway_controller = DeviceAGatewayController(device_gateway_a_runner)
    device_b_gateway_controller = DeviceBGatewayController(device_gateway_b_runner)

    device_a_gateway = threading.Thread(target=device_a_gateway_controller.run)
    device_b_gateway = threading.Thread(target=device_b_gateway_controller.run)

    return device_gateway_a_runner, device_gateway_b_runner, \
       device_a_gateway_controller, device_b_gateway_controller, \
       device_a_gateway, device_b_gateway
