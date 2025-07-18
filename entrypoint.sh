#!/bin/sh
source .env

echo "Waiting for Database..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done
echo "Database started"
exec "$@"
