# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables (optional)
ENV FLASK_APP=core/server.py
ENV FLASK_ENV=production

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN apt-get update && \
    apt-get install -y build-essential gcc && \
    apt-get install -y python3-dev && \
    apt-get install -y apt-utils


RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Make sure run.sh is executable
RUN chmod +x run.sh

# Run run.sh when the container launches
ENTRYPOINT ["./run.sh"]
