FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /schemio
WORKDIR /schemio

ADD . /schemio/

RUN pip3 install -r requirements.txt
