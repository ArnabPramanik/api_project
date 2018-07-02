from flask import Flask,jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='views')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from controllers import *

if __name__ == '__main__':
    app.run()