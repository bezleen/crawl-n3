FROM python:3.8-slim-bullseye

RUN apt-get update \
    && apt-get install -y gcc vim supervisor \
    && rm -rf /tmp/* /var/cache/*
RUN apt-get install -y ffmpeg
COPY requirements.txt /
RUN pip --no-cache-dir install --upgrade pip setuptools
RUN pip --no-cache-dir install -r requirements.txt && mkdir -p /var/log/apps

COPY . /webapp
WORKDIR /webapp