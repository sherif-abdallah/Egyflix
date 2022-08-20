# Egyflix
Egyflix is a free streaming service that allows our members to watch TV shows and movies, You can also download TV shows and movies to your iOS, Android, Windows 10, Macos or Linux and watch.

   

## Table of Content
- [Egyflix](#egyflix)
  * [Tools](#tools)
  * [How to run](#how-to-run)
  * [Author](#author)

## Tools
1. Python
2. Django
3. Sqlite3
4. JavaScript
5. Jquery
7. Bootstrap
8. Boxicons
9. Fontawesome
10. owlcarousel
11. googlefonts
12. tailwind
13. Goormide Cloud


## How to run
* Enter the directory where the script is located then type the following to the console
```sh
$ git clone https://github.com/sherif-abdallah/Egyflix Egyflix
```
* Install Python 3.8 venv, pip and compiler

```sh
$ sudo apt-get install python3.8 python3.8-venv python3-venv
```

* Create a virtual environment to install dependencies in and activate it:

```sh
$ python3.8 -m venv venv
$ source venv/bin/activate
```

* Then install the dependencies:

```sh
(venv)$ cd Egyflix
(venv)$ python -m pip install --upgrade pip
(venv)$ python -m pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

* then you will have to migrate the db

```sh
(venv)$ python manage.py migrate --run-syncdb
```

* Finally run The Egyflix Server
```sh
(venv)$ python manage.py runserver
```
* And navigate to `http://127.0.0.1:8000`.

## Author
[Sherif Abdullah](https://github.com/sherif-abdallah)
