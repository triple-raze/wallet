FROM python:3.11-slim

WORKDIR /app/src

COPY requirements.txt ..
COPY pyproject.toml ..

RUN pip install -r ../requirements.txt && pip install -e ..

COPY . ..

