## Description: 
A Twitter clone implemented with Django.

## References
* Django Tutorial: https://docs.djangoproject.com/en/1.10/intro/
* Bootstrap Tutorial: http://www.w3schools.com/bootstrap/default.asp
* Deploy Djando projects on Heroku: https://devcenter.heroku.com/articles/django-app-configuration#migrating-an-existing-django-project
* Setup Django for Postgres: https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/content/optional_postgresql_installation/


## Instructions
* Run Django development server:
** Visiting NOT from localhost, run 'python manage.py runserver'
** Visiting form localhost, run 'python manage.py runserver 0.0.0.0:8000'
* Install Postgres locally: https://www.postgresql.org/download/linux/ubuntu/
* Install and Connect to Postgres: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04
$ sudo -i -u postgres
$ psql
=> create user <Linux username>;
=> create database <database name> owner <Linux username>;
=> \q 
$ exit #to normal user 
vagrant:$ psql <databasename>



## Troubleshooting
* "ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?"
**  try Python3 instead. 
* Heroku/Gunicorn logs using '''heroku logs -app <app_name>''': https://devcenter.heroku.com/categories/command-line
* Postgres peer authentication fails: psql user is authenticated using Linux user
