#!/bin/bash
./wait-for-it.sh db_order:5432
./manage.py migrate
./manage.py runserver 0.0.0.0:8000
