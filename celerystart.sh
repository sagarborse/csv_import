#!/bin/bash
echo "Starting Celery CSV"
if [[ ! -e logs/elements.log ]]; then
    mkdir -p logs
    touch logs/elements.log
    chmod +x logs/elements.log
fi

cd /elements/src/
celery -A core worker -l info -Q csv_queue  --concurrency=1