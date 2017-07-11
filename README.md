# rpi-streaming
Docker image for streaming webcam photo to cloud storage

__WARNING__: This image is designed to run on _ARM_ architecture. x64 computer will not able to run this image.

## Set up camera for raspberry PI
See this [tutorial](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera)

## Get service account key
Service account is required for uploading image to cloud storage. See [here](https://cloud.google.com/docs/authentication/getting-started#auth-cloud-implicit-python) for instruction to get the key.

Set the _CONTENT_ of the JSON file downloaded to environment variable `$GOOGLE_SERVICE_KEY`.

## Install dependencies
Run the following commands:
```bash
sudo apt-get update # Update package database
sudo apt-get install python3 python3-pip # Install python interpolator
sudo pip3 install setuptools # Install python dependency
sudo pip3 install pipenv # Install pipenv, package management for python
pipenv --three install --dev # Install local dependencies
```

## Execution
__Remember to set google service key first__
```bash
pipenv shell python3 main.py
```
