FROM python:3.6-alpine

WORKDIR /home/app

RUN pip install flask
RUN pip install kafka-python


COPY . .
EXPOSE 5000

CMD python app.py