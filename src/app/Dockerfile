FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

COPY ../pyproject.toml pyproject.toml

RUN poetry install --only main

COPY ./src/app app

CMD uvicorn app.main:app \
    --host "0.0.0.0" \
    --port 8000 \
    --workers ${APP_WORKERS} \
    --log-level ${APP_LOG_LEVEL}
