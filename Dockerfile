FROM python:3.8.12-slim

COPY requirements.txt requirements.txt
COPY dslogic_package dslogic_package

RUN pip install -r requirements.txt



CMD uvicorn dslogic_package.api_file:app --host 0.0.0.0 --port $PORT
