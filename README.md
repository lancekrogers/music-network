# music-network
final project

I am setting out to build a social network primarily for muscisians for my final Iron Yard project.
First I will build a basic django crud app and rest api for the MVP.  I plan to have this done by wed
and add permissions thursday and friday.  The next step will be to build a simple front end application 
with css and javascript that communicates with my django backend.  If I have time I plan on building 
an android front end that also talks to my django backend.


All features have been taking more time than expected. I am now building a presentable application, and
will work on the api after I have a presentable product.  As of right now there is an easily updatable
profile and musician to musician messaging.  Next I will work on finishing up the forum functionality,
and then I can tie the three apps together in cleff_main.  Cleff_main will contain the main flow of the
site.  Users will have a feed with content after the first log in with users in their area,
there will be a button to the forum on one side, and button to update your profile and a button to your inbox
on the other.  I might try to figure out how to do a slide in button menu containing links to all the pages in 
my site.

# Running requirements

I made some customizatinos to django-geoposition.  My project requires a pip install from my github page. 

* Pip install git+https://github.com/lancekrogers/django-geoposition

* Pip install requirements.txt

* Install Postgres onto you're system and create a user and database to use.
  Start the Postgres server.  Open music-network/cleff/cleff/settings.py/ ;
  find DATABASES and replace 'NAME':, 'cleff',  'USER': 'cleff', with 
  'NAME': 'your database name', 'USER': 'your database username'.

* Install geo-django to the system you are using, follow the 
  instructions in the documentation 
  https://docs.djangoproject.com/en/1.8/ref/contrib/gis/

* Install ElasticSearch on your system 

* ./manage.py runserver

