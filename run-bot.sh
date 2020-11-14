#!/bin/sh

echo 'Removing Old View Bot container...'
docker rm view-bot || true

echo ""
echo "Building Docker Image for View Bot..."
docker build -t view-bot .

echo ""
echo "Running View Bot..."
docker run --name=view-bot view-bot