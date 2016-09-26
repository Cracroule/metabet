# metabet

Football data and API. Developed in Python 3.5.1 with Django 1.10.

## Setup

- create a python 3.5 virtualenv

- install requirements:
````
pip install -r requirements.txt
````
- install PostgreSQL and create a database named metabet, with no password
- Launch the database migration:
````
./manage.py migrate
````
- launch the server
````
./manage.py runserver 5000
````
- The API is now accessible through [http://localhost:5000/api/competitions/](http://localhost:5000/api/competitions/)
