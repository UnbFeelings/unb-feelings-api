#!/bin/sh

echo "Creating migrations and insert into psql database"
python3 manage.py makemigrations
python3 manage.py migrate

echo "Run the server"
python3 manage.py runserver 0.0.0.0:8000
