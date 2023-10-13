# Use Ubuntu as the base image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Update and install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip nano

# Copy the Flask app files into the container
COPY . /app

# Install Flask and dependencies
RUN pip3 install Flask Pillow numpy keras tensorflow

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the app
CMD ["python3", "app.py"]
