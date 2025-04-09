FROM python:3.13-bullseye as base
ENV PYTHONUNBUFFERED=1

RUN apt update
RUN apt install gettext -y

RUN mkdir /code

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

FROM base as development

RUN poetry install --no-root

RUN poetry run playwright install --with-deps

COPY . .

EXPOSE 8000

ENTRYPOINT [ "/code/start-django.sh" ]

FROM base AS production

RUN poetry install --only main

COPY . .

EXPOSE 8000

ENTRYPOINT [ "/code/start-django.sh" ]