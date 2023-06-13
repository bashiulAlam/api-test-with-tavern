FROM python:3.11
RUN pip3 install tavern
WORKDIR /usr/src/app
COPY . .
EXPOSE 8080
CMD [ "python", "./main.py", "host=127.0.0.1", "port=8080" ]