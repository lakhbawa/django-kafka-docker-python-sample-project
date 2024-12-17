FROM amazonlinux:latest

RUN yum update -y && \
    yum install -y git python3-pip

WORKDIR /var/www

COPY ./src /var/www/
RUN pip3 install -r requirements.txt
RUN pip3 install Django

EXPOSE 2000

CMD [ "python3", './app.py' ]