#!/bin/bash

echo "Starting Django project setup..."
sleep 4

echo -n "Creating migrations..."
python manage.py makemigrations
echo "Done!"

sleep 4

echo -n "Applying migrations..."
python manage.py migrate
sleep 4

echo "Starting development server..."
python manage.py runserver
