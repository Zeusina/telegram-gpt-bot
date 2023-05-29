FROM python:3.10.11-alpine as Builder

COPY pyproject.toml /
COPY poetry.lock /
RUN pip --no-cache-dir install poetry &&\
    poetry export -f requirements.txt --output /requirements.txt

FROM python:3.10.11-alpine as Runner

COPY --from=Builder /requirements.txt /requirements.txt
RUN pip --no-cache-dir install -r /requirements.txt

COPY  config.yaml /config.yaml
COPY  /src/telegram-gpt-bot/ /src/telegram-gpt-bot/

CMD python /src/telegram-gpt-bot