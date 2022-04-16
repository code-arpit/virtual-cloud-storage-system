FROM python:3.8-slim-buster

ARG build_env=dev

ENV CURRENT_ENVIRONMENT $build_env

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /code 

WORKDIR /code

#Installing project level python dependencies
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock /code/
RUN poetry install $(test "${CURRENT_ENVIRONMENT}") --no-interaction --no-ansi

COPY ./src /code/
