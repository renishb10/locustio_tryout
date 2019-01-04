FROM ubuntu
LABEL maintainer="renish.bhaskaran@globalenglish.com"

WORKDIR /usr/src/reachperftest

#install basic needs for python & locust.io
RUN apt-get update
RUN apt-get install nodejs
RUN npm -g install phantomjs
RUN apt-get -y install python3
RUN apt-get -y install python-pip
RUN pip install locustio
RUN pip install numpy
RUN pip install bokeh
RUN pip install pillow
RUN pip install selenium


#Copy all the python files
COPY . .

#Running on below port
EXPOSE 8090

#Executable command
CMD [ "locust" ]