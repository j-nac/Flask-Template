from flask import Flask
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)
config = yaml.load(open('../config.yaml', 'rb'))
app.config['SECRET_KEY'] = config['secret_key']

# MySQL setup
app.config['MYSQL_HOST'] = config['mysql_host']
app.config['MYSQL_USER'] = config['mysql_user']
app.config['MYSQL_PASSWORD'] = config['mysql_password']
app.config['MYSQL_DB'] = config['mysql_db']

mysql = MySQL(app)

from flaskr import routes