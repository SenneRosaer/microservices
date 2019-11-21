#!/bin/sh

echo "Waiting for the database..."

while ! nc -z users-db 5432; do
  sleep 0.1
done

echo "Database started"

gunicorn -b 0.0.0.0:5001 manage_rating:app