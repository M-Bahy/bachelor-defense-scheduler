FROM python:3.8-alpine
ENV PYTHONUNBUFFER 1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN apk update && \
    apk add build-base && \
    apk add build-base linux-headers && \
    apk add lapack-dev blas-dev && \
    apk add postgresql-dev gcc python3-dev musl-dev && \
    apk add ethtool && \
    pip install psutil && \
    /usr/local/bin/python -m pip install --upgrade pip && pip3 install -r requirements.txt
COPY . .
