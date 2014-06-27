Welcome to muscle
===

Muscle is a school project started by Luciano to monitor some sensors coupled on <b>CYPRESS PSoC4 microcontroller</b>.

All low level programming was implemented by him, the django platform and all high level programming was implemented by me.

We will use it to learning about python, django and C programming.


### Communication structure

The board sends when requested sensor's informations to be processed by django and save it in database.

The data is received in hexadecimal format, so, to the application understand the data, was used a structure to let it easier. Below it is displayed.

####Estrutura TLV

| Start | Version | Timestamp | Type | Format | Len | paylod |
| ----- |:-------:|:---------:|:----:|:------:|:---:| ------:|
| 2 Bytes | 2 Bytes | 4 Bytes | 2 Bytes | 1 Byte | 2 Bytes | len(Bytes) |


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
