# Use an official Python runtime as a base image
FROM python:3.7-slim-buster

# Create a non-root user and group with UID and GID in the acceptable range
RUN groupadd -r appgroup && useradd -r -u 10001 -g appgroup appuser

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Change ownership of the application directory to the new user
RUN chown -R appuser:appgroup /app

# Switch to the non-root user
USER appuser  # Ensure this user exists with UID 10001

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]