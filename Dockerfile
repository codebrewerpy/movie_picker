# Use a lightweight Python image as the base image
FROM python:3.9-slim

# Install Git
RUN apt-get update && apt-get install -y git

# Set the working directory
WORKDIR /app

# You can add your application files and do other setup here if needed
