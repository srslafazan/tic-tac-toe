FROM python:3.11.4

ADD . /app

WORKDIR /app

RUN python -m pip install library/

WORKDIR /app/backends

RUN python -m pip install pyproject.toml
RUN python -m pip install -r requirements.txt
RUN python -m pip install -r requirements.production.txt
RUN python -m pip install .

CMD gunicorn --bind 0.0.0.0:8000 wsgi:app
