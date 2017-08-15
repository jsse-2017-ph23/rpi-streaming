import uuid

from math import floor

BUCKET_NAME = 'turbo-chainsaw'
DIRECTORY = 'webcam-images/'


def upload(picture, time, storage):
    bucket = storage.get_bucket(BUCKET_NAME)
    uuid_txt = uuid.uuid4().hex
    blob = bucket.blob(DIRECTORY + uuid_txt + '.jpeg')
    blob.metadata = {
        'creationTime': floor(time.timestamp() * 1000)
    }
    blob.upload_from_string(picture, content_type='image/jpeg')
