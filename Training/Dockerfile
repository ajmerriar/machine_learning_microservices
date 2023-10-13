# Use Ubuntu as the base image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Update and install required packages
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip nano

# Copy your code into the container
COPY ./training /app

# Install required Python packages
RUN pip3 install numpy pandas keras scikit-learn matplotlib tensorflow keras_preprocessing 

# Expose any necessary ports (if applicable)
# EXPOSE 80

# Define the command to run your code when the container starts
# CMD ["python3", "script.py"]
CMD ["python3", "train.py"]
