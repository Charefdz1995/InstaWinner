# InstaWinner

InstaWinner is an application to Select a winner and he must be follower to this page . 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

* [Python 3](https://www.python.org/download/releases/3.0/) 



### Installing

A step by step series of examples that tell you how to get a development env running

After downloading the repo , from your command prompt or terminal run the following command

```
pip3 install -r requirement_file.txt
```
wait for the dependencies to be installed and then 
Run the following command 

Download [Chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=2.40/) suitable to your OS

extract the file and copy it to the static Folder (Linux is default replace if other OS ) 

### Authentication
to login to your IG you have to set your username and password in base.yaml (static/base.yaml)


Start the server by 
```
 python3 manage.py startserver
```
now you can access your application via Localhost and the django default port 8000 or type in your browser 

```
http://127.0.0.1:8000
```

## Built With

* [Python](https://www.python.org/download/releases/3.0/?) 
* [Django](https://www.djangoproject.com/) - The web framework used
* [YAML](http://yaml.org/) - YAML Ain't Markup Language :data serialization standard
* [selenium](https://www.seleniumhq.org/projects/webdriver/) - Selenium is a suite of tools specifically for automating web browsers.






## Authors:

* **Charef Eddine CHERRAD** - *Initial work* - [Charefdz1995](https://github.com/Charefdz1995)

