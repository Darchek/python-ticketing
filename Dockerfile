FROM python:3.12-slim

WORKDIR /app/backend

COPY backend /app/backend
COPY frontend /app/frontend

RUN pip install -r requirements.txt

EXPOSE 5000