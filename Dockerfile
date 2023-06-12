FROM python:3.11
RUN pip3 install tavern
WORKDIR /usr/src/app
COPY . .
CMD [ "python", "./main.py", "--host=0.0.0.0" ]