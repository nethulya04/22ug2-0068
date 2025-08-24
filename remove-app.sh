#!/bin/bash
echo "Removing all app resources..."
# The -v flag removes named volumes, --rmi all removes images
docker-compose down -v --rmi all
# As a safeguard, manually remove network and volume if they persist
docker network rm todo-network >/dev/null 2>&1 || true
docker volume rm mongo-data >/dev/null 2>&1 || true
echo "Removed app."