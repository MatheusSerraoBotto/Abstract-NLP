FROM python:3.8-slim

RUN apt-get update
RUN apt-get install gcc g++ curl unzip -y

RUN useradd -ms /bin/bash jk
USER jk

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt