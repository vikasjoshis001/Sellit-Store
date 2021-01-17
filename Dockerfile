FROM ubuntu
MAINTAINER vikasjoshis001@gmail.com

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install python3 && apt-get -y install python3-pip && apt-get -y install gunicorn
RUN pip3 install Django==3.0.4
RUN pip3 install djangorestframework
RUN pip3 install djangorestframework-jwt
RUN pip3 install django-crispy-forms
RUN pip3 install pillow
RUN mkdir Sellit
RUN cd Sellit
WORKDIR /Sellit
ADD . /Sellit
ENV PORT=8000
EXPOSE 8000
