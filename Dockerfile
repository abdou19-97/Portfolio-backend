FROM python:3.9

ENV PYTHONUNBUFFERED 1 

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD python manage.py runserver 127.0.0.1:8000