FROM python:3.12-slim

WORKDIR /app/backend

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000