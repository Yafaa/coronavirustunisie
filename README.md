# Full Stack Nanodegree Project: Item Catalog

## What is this project ?
An application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

A RESTful web application using the Python framework Flask along with implementing third-party OAuth authentication

### Set Up Instructions
Follow these instructions to set up the Vagrant Linux Environment and the Item Catalog Project

## Prerequisite Resources
You will need the following Python resources for it to run:

Python 2.7 or above (https://www.python.org/downloads/).
Git (https://git-scm.com/downloads).
Vagrant (https://www.vagrantup.com/).
VirtualBox (https://www.virtualbox.org/wiki/Downloads).
Sqlalchemy (https://www.sqlalchemy.org/download.html).
You will need the following other resources for it to run:

Flask (http://flask.pocoo.org/).
Httplib2 (https://pypi.python.org/pypi/httplib2/0.10.3).
Oauth2client (https://pypi.python.org/pypi/oauth2client/).
Web browser i.e. Chrome (https://www.google.com/chrome/)

## Installation
Install Git (https://git-scm.com/downloads) on the local machine
Install Python 2.7 or above (https://www.python.org/downloads/) on the local machine
Install VirtualBox (https://www.virtualbox.org/wiki/Downloads) on the local machine
Install Vagrant (https://www.vagrantup.com/) on the local machine

## Preparing the Virtual Machine
Run the command 'vagrant up' to download and install the linux operating system.
Run the command 'vagrant ssh' to log in to the virtual machine.
Install Flask (http://flask.pocoo.org/) with pip install Flask, if it is not installed already.
Install Sqlalchemy, Httplib2 and Oauth2client with sudo apt-get install, if they are not installed already.

## Setup the Database
After the initial setup you can load the project files while connected to vagrant.

Navigate to cd project:


Run python database_setup.py
Run your web browser.


## Preparing the Project
In order to run the project you must have:


Run dbSetup.py with the python dbSetup.py command.
Run the command python project.py in order to start the item-catalog.
Navigate to http://localhost:5000 on your web browser for access.
Useful Editors:
