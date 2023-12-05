FROM python:3.9

ENV PYTHONUNBUFFERED 1 

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

RUN python manage.py collectstatic --noinput --verbosity 3

EXPOSE 8000
CMD python manage.py collectstatic --noinput --verbosity 3 && python manage.py runserver 0.0.0.0:8000
# CMD python manage.py runserver 0.0.0.0:8000