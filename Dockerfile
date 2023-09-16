FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /opt/CurrencyExchanger

COPY ./ ./

RUN pip install --upgrade pip &&  \
    pip install poetry

RUN poetry config installer.max-workers 10 &&  \
    poetry install