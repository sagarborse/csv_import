#!/bin/bash
echo "Starting Celery Scheduler for CSV"
if [[ ! -e logs/elements.log ]]; then
    mkdir -p logs
    touch logs/elements.log
    chmod +x logs/elements.log
fi
cd src
celery -A core beat -l info -S django_celery_beat.schedulers:DatabaseScheduler