FROM python:3.12

COPY . /projectdir

WORKDIR /projectdir

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

