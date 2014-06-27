Welcome to muscle
===


### Getting Started

The technologies used were python, django and sqlite, so, it very simple to use and install. There is a step by step to do the installation

1 -  Clone the <b>git</b> repository

```
git clone https://github.com/vitoratair/muscle
```
	
2 - Install <b>virtualenv</b> on the repository created

```
virtualenv muscle
cd muscle
source bin/activate
```

3 - Install the <b>requirements</b>

```
pip install -r requirements.txt
```

4 - Sync the <b>database</b>

```
(muscle)~VIRTUAL_ENV|master ⇒ python manage.py syncdb
Creating tables ...
Installing custom SQL ...
Installing indexes ...
Installed 0 object(s) from 0 fixture(s)	
```

5 - Run the <b>web server</b>

```
(muscle)~VIRTUAL_ENV|master ⇒ python manage.py runserver
Validating models...
0 errors found
June 27, 2014 - 19:13:51
Django version 1.6, using settings 'muscle.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.	
```
