# syntax=docker/dockerfile:1

# base image
FROM python:3.11-slim

# çalışma dizini
WORKDIR /app

# bağımlılıkları kopyala
COPY requirements.txt .

# bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# kodları kopyala
COPY api/ ./api
COPY model/ ./model

# FastAPI başlat
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
