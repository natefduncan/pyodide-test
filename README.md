# Flask + Maria DB Boilerplate

[Flask](https://flask.palletsprojects.com/en/1.1.x/) and [Maria DB](https://mariadb.org/) run in [Docker containers](https://www.docker.com/resources/what-container) ([python](https://hub.docker.com/_/python/), [mariadb](https://hub.docker.com/_/mariadb), [adminer](https://hub.docker.com/_/adminer)). Code formatted with [black](https://github.com/psf/black), packages sorted with [isort](https://pycqa.github.io/isort/). CSS formatted with [Bulma](https://bulma.io/). [SqlAlchemy](https://www.sqlalchemy.org/) and [Marshmallow](https://marshmallow.readthedocs.io/en/stable/) used for data models and serialization.

## Installation

1. Clone or fork repository.
2. To install Bulma (CSS): `npm install --prefix ./app/static bulma`
3. To build docker container: `docker-compose build`
4. To run docker container: `docker-compose up`

## Usage

- Website: `localhost:5000`.
- DB Interface: `localhost:8081`
