#!/bin/bash
echo "Starting Microservice"
if [[ ! -e logs/elements.log ]]; then
    mkdir -p logs
    touch logs/elements.log
    chmod +x logs/elements.log
fi
if [[ ! -e logs/gunicorn-access.logs ]]; then
    touch logs/gunicorn-access.logs
    chmod +x logs/gunicorn-access.logs
fi
if [[ ! -e logs/gunicorn-errors.logs ]]; then
    touch logs/gunicorn-errors.logs
    chmod +x logs/gunicorn-errors.logs
fi
cd /elements/src
python -u manage.py makemigrations
python -u manage.py migrate
python  manage.py collectstatic --noinput

#gunicorn --workers=${WORKERS} -b 0.0.0.0:${APP_PORT} --access-logfile /elements/logs/gunicorn-access.logs --error-logfile /elements/logs/gunicorn-errors.logs core.wsgi
python -u /commservice/src/manage.py runserver 0.0.0.0:80
