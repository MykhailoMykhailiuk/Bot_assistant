FROM python:3.11.6-alpine

RUN pip install prompt_toolkit

WORKDIR /app

COPY . .

ENTRYPOINT [ "python", "run.py" ]