FROM python:3.8.12-slim

COPY requirements.txt requirements.txt
COPY dslogic_package dslogic_package
COPY setup.py setup.py

RUN pip install --upgrade pip setuptools wheel


RUN pip install .
RUN pip install -r requirements.txt

#Run container
#Launch app locally
#CMD uvicorn dslogic_package.api_file:app --host 0.0.0.0

#Run container deployed
CMD uvicorn dslogic_package.api_file:app --host 0.0.0.0 --port $PORT
