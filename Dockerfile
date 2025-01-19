# Use Python 3.10 slim image as base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

# Create directories for temp files, output and model cache
RUN mkdir -p temp output model-cache

# Copy project files
COPY . .

# Download and cache model weights during build
RUN python script/download-weights

# Expose port
EXPOSE 80

# Run the application
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]