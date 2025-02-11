# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . .

# Install necessary packages
RUN pip install -r requirements.txt

# Expose the port your app will run on
EXPOSE 8000

# Command to run your Python application
CMD ["python", "main.py"]
