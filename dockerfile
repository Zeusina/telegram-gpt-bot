FROM python:3.10.11-alpine as Builder

RUN pip --no-cache-dir install poetry

COPY pyproject.toml /
COPY poetry.lock /

RUN poetry export --without-hashes --format=requirements.txt > requirements.txt

FROM python:3.10.11-alpine as Runner

COPY --from=Builder /requirements.txt /requirements.txt
RUN pip --no-cache-dir install -r /requirements.txt

COPY  config.yaml /config.yaml
COPY  /src/telegram_gpt_bot/ /src/telegram_gpt_bot/

ENV PYTHONPATH "${PYTHONPATH}:/src/telegram_gpt_bot:/src:/src/openai/:/src/openai/gpt4free"

CMD python ./src/telegram_gpt_bot/