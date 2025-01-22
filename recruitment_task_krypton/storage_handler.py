import json
import os

import ijson


class StorageHandler:

    def __init__(self, path):
        self._PATH = path
        if not os.path.isfile(path):
            self._file_obj = open(self._PATH, 'wb+')
            self._init_state()
        else:
            self._file_obj = open(self._PATH, 'rb+')
            self._file_obj.seek(-1, os.SEEK_END)
            self._file_obj.truncate()
            self._write_to_file("]")

    def _init_state(self):
        self._file_obj.seek(0)
        self._open_storage()
        self._close_storage()
        self._file_obj.flush()

    def _open_storage(self):
        self._write_to_file("[")

    def get_data(self):
        items_found = []
        self._file_obj.seek(0)
        for item in ijson.items(self._file_obj, 'item'):
            items_found.append(item)
        return items_found

    def add_new(self, data):
        self._file_obj.seek(-1, 1)
        self._file_obj.truncate()
        json_data = self._add_proper_data(data)
        self._write_to_file(json_data)
        self._close_storage()
        self._file_obj.flush()

    def _add_proper_data(self, data):
        if self._file_obj.tell() > 5:
            json_data = '   ,'
        else:
            json_data = '\t'
        json_data += f'{json.dumps(data)}'
        return json_data

    def _close_storage(self):
        self._write_to_file("\n]")

    def _write_to_file(self, data):
        self._file_obj.write(data.encode('utf8'))

    def close(self):
        self._file_obj.close()
