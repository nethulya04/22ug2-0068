#!/bin/bash
echo "Preparing app resources..."
docker network create todo-network
docker volume create mongo-data
echo "Preparation complete."