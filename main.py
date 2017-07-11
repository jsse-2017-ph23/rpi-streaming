import os
from time import sleep

from google.cloud import storage
from google.oauth2 import service_account
from picamera import PiCamera

from streaming.main_loop import main_loop


def storage_client_factory():
    json = os.getenv('GOOGLE_SERVICE_KEY')
    if json is None:
        raise RuntimeError('GOOGLE_SERVICE_KEY environment variable is not set. Check README.md, service key section '
                           'for details')
    credentials = service_account.Credentials.from_service_account_info(json)
    return storage.Client(credentials=credentials)

def main():
    client = storage_client_factory()
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    main_loop(camera, client)

if __name__ == '__main__':
    main()
