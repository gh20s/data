#!/bin/bash

# This script is provided to start  PostgreSQL and wait for it to be available before completing.

# Usage:
#   ./ready_local_db.sh


echo "Running docker"
docker-compose up -docker

# Wait until PostgreSQL is available before moving on
attempts=0
until docker container exec test_db psql -U postgres -c 'SELECT 1' > /dev/null 2>&1; do
  ((attempts=attempts+1))
  if [ $attempts -ge 10 ]; then
    echo "Failed to connect to PostgreSQL after 10 attempts, aborting"
    exit 1
  fi

  echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done
sleep 1 # sometimes a bit of extra time is needed before it's ready for apps to connect
echo "PostgreSQL is available"