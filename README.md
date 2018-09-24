# Multi Author Blog
A multi author blog built with Django 2.0. [I followed a tutorial by Corey Schafer] (https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

## Getting Started
This section describes how to set up an environmet to run and test the project.

### Prerequisites
* You have a working installation of Python 3.6.*
* You can install software on your system.
* You can create and activate Python virtual environments.

### Setup
Create a Python virtual environment somewhere on your system and activate it.
Your shell prompt should look something like this:
```
(env)[username@computer pwd]$
```

Clone this repository into the directory of your choice like so:
```
git clone https://github.com/Williano/Multi-Author-Blog.git
```

`cd` into the project root directory and install the needed requirements.
NB: Ensure your virtual environment is activated.
```
cd Multi-Author-Blog/
pip install -r requirements.txt
```

Setup the database by running the following.
```
python manage.py makemigrations
python manage.py migrate
```

### Running
When all is okay, you can start the local development server.
```
python manage.py runserver
```

Visit `localhost:8000` in your browser.
