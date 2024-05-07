FROM python:3.12

WORKDIR /app

RUN pip install --no-cache-dir poetry==1.8.2

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && \
    poetry install --only main --no-root --no-cache --no-interaction --no-ansi

COPY . .
