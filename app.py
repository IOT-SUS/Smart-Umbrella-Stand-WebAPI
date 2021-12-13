from flask import Flask
from flask import request
from flask import jsonify

from flask_pymongo import PyMongo

app = Flask(__name__)

# add config
from cfg import config

# server
app.config['SERVER_NAME'] = config.SERVER_NAME

# mongodb
app.config["MONGO_URI"]  = config.MONGO_URI

# json web token
app.config['FAKE_TOKEN']        = config.TOKEN_FAKE
app.config['TOKEN_SECRET_KEY']  = config.TOKEN_SECRET_KEY
app.config['TOKEN_EXPIRE_TIME'] = config.TOKEN_EXPIRE_TIME

# python mongodb
mongo  = PyMongo(app)


# add router
from router import *