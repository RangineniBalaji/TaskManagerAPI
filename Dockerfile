FROM python:3.10-slim

ENV PYTHONBUFFERED True

ENV APP_HOME /APP_HOME
WORKDIR $APP_HOME
COPY . ./

RUN pip install Flask gunicorn 

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
