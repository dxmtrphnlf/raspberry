FROM python:3.6
RUN apt-get update -y
RUN apt-get -y install binutils libproj-dev gdal-bin gettext

RUN mkdir -p /raspberry

RUN pip install --upgrade pip

ADD app/requirements.txt /raspberry
RUN pip install --no-cache-dir -r /raspberry/requirements.txt

WORKDIR /raspberry

COPY app .
