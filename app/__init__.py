from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from config import Config

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(Config)
db = SQLAlchemy(app)
ma = Marshmallow(app)

from app import routes, models
