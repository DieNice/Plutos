FROM python:3.8
RUN mkdir /www/ && mkdir /www/Plutos
WORKDIR /www/Plutos
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 8001