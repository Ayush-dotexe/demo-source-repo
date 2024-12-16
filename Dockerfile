# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY app.py /app/

# Placeholder for config.yaml to be copied at runtime
COPY config.yaml /app/

# Install dependencies
RUN pip install pyyaml

# Command to run the app
CMD ["python", "app.py"]
