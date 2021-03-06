FROM python:3.7.2-alpine3.7

WORKDIR /app

ADD ./requirements.txt /app

RUN pip install -r requirements.txt
RUN pip install flask-cors

CMD ["python", "app.py"]
