#!/usr/bin/env sh
set -ex

# DRY command
EXEC_CMD='docker-compose exec web'

# Build the docker image
docker-compose -f docker-compose.prod.yml build

# Launch the app
docker-compose -f docker-compose.prod.yml up --detach

# Wait for the database to go live
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Run migrations
${EXEC_CMD} python3 manage.py makemigrations
${EXEC_CMD} python3 manage.py migrate
${EXEC_CMD} python3 manage.py compilescss
${EXEC_CMD} python3 manage.py collectstatic --no-input --clear

# Run tests
${EXEC_CMD} python3 manage.py test
