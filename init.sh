#!/bin/bash

echo "Running collectstatic"
python src/manage.py collectstatic --noinput
echo "Running migrations"
python src/manage.py migrate --noinput

/usr/bin/supervisord
