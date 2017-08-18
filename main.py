import os
from time import sleep

import json

import logging
from google.cloud import storage
from google.oauth2 import service_account
from picamera import PiCamera

from streaming.main_loop import main_loop

# Set up logging
logging.basicConfig(
    format='[%(asctime)s] [%(name)s / %(threadName)s / %(levelname)s] %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG
)
logger = logging.getLogger('Root')


def storage_client_factory():
    key = os.getenv('GOOGLE_SERVICE_KEY')
    if key is None:
        raise RuntimeError('GOOGLE_SERVICE_KEY environment variable is not set. Check README.md, service key section '
                           'for details')
    parse = json.loads(key)
    logger.debug('Got google service key. It is valid JSON.')
    credentials = service_account.Credentials.from_service_account_info(parse)
    return storage.Client('jsse-2017', credentials=credentials)


def main():
    logger.info('Initializing')

    client = storage_client_factory()
    logger.debug('Google cloud storage initialized')

    camera = PiCamera()
    camera.start_preview(alpha=128)
    logger.info('Warming up camera')
    sleep(2)

    logger.info('Initialization completed')
    main_loop(camera, client)


if __name__ == '__main__':
    main()
