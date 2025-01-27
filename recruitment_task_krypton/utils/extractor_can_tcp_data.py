class ExtractorCanTcpData:

    _MAX_ALLOWED_BYTES = 13

    def __init__(self, data):
        self._data = data
        self._data_length = None
        self._extracted_data = {}

    def execute(self):
        self._extract_frame_format()
        self._extract_frame_type()
        self._extract_data_length()
        self._extract_can_id()
        self._extract_can_data()

    def _extract_frame_format(self):
        ff = (self._data[0] & 0x80) >> 7
        self._extracted_data['frame_format'] = 'extended frame' if ff == 1 else 'standard frame'

    def _extract_frame_type(self):
        rtr = (self._data[0] & 0x40) >> 6
        self._extracted_data['frame_type'] = 'remote frame' if rtr == 1 else 'data frame'

    def _extract_data_length(self):
        self._data_length = self._data[0] & 0x0F
        self._extracted_data['data_length'] = self._data_length

    def _extract_can_id(self):
        can_id = int.from_bytes(self._data[1:5], byteorder='big')
        self._extracted_data['can_id'] = hex(can_id)[2:].zfill(4)

    def _extract_can_data(self):
        can_data = self._data[5:5 + self._data_length]
        self._extracted_data['can_data'] = can_data.hex()

    def get_extracted_data(self):
        return self._extracted_data
