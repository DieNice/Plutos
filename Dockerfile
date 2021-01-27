FROM python:3.8
RUN mkdir /www/ && mkdir /www/Plutos
WORKDIR /www/Plutos
EXPOSE 8001