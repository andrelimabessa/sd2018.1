FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /web
WORKDIR /web

RUN apt-get update && apt-get upgrade -y
RUN pip install -U pip setuptools
RUN pip install virtualenv
RUN virtualenv myenv
RUN /bin/bash -c "source myenv/bin/activate"
RUN pip install django
RUN django-admin startproject project
WORKDIR /web/project
RUN python manage.py startapp app