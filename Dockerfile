FROM python:3.9

ENV PYTHONUNBUFFERED 1 

WORKDIR /app

COPY requirements.txt /app/requirements.txt

# Install psycopg2 dependencies
RUN apt-get update && apt-get install -y \
    postgresql \
    python3-psycopg2 \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD python manage.py runserver 127.0.0.1:8000