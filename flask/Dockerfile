# Use an official Python runtime as a base image
FROM python:3.7-slim-buster

RUN  apt-get update
RUN pip install --upgrade pip

# Set the timezone to IST (Indian Standard Time)
ENV TZ=Asia/Kolkata

ENV PORT 5000
EXPOSE $PORT

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt ./

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Run the Flask application
#CMD ["flask", "run", "--host=0.0.0.0","--port=$PORT"]
CMD flask run --host=0.0.0.0 --port $PORT
