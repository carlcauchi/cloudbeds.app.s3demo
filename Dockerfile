FROM tiangolo/uwsgi-nginx-flask:python3.8

LABEL maintainer="Carl Cauchi <carl@ultradesigns.net>"

COPY src /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir flask boto3

WORKDIR /app

ENV AWS_BUCKET_NAME=none
ENV AWS_KEY_ID=none
ENV AWS_SECRET_ACCESS_KEY=none
ENV AWS_REGION_NAME=none
ENV SERVER_ADDRESS=0.0.0.0
ENV SERVER_PORT=5000
ENV LISTEN_PORT=80
ENV DEBUG_MODE=False

EXPOSE 80/tcp