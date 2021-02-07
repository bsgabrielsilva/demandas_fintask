#!/bin/bash

echo "Copy .env-test to .env"
cp .env-test .env

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Apply fixtures
echo "Apply loaddata cidades"
python manage.py loaddata cidades.json

echo "Apply loaddata user"
python manage.py loaddata user.json

echo "Apply api tests"
python manage.py test

# apply collectstatic files
echo "Apply collectstatic --no-input"
python manage.py collectstatic --no-input

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
