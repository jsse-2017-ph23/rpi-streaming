import threading
from datetime import datetime
from time import sleep

import logging

from streaming.take_picture import take_picture
from streaming.upload import upload

logger = logging.getLogger('MainLoop')


def main_loop(camera, storage):
    while True:
        threading.Thread(target=tick, name="tick", args=[camera, storage])
        sleep(2)


def tick(camera, storage):
    logger.debug('Attempting to take picture')
    picture = take_picture(camera)
    logger.debug('Picture successfully taken')

    time = datetime.utcnow()
    logger.debug('Time now is %s', time)

    logger.debug('Starting to upload')
    upload(picture, time, storage)
    logger.debug('Upload completed')
