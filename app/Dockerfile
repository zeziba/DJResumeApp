# pull official base image
FROM debian:11

# set work directory
WORKDIR /usr/src/app

# Setup env for python
RUN apt-get update -y
RUN apt-get install -y python3.9 python3-pip curl

# Install Pyscopg2 dependencies
RUN apt-get install -y postgresql-server-dev-all gcc python3-dev musl-dev netcat

# Install NPM
RUN apt-get update && apt-get install -y \
    software-properties-common \
    npm
RUN npm install npm@latest -g && \
    npm install n -g && \
    n latest

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN npm install --prefix ./app/static bootstrap-sass bootstrap sass

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]