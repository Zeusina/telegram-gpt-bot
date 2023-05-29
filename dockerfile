FROM python:3.10.11-alpine

RUN pip install poetry

COPY poetry.lock /
COPY pyproject.toml /
COPY README.md /README.md

COPY /src/telegram-gpt-bot/ /src/telegram-gpt-bot/
COPY config.yaml /config.yaml

RUN poetry install

CMD poetry run python /src/telegram-gpt-bot