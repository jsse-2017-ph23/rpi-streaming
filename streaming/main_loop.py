import threading
from datetime import datetime
from time import sleep

import logging

from streaming.take_picture import take_picture
from streaming.upload import upload

logger = logging.getLogger('MainLoop')


def main_loop(camera, storage):
    while True:
        thread = TickThread(camera, storage)
        thread.start()
        sleep(5)


class TickThread(threading.Thread):
    def __init__(self, camera, storage):
        super(TickThread, self).__init__()
        self.camera = camera
        self.storage = storage

    def run(self):
        logger.debug('Attempting to take picture')
        picture = take_picture(self.camera)
        logger.debug('Picture successfully taken')

        time = datetime.now()  # Seems that using local timezone will work, given all devices are at same tz
        logger.debug('Time now is %s', time)

        logger.debug('Starting to upload')
        upload(picture, time, self.storage)
        logger.debug('Upload completed')
