# Squawker on Django
 
A Twitter clone implemented with Django.

## Instructions

### Install dependency
    * From `Pipfile` with ```pipenv install``` 
    * From `Pipfile.lock` with ```pipenv install --ignore-pipfile```

### Run Django development server locally

    * Visiting from localhost, ```python manage.py runserver 127.0.0.1:8000```
    * Visiting NOT from localhost, run ```python manage.py runserver```

    https://docs.djangoproject.com/en/3.1/ref/django-admin/

### Run Heroku locally
```
heroku config:get -a mw866-squawker  DATABASE_URL  -s  >> .env 
heroku local
```


### Configure Postgres (On MacOS )

```
brew install postgresql
pg_ctl -D /usr/local/var/postgres start
```
https://dataschool.com/learn-sql/how-to-start-a-postgresql-server-on-mac-os-x/

Create database
```
psql postgres
=> create user <Linux username>;
=> create database <database name> owner <database username>;
=> GRANT ALL PRIVILEGES ON DATABASE <database name>  TO <database username>;
=> \q 

$ exit 
```
https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

```
python manage.py migrate
```
### Generate [Django Secret Key](https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-SECRET_KEY)
```
from django.core.management.utils import get_random_secret_key  
get_random_secret_key()
```

* Pull and Push Postgres between Heroku and Local: https://devcenter.heroku.com/articles/heroku-postgresql#pg-push-and-pg-pull

## Troubleshooting
### Error: pg_config executable not found.
Solution: Install PostgreSQL. For example, ```brew install postgresql```
## References

* Django Tutorial: https://docs.djangoproject.com/en/1.10/intro/
* Bootstrap Tutorial: http://www.w3schools.com/bootstrap/default.asp
* Deploy Djando projects on Heroku: https://devcenter.heroku.com/articles/django-app-configuration#migrating-an-existing-django-project
* Setup Django for Postgres: https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/content/optional_postgresql_installation/
* Provision Postgres on Heroku: https://devcenter.heroku.com/articles/getting-started-with-python#provision-a-database
* Tutorial on Django's Built-in Login System: https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html
* Failproof Django Favicons: http://staticfiles.productiondjango.com/blog/failproof-favicons/