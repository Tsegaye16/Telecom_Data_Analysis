FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install the dependencies listed in the requirements file
RUN pip install -r requirements.txt

# Copy the application source code into the container
COPY / .

# Specify the command to run the application
CMD ["python", "app.py"]
