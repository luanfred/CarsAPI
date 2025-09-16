FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz && \
    tar xzf dockerize-linux-amd64-v0.6.1.tar.gz && \
    mv dockerize /usr/local/bin/

COPY . .

CMD ["dockerize", "-wait", "tcp://db:5432", "-timeout", "120s", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]