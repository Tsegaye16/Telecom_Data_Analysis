FROM python:3.10-slim

# Install system dependencies for ta-lib and other build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    libatlas-base-dev \
    && apt-get clean

WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY / .

CMD ["python", "app.py"]
