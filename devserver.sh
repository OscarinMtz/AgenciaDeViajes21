#!/bin/sh
source .venv/bin/activate
unset DJANGO_SETTINGS_MODULE
export DJANGO_SETTINGS_MODULE=backend_viajes21.settings
python backend_viajes21/manage.py runserver $PORT
