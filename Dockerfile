FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /prototype
ADD ./prototype/requirements.txt .
RUN pip install -r requirements.txt
ADD ./prototype .
