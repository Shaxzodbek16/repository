#!/bin/bash

echo "Starting Django project setup..."
sleep 4

echo -n "Creating migrations..."
python manage.py makemigrations
echo "Done!"

sleep 4
export DJANGO_SETTINGS_MODULE=repositoryAPI.settings  # Replace 'your_project' with your project's name

echo -n "Applying migrations..."
python manage.py migrate
echo "Done!"
sleep 4
echo "Testing..."
pytest
sleep 4

echo "Starting development server..."
python manage.py runserver
