import threading
from datetime import datetime
from time import sleep

from streaming.take_picture import take_picture
from streaming.upload import upload


def main_loop(camera, storage):
    while True:
        threading.Thread(target=tick, name="tick", args=[camera, storage])
        sleep(1)


def tick(camera, storage):
    picture = take_picture(camera)
    time = datetime.utcnow()
    upload(picture, time, storage)
