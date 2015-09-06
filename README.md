# music-network

Iron Yard final project

# Cleff

Cleff is a social network where musicians can meet musicians near them.  Musicians create accounts and 
build their public profile as a resume so people can make a conscious decision if they want to talk to the 
person or not.  A users home page is a page with a sample from all the uses in their area that have posted a
youtube sample of their playing. In addition to musicians, non-musicians can sign up, view local musicians,
and communicate with musicians through the non-musician forum.  

I designed the site to update as the user navigates through the site, not requiring a task runner. 


# Running requirements

I made some customizations to django-geoposition so my project requires a pip install from my github page. 

* Pip install git+https://github.com/lancekrogers/django-geoposition

* Pip install requirements.txt

* Install Postgres onto you're system and create a user and database to use.
  Start the Postgres server.  Open music-network/cleff/cleff/settings.py/ ;
  find DATABASES and replace 'NAME':, 'cleff',  'USER': 'cleff', with 
  'NAME': 'your database name', 'USER': 'your database username'.

* Install geo-django spatial libraries to the system you are using, follow the 
  instructions in the documentation 
  https://docs.djangoproject.com/en/1.8/ref/contrib/gis/install/geolibs/

* Install ElasticSearch on your system 

* cd music-network/cleff/ 
  then type ./manage.py runserver
  hit enter and go to localhost:8000

