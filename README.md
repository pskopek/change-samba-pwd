# Change Samba Password

Super easy application to be used to change Samba passwords for external users at SOS.

## How to start the application

First clone the repository

```
$ git clone https://github.com/pskopek/change-samba-pwd.git

or using GihHub CLI

$ gh repo clone pskopek/change-samba-pwd
```
Change directory to change-samba-pwd

```
$ cd change-samba-pwd
```
Create a virtual environment and install dependencies
```
$ python -m venv venv
$ source venv/bin/activate
$ python -m pip install --upgrade pip setuptools
$ python -m pip install -r requirements.txt
```

Start the development server
```
$ source venv/bin/activate
$ flask --app flaskr --debug run
```
That's it! You can test the app using http://127.0.0.1:5000/ or http://<your_server_ip>:5000/

## How to deploy the application

Application can be deployed on Apache httpd using mod_wsgi.
See more details here: https://flask.palletsprojects.com/en/2.2.x/deploying/mod_wsgi/

**Note:** Inspired by [flask-quickstart.](https://github.com/bittobennichan/flask-quickstart)