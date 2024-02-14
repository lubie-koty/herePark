FROM python:3.11

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock* ./

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry install

COPY . .
