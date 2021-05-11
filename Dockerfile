FROM ubuntu:latest as build
RUN apt update
RUN apt upgrade -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install --upgrade wheel
WORKDIR /app
COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["python3", "./main.py"]

