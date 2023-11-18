FROM python:3.10
LABEL authors="shreydabhi"

WORKDIR /opt/app

#install dependencies
COPY requirements.txt .

RUN pip install -r /opt/app/requirements.txt

# copy django files
COPY api /opt/app/api

COPY ghibliapi /opt/app/ghibliapi

COPY manage.py /opt/app

# copy static files
COPY templates /opt/static

ENTRYPOINT ["gunicorn", "ghibliapi.wsgi", "--workers", "5", "--bind", "0.0.0.0:8000", "--timeout", "60"]