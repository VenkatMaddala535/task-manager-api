# Base Image
FROM python:3.12-slim

# Prevent Python from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Print logs immediately
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Install dependencies first (better Docker layer caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

# Flask application port
EXPOSE 5002

# Start the application
#CMD ["python", "run.py"]
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "run:app"]