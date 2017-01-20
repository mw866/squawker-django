## Description: 
A Twitter clone implemented with Django.

## References
* Django Tutorial: https://docs.djangoproject.com/en/1.10/intro/
* Bootstrap Tutorial: http://www.w3schools.com/bootstrap/default.asp
* Deploy Djando projects on Heroku: https://devcenter.heroku.com/articles/django-app-configuration#migrating-an-existing-django-project
* Setup Django for Postgres: https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/content/optional_postgresql_installation/
* Provision Postgres on Heroku: https://devcenter.heroku.com/articles/getting-started-with-python#provision-a-database
* Tutorial on Django's Built-in Login System: https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html
* Failproof Django Favicons: http://staticfiles.productiondjango.com/blog/failproof-favicons/
## Instructions
* Run Django development server:
** Visiting NOT from localhost, run 'python manage.py runserver'
** Visiting form localhost, run 'python manage.py runserver 0.0.0.0:8000'
* Install Postgres locally: https://www.postgresql.org/download/linux/ubuntu/
* Connect to Postgres locally: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04
$ sudo -i -u postgres
$ psql
=> create user <Linux username>;
=> create database <database name> owner <Linux username>;
=> \q 
$ exit #to normal user 
vagrant:$ psql <databasename>
* Pull and Push Postgres between Heroku and Local: https://devcenter.heroku.com/articles/heroku-postgresql#pg-push-and-pg-pull

## Troubleshooting
* "ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?"
**  try Python3 instead. 
* Heroku/Gunicorn logs using '''heroku logs -app <app_name>''': https://devcenter.heroku.com/categories/command-line
* Postgres peer authentication fails: psql user is authenticated using Linux user
