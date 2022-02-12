from celery import Celery
from flask import Flask, jsonify, request, Blueprint
from pymongo import MongoClient
from flask_caching import Cache
from flask_cors import CORS

from .constants import *


app = Flask(__name__)
CORS(app)

app.config['CELERY_BROKER_URL'] = CELERY_BROKER_URL
app.config['CELERY_RESULT_BACKEND'] = CELERY_RESULT_BACKEND
app.config['CACHE_TYPE'] = CACHE_TYPE
app.config['CACHE_REDIS_HOST'] = CACHE_REDIS_HOST
app.config['CACHE_REDIS_PORT'] = CACHE_REDIS_PORT
app.config['CACHE_REDIS_DB'] = CACHE_REDIS_DB
app.config['CACHE_REDIS_URL'] = CACHE_REDIS_URL

cache = Cache(app)

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# celery.conf.broker_url = MONGODB_CON_STR
celery.conf.update(app.config)


db = MongoClient(MONGODB_URL)[DB_NAME]

from .routes import *

# Versioning for extra points
app.register_blueprint(ad, url_prefix="/api/v1/ad")


@app.route('/')
def index_page():
    output = {"msg": "I'm the root endpoint from ad."}
    return jsonify(output)