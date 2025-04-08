FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install -r backend/requirements.txt

EXPOSE 5000