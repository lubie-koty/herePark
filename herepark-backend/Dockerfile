FROM python:3.11

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock* ./

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config settings.virtualenvs.create false && \
    poetry export -f requirements.txt --output requirements.txt --without-hashes && \
    pip install -r requirements.txt

COPY . .
