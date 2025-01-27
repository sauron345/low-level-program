import os
import shutil

from recruitment_task_krypton.utils.storage_handler import StorageHandler
from django.conf import settings


def init_storage_handlers(dev_a_clients, dev_b_clients):
    dev_a_storage_handlers_list = []
    dev_b_storage_handlers_list = []

    dev_a_storages_dir = settings.BASE_DIR / 'logs_storages/device_a'
    dev_b_storages_dir = settings.BASE_DIR / 'logs_storages/device_b'

    if os.path.exists(dev_a_storages_dir):
        shutil.rmtree(dev_a_storages_dir)
        os.makedirs(dev_a_storages_dir)

    if os.path.exists(dev_b_storages_dir):
        shutil.rmtree(dev_b_storages_dir)
        os.makedirs(dev_b_storages_dir)

    for index, dev_client in enumerate(dev_a_clients):
        dev_a_storage_handlers_list.append(StorageHandler(dev_a_storages_dir / f'stub_{index+1}.json'))

    for index, dev_client in enumerate(dev_b_clients):
        dev_b_storage_handlers_list.append(StorageHandler(dev_b_storages_dir / f'emulator_{index+1}.json'))

    block_c_storage_handler = StorageHandler(settings.BASE_DIR / 'logs_storages/block_c.json')

    return dev_a_storage_handlers_list, dev_b_storage_handlers_list, block_c_storage_handler
