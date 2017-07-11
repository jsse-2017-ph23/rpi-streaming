import threading
from io import BytesIO


capture_lock = threading.Lock()


def take_picture(camera):
    # Create an in-memory stream
    stream = BytesIO()
    with capture_lock:
        camera.capture(stream, 'jpeg')
    value = stream.getvalue()
    stream.close()
    return value
