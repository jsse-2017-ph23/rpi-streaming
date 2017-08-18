import threading
from datetime import datetime
from io import BytesIO


capture_lock = threading.Lock()


def take_picture(camera):
    # Create an in-memory stream
    stream = BytesIO()
    camera.rotation = 180
    camera.annotate_text = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with capture_lock:
        camera.capture(stream, 'jpeg', resize=(720, 480))
    value = stream.getvalue()
    stream.close()
    return value
