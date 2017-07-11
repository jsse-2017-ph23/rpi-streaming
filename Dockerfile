FROM resin/rpi-raspbian:stretch
MAINTAINER Holi0317 "holliswuhollis@gmail.com"

# Copy necessary files
COPY . /srv/

# Build
WORKDIR /srv/
RUN apt-get update \
  && apt-get install python3 python3-pip \
  && pip3 install setuptools \
  && pip3 install pipenv \
  && pipenv --three install --dev

ENTRYPOINT ["pipenv", "shell", "python3", "main.py"]
