# pull official base image
FROM debian:11

# set work directory
WORKDIR /usr/src/app

# Setup env for python
RUN apt-get update -y
RUN apt-get install -y python3.9 python3-pip

# Install Pyscopg2 dependencies
RUN apt-get install -y postgresql-server-dev-all gcc python3-dev musl-dev netcat

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]