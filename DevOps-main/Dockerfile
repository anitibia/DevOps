# Dockerfile for projeckt
FROM python:3.12

WORKDIR /app

COPY . /app/

RUN pip install -r requirments.txt

CMD flask run --host=0.0.0.0 --port=80
