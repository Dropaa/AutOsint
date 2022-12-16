FROM python:latest

RUN mkdir /app
WORKDIR /app

# Copier les fichiers nécessaires à votre application dans le répertoire de travail
COPY install.sh /app
COPY requirements.txt /app
COPY VenvProjet/ /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]

