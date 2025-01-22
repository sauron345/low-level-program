import time
from datetime import datetime
from threading import Lock


class ArithmeticOperation:

    _DEFAULT_OPERATOR = '+'
    _INTERVAL = 0.1  # 100ms cycle

    def __init__(self, param_a, param_b):
        self._param_a = param_a
        self._param_b = param_b
        self._operator = self._DEFAULT_OPERATOR
        self._lock = Lock()

    def execute(self):
        from recruitment_task_krypton.startup import block_c_storage_handler

        while True:
            data = self._get_proper_params_result() + datetime.now().second
            block_c_storage_handler.add_new(data)
            time.sleep(self._INTERVAL)

    def _get_proper_params_result(self):
        operator = self._get_chosen_operator()
        return self._get_proper_result(operator)

    def _get_chosen_operator(self):
        with self._lock:
            return self._operator

    def _get_proper_result(self, operator):
        match operator:
            case '+':
                return self._param_a + self._param_b
            case '-':
                return self._param_a - self._param_b
            case '*':
                return self._param_a * self._param_b
            case '/':
                return self._param_a / self._param_b
            case '**':
                return self._param_a ** self._param_b

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, char):
        self._operator = char
