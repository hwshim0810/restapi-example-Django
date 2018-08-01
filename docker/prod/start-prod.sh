#!/bin/bash

mkdir -p /var/log/uwsgi/restexample

/root/.pyenv/versions/app/bin/pip install -r requirements.txt
/root/.pyenv/versions/app/bin/python manage.py migrate --noinput

/root/.pyenv/versions/app/bin/uwsgi --ini ./.config/uwsgi/restexample.ini
