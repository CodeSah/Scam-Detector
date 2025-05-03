# Dockerfile
FROM python:3.10

WORKDIR /app

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ ./backend/
WORKDIR /app/backend

# Copy frontend to serve via static hosting or proxy later
COPY frontend/ /app/frontend/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
