# First Step
docker-compose exec web python manage.py migrate --noinput

# Check on database(Sql)
docker-compose exec db psql --username=resume_admin --dbname=resume_dev

# Entry for query of database
resume_dev# \l
resume_dev# \dt
resume_dev# \c resume_dev

# Inspect the database
docker volume ls # Pick correct volume
docker volume inspect djresumeapp_postgres_data

# Run the migrate command on the docker manage.py
docker-compose -f docker-compose.prod.yml exec web python3 manage.py migrate --noinput

# Copy static files to the proper locations
docker-compose -f docker-compose.prod.yml exec web python3 manage.py collectstatic --no-input --clear

# Setup super user
docker-compose exec web python3 manage.py migrate
docker-compose exec web python3 manage.py createsuperuser

# Run the tests
docker-compose exec web python3 manage.py test