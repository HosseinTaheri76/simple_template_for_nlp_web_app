# Nlp web application project

This project is a web application powered by django and python, its goal is to get text input from user and
process it with nlp models and store and show the result.

# Installation

this project runs in docker, so first you need to install docker for you operating system, you can dowload
docker from [here](https://docs.docker.com/get-docker/), don't forget to signup in [docker hub](https://hub.docker.com/)
you will need it.
after docker installation clone this project into your computer and open the terminal in the project root directory and
type

```bash
docker login
```
the enter your credentials, after that enter the command bellow to download necessary files and run the project, this may
take a while.

```bash
docker-compose up --build
```
now you need to apply migrations to build database, oepn another terminal in ther same directory, (note: don't close
current terminal!) then enter the command bellow and wait for it

```bash
docker-compose exec web python manage.py migrate
```

congratulations!!
now you can access the project via address http://127.0.0.1:8000/ on your computer.

# sending commands to docker-compose sevices

you can send you commands for any service defined in docker-compose file like bellow:

```bash
docker-compose exec <service name> <command>
```

we saw an example before when we sent python manage.py migrate command to web service.
