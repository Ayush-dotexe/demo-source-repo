# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application source code
COPY app.py /app/app.py

# Install dependencies
RUN pip install pyyaml

# Define the command to run the app
CMD ["python", "/app/app.py"]
