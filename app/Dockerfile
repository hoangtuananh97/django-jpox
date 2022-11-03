FROM python:3.9-slim
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get install -y build-essential python3-dev libpq-dev \
    && apt-get clean \

RUN apt-get update \
  && apt-get install -y \
  libcairo2 \
  libgdk-pixbuf2.0-0 \
  liblcms2-2 \
  libopenjp2-7 \
  libpango-1.0-0 \
  libpangocairo-1.0-0 \
  libssl1.1 \
  libtiff5 \
  libwebp6 \
  libxml2 \
  libpq5 \
  libcurl4-openssl-dev \
  shared-mime-info \
  curl \
  mime-support \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python3 manage.py runserver 0.0.0.0:8001