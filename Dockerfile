FROM python:latest
COPY VenvProjet/main.py /
CMD ["python3", "/main.py"]