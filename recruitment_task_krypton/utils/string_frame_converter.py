class StringFrameConverter:

    def __init__(self, frames_str):
        self._frame_str = frames_str
        self._is_valid = True
        self._bytes_in_str_list = []

    def get_in_bytes(self):
        self._check_length()
        self._execute_validation()
        return self._get_proper_result()

    def _check_length(self):
        if self._is_length_proper():
            self._is_valid = False

    def _is_length_proper(self):
        return len(self._frame_str.split(' ')) != 13

    def _execute_validation(self):
        for byte in self._frame_str.split(' '):
            self._add_to_list_if_valid(byte)

    def _add_to_list_if_valid(self, byte):
        if byte.isdigit() and len(byte) == 2:
            self._bytes_in_str_list.append(f"0x{byte}")
        else:
            self._is_valid = False

    def _get_proper_result(self):
        if self._is_valid:
            return self._get_converted_list_to_bytes()
        return None

    def _get_converted_list_to_bytes(self):
        return bytes([int(hex_value, 16) for hex_value in self._bytes_in_str_list])
