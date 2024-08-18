# Use an official Python runtime as a base image
FROM tbagavathiraja/private-repo:base-image-python-3.7-v0.0.1

RUN  apt-get update && apt-get install sqlite3 curl -y
RUN pip install --upgrade pip

# Set the timezone to IST (Indian Standard Time)
ENV TZ=Asia/Kolkata

ENV PORT 5000
# Expose the port that the Flask application will run on
EXPOSE $PORT

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt ./

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Set the environment variable for Flask
#ENV FLASK_APP=main.py

# Run the Flask application
#CMD ["flask", "run", "--host=0.0.0.0","--port=$PORT"]
CMD flask run --host=0.0.0.0 --port $PORT

