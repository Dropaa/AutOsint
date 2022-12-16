FROM python:latest
COPY VenvProjet/main.py /app
WORKDIR /app
ENTRYPOINT ["python3", "main.py"]