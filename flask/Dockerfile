# Use an official Python runtime as a base image
FROM python:3.7-slim-buster

RUN  apt-get update
RUN pip install --upgrade pip

# Create a non-root user and group
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Set the timezone to IST (Indian Standard Time)
ENV TZ=Asia/Kolkata

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt ./

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Change ownership of the application directory to the new user
RUN chown -R appuser:appgroup /app

# Switch to the non-root user
USER appuser

ENV PORT 5000
EXPOSE $PORT

CMD flask run --host=0.0.0.0 --port $PORT
