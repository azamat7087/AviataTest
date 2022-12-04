FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /airflow
RUN apt-get update && apt-get -y install cron
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

