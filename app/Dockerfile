FROM python:3.9.6-slim
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get install -y build-essential python3-dev postgresql-client libpq-dev \
    && apt-get clean
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary --no-binary psycopg2-binary
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
COPY . .