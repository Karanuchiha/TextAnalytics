FROM ubuntu:18.04

RUN apt-get update

RUN apt-get install python3.8 -y
RUN apt-get install python2.7 -y
RUN apt-get install python3-pip -y
RUN apt-get install openjdk-8-jdk -y

RUN python3.8 -m pip install flask
RUN python3.8 -m pip install Flask-Cors

RUN apt-get install wget -y
RUN wget "www.personal.psu.edu/xxl13/downloads/L2SCA-2016-06-30.tgz"
RUN tar -xzvf L2SCA-2016-06-30.tgz

RUN touch /L2SCA-2016-06-30/input_file.txt
RUN touch /L2SCA-2016-06-30/output_file.txt

ADD flask_backend.py /L2SCA-2016-06-30/flask_backend.py

EXPOSE 1234

WORKDIR /L2SCA-2016-06-30
CMD ["python3.8", "flask_backend.py"]