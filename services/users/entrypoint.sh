#!/bin/sh

echo "Waiting for the database..."

while ! nc -z users-db 5432; do
  sleep 0.1
done

echo "Database started"

python manage.py run -h 0.0.0.0