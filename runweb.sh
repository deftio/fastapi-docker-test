#!/bin/bash

IMAGE_NAME="web_fastapi_image"
CONTAINER_NAME="web_fastapi_instance"

echo "Rebuilding Docker image: $IMAGE_NAME..."
# Build the Docker image
docker build -t $IMAGE_NAME .

# Check if the container is already running
if [ $(docker ps -q -f name=$CONTAINER_NAME) ]; then
    echo "Container $CONTAINER_NAME is running. Stopping and removing..."
    # Stop the container
    docker stop $CONTAINER_NAME
    # Remove the container after stopping
    docker rm $CONTAINER_NAME
fi

# Run the Docker container
echo "Running new Docker container: $CONTAINER_NAME..."
docker run -d --name $CONTAINER_NAME -p 80:80 $IMAGE_NAME

echo "Container $CONTAINER_NAME has been started successfully."


#docker build -t web_mo1 .
# docker run -d --name web_mo1-app -p 80:80 web_mo1