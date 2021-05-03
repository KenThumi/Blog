# Blog Application
## Description
Welcome to this Blog application. The app is a platform whereby registered writers can post & edit their articles<br>
provided they have registered. Readers can comment on articles of which the writer has the liberty to delete <br>
delogatory comments. Readers can also subscribe and get notified when a new article is uploaded.

## Author
- [Kenneth Thumi](https://github.com/KenThumi)

## Contact
Email:kenthumi@gmail.com

## Setup instructions
Below are steps to follow:
1. Open cli, navigate to your project folder and clone the project: <br/>
         `git clone https://github.com/KenThumi/Blog.git`
2. Install python, preferably python3.
3. Create a virtual environment: <br/>
         `python3 -m venv virtual`
4. To activate the virtual environment run:<br/>
         `source virtual/bin/activate`
5. Now, in the virtual environment, install Flask to the project using the following command:<br/>
         `pip install flask`
6. Install dependencies that dont come with flask above:<br/>
         `pip install -r requirements.txt` 
7. Install postgres (Linux-Ubuntu).  
        `sudo apt-get update` <br/>
        `sudo apt-get install postgresql postgresql-contrib libpq-dev` <br>  
 Create our own superuser role to connect to the server. <br>
        `sudo service postgresql start` <br>
        `sudo -u postgres createuser --superuser $USER` <br>
        `sudo -u postgres createdb $USER` <br>  
 To save your history, navigate to your home directory and enter the following command to create the .psql_history  <br>
        `touch .psql_history`  <br>
 Connect to the postgres server by typing <br>
        `psql` <br>  
 Create your db. <br>
        `#  CREATE DATABASE your_db;` <br>  
 In your `Config.py` file edit `SQLALCHEMY_DATABASE_URI` variable in `DevConfig` class as below:<br>
        `SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/your_db'` <br>  
 Put your role `username` (computer account name in this case) , role `password `and `your_db`.  
 Run below cli command, inside project folder, to set up the db with our tables: <br/>
            `python3 manage.py db upgrade`  
8. Head over to [New API](https://newsapi.org/) and generate API key. To generate SECRET KEY 
    , open REPL by typing command `python3`. Enter these commands: <br/>
            `import secrets` <br/>
            `secrets.token_hex(16)`<br/>
    Where 16 is key length. Copy the keys to somewhere.
9. To register the SECRET KEY (for csrf protection), MAIL_USERNAME (email for sending mails) and MAIL_PASSWORD <br>
 (email password) to OS for use, enter these commands from the cli. Enter the respective value where necessary <br/>
            `export SECRET_KEY='secret key generated'` <br/>
            `export MAIL_USERNAME='your email'`        <br/>
            `export MAIL_PASSWORD='your email password'`

10. Inside the same folder,  type following commands to start the application:<br/>
            `python3 manage.py server`
11. Open browser and input `http://127.0.0.1:5000`
12. To edit, use IDE of your choice to work with the project, e.g VsCode, Sublime text ,etc.

## Technologies Used
In this project, below is a list of technologies used:
- [Python version 3](https://www.python.org/)
- HTML
- CSS (Less, SCSS)

## Dependencies
Below are all dependencies for this application: <br>

alembic==1.5.8,
blinker==1.4,
click==7.1.2,
dnspython==2.1.0,
dominate==2.6.0,
email-validator==1.1.2,
Flask==1.1.2,
Flask-Bootstrap4==4.0.2,
Flask-Login==0.5.0,
Flask-Mail==0.9.1,
Flask-Migrate==2.7.0,
Flask-Script==2.0.6,
Flask-SQLAlchemy==2.5.1,
Flask-Uploads==0.2.1,
Flask-WTF==0.14.3,
greenlet==1.0.0,
idna==3.1,
itsdangerous==1.1.0,
Jinja2==2.11.3,
Mako==1.1.4,
MarkupSafe==1.1.1,
psycopg2==2.8.6,
python-dateutil==2.8.1,
python-editor==1.0.4,
six==1.15.0,
SQLAlchemy==1.4.11,
visitor==0.1.3,
Werkzeug==0.16.0,
WTForms==2.3.3,

## License info
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2021 © Blog Application
