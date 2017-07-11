# rpi-streaming
Docker image for streaming webcam photo to cloud storage

__WARNING__: This image is designed to run on _ARM_ architecture. x64 computer will not able to run this image.

## Get service account key
Service account is required for uploading image to cloud storage. See [here](https://cloud.google.com/docs/authentication/getting-started#auth-cloud-implicit-python) for instruction to get the key.

Set the _CONTENT_ of the JSON file downloaded to environment variable `$GOOGLE_SERVICE_ACCOUNT_KEY`.

## Installation
Only docker is required for running the image. After installing docker, run
```bash
docker build -t jsse2017ph23/rpi-streaming .
```

## Execution
```bash
docker run --device=/dev/video0 --restart=always --env GOOGLE_SERVICE_KEY=YOUR_GOOGLE_SERVICE_KEY_JSON -d jsse2017ph23/rpi-streaming
```

Replace `YOUR_GOOGLE_SERVICE_KEY_JSON` to JSON content of the key.
