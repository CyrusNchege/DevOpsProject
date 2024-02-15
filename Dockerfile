FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

ADD . /app/

RUN python manage.py makemigrations myapp
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000