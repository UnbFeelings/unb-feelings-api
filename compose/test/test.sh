#!/bin/sh

echo "Deleting migrations"
find . -path "*/migrations/*.pyc"  -delete
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

echo "Deleting staticfiles"
find . -path "ferramenta_custos/static/*"  -delete

echo "Creating migrations and insert into psql database"
python3 manage.py makemigrations
python3 manage.py migrate
