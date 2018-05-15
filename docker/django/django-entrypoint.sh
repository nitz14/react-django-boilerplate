#!/usr/bin/env bash

until cd src
do
    echo "Waiting for django volume..."
done

until python manage.py migrate
do
    echo "Waiting for postgres ready..."
    sleep 2
done

python manage.py runserver 0.0.0.0:8000
