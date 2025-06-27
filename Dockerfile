# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy required files
COPY ./app ./app
COPY ./data ./data
COPY config.json .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
