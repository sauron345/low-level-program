import time
from datetime import datetime
from threading import Lock

from low_level_program.utils.extractor_can_tcp_data import ExtractorCanTcpData


class ArithmeticOperation:

    _DEFAULT_OPERATOR = '+'
    _INTERVAL = 0.1  # 100ms cycle

    def __init__(self, dev_a_client, dev_b_client, operator=_DEFAULT_OPERATOR):
        self._extract_can_data_from(dev_a_client, dev_b_client)
        self._operator = operator
        self._running = True
        self._lock = Lock()

    def _extract_can_data_from(self, dev_a_client, dev_b_client):
        can_data_extractor_for_client_a = ExtractorCanTcpData(dev_a_client.can_frame)
        can_data_extractor_for_client_a.execute()

        can_data_extractor_for_client_b = ExtractorCanTcpData(dev_b_client.can_frame)
        can_data_extractor_for_client_b.execute()

        client_a_extracted_data = can_data_extractor_for_client_a.get_extracted_data()
        client_b_extracted_data = can_data_extractor_for_client_b.get_extracted_data()

        self._param_a = int(client_a_extracted_data['can_data'])
        self._param_b = int(client_b_extracted_data['can_data'])

    @staticmethod
    def allowed_operators():
        return ['+', '-', '*', '/']

    def execute(self):
        from low_level_program.startup import block_c_storage_handler

        while self._running:
            data = self._get_proper_params_result() + self._get_realtime_in_seconds()
            block_c_storage_handler.add_new({"result": data})
            time.sleep(self._INTERVAL)

    def _get_realtime_in_seconds(self):
        now = datetime.now()
        seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        return seconds_since_midnight

    def _get_proper_params_result(self):
        operator = self._get_chosen_operator()
        return self._get_proper_result(operator)

    def _get_chosen_operator(self):
        with self._lock:
            return self._operator

    def _get_proper_result(self, operator):
        match operator:
            case '+':
                return self._addition()
            case '-':
                return self._subtraction()
            case '*':
                return self._multiplication()
            case '/':
                return self._division()

    def _addition(self):
        return self._param_a + self._param_b

    def _subtraction(self):
        return self._param_a - self._param_b

    def _multiplication(self):
        return self._param_a * self._param_b

    def _division(self):
        try:
            return self._param_a / self._param_b
        except ZeroDivisionError:
            return 0

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, char):
        self._operator = char

    def close(self):
        with self._lock:
            self._running = False
