FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /schemio
WORKDIR /schemio

ADD . /schemio/

RUN pip3 install -r requirements.txt && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py collectstatic --noinput

CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]
