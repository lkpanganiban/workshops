FROM python:3.11.6-slim

RUN apt update -y && apt -y install curl

RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src
RUN pip install -r requirements.txt
ADD . /src/

CMD @exec