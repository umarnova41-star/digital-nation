# Dockerfile for FastAPI app (backend/app/main.py)
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install build deps for some packages (e.g., psycopg2/asyncpg)
RUN apt-get update && apt-get install -y gcc libpq-dev --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first for better layer caching
COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy app source
COPY . .

# Create non-root user and set ownership
RUN groupadd -r app && useradd -r -g app app \
    && chown -R app:app /app

USER app

EXPOSE 8000

# Run uvicorn; in production consider using --workers >1 and a process manager
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
