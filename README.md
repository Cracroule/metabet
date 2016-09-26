# metabet

Football data and API. Developed in Python 3.5.1 with Django 1.10.

## Prequisites

You need:
- A python 3.5 virtualenv
- PostgreSQL

## Setup

- install requirements:
````
pip install -r requirements.txt
````
- Create a database named metabet, with no password:
````
CREATE DATABASE metabet;
````
- Launch the database migration:
````
./manage.py migrate
````
- load a season's data (eg 2016-2017):
````
./manage.py load_competition 2016-2017
````
- launch the server
````
./manage.py runserver 5000
````
- The API is now accessible through [http://localhost:5000/api/competitions/](http://localhost:5000/api/competitions/)
