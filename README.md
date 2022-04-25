# Modern Resume App using Django
This django app focus on making a clean and intuitive resume app that can support multiple resumes at the same time.

### Files that are needed but not included, these are settings files
.env.prod

.env.prod.db

#### Examples of the above files can be found at
[.env.prod](Examples/.env.prod)

[.env.prod.db](Examples/.env.prod.db)

## Dependancies
### npm
Install npm and run the following command to install bootstrap and boostrap-sass

If the static folder does not exist create it

`mkdir ./app/static`

#### Install Node models for bootstrap
`npm install --prefix ./app/static bootstrap-sass bootstrap`

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

### Use if default sass run
`docker-compose exec web python3 manage.py compilescss`

### Use only the complied css needs to be moved to the static folder
`docker-compose exec web python3 manage.py compilescss --use-storage`

`docker-compose exec web python3 manage.py collectstatic --no-input --clear`


#### Run if the database is having issues
`docker-compose exec web python3 manage.py migrate --run-syncdb`

# Database commands
### Check on database(Sql)
`docker-compose exec db psql --username=resume_admin_prod --dbname=resumeapp_prod`

### Entry for query of database
`resume_dev# \l`

`resume_dev# \dt`

`resume_dev# \c resume_dev`
