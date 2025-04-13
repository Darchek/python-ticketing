FROM python:3.12-slim

# Install Git and SSH
RUN apt-get update && \
    apt-get install -y git openssh-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN rm -rf /app/* && \
    git clone https://github.com/Darchek/python-ticketing.git .

COPY . /app

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --force-reinstall -r /app/backend/requirements.txt

EXPOSE 5000