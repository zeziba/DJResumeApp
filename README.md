# Modern Resume App using Django
This django app focus on making a clean and intuitive resume app that can support multiple resumes at the same time.


# Check on database(Sql)
`docker-compose exec db psql --username=resume_admin_prod --dbname=resumeapp_prod`

# Entry for query of database
`resume_dev# \l`
`resume_dev# \dt`
`resume_dev# \c resume_dev`

# Inspect the database
`docker volume ls # Pick correct volume`
`docker volume inspect djresumeapp_postgres_data`

# Copy static files to the proper locations
`docker-compose -f docker-compose.prod.yml exec web python3 manage.py collectstatic --no-input --clear`

# Run the tests
`docker-compose exec web python3 manage.py test`

# After production build run the following commands to ensure all files and databases are setup
`docker-compose exec web python3 manage.py flush --no-input`
`docker-compose exec web python3 manage.py makemigrations`
`docker-compose exec web python3 manage.py migrate`
`docker-compose exec web python3 manage.py createsuperuser`
`docker-compose exec web python3 manage.py collectstatic --no-input --clear`
`docker-compose exec web python3 manage.py migrate --run-syncdb`