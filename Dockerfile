FROM python:3.12-slim
# sample-testing
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

ENV PORT=8080

CMD exec gunicorn --bind :$PORT app:app
