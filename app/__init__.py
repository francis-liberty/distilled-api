#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" init file for app.
"""
from functools import partial

from flask import Flask
from flask import jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from app import models
from app import utils
from app import admin


# Use Flask's error handler instead of the one in flask-restful.
app.handle_exception = partial(Flask.handle_exception, app)
app.handle_user_exception = partial(Flask.handle_user_exception, app)

@app.errorhandler(utils.APIException)
def error_handler(api_exception):
    return jsonify(api_exception.to_dict())

@app.route('/')
@app.route('/test')
def test():
    return 'Hello world from {}!'.format(__name__)
