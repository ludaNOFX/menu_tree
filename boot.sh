#!/bin/bash
# this script is used to boot a Docker container with Daphne

# Wait for the database to be ready if necessary
while true; do
    python manage.py migrate --noinput
    if [ "$?" -eq 0 ]; then
        break
    fi
    echo "Migration command failed, retrying in 5 secs..."
    sleep 5
done

# Collect static files
python manage.py collectstatic --noinput

exec python manage.py runserver 0.0.0.0:8000

