# Server image
FROM python:3.13-slim AS server

WORKDIR /app

COPY dictionary-server/src/server.py .

EXPOSE 5000

CMD ["python", "server.py"]


# Client image
FROM python:3.13-slim AS client

WORKDIR /app

COPY client/src/client.py .

CMD ["python", "client.py"]