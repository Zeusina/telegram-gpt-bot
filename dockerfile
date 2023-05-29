FROM python:3.10.11-alpine

COPY pyproject.toml /
COPY poetry.lock /
RUN pip install poetry &&\
    poetry export -f requirements.txt --output /requirements.txt && ls -la && \
    pip uninstall -y poetry &&\
    pip install -r /requirements.txt &&\
    rm /poetry.lock && rm pyproject.toml

COPY /src/telegram-gpt-bot/ /src/telegram-gpt-bot/
COPY config.yaml /config.yaml

CMD python /src/telegram-gpt-bot