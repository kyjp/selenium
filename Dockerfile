FROM python:latest

ENV PYTHONIOENCODING utf-8
ENV TZ="Asia/Tokyo"
ENV LANG=C.UTF-8
ENV LANGUAGE=en_US:en_US

RUN apt-get update && \
apt-get install -y \
build-essential \
  cmake \
  git \
  sudo \
  wget \
  vim
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
WORKDIR /app
CMD ["/bin/bash"]
