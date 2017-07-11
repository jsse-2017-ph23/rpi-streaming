# rpi-streaming
Docker image for streaming webcam photo to cloud storage

__WARNING__: This image is designed to run on _ARM_ architecture. x64 computer will not able to run this image.

## Installation
Only docker is required for running the image. After installing docker, run
```bash
docker build -t jsse2017ph23/rpi-streaming .
```

## Execution
```bash
docker run -d jsse2017ph23/rpi-streaming
```
