# Change Samba Password

Super easy application to be used to change Samba passwords for external users at SOS.

## How to start

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
That's it! 

**Note:** Inspired by [flask-quickstart.](https://github.com/bittobennichan/flask-quickstart)