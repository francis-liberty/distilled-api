#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Configuration file.
"""
import os

# Debug or not
DEBUG = True

# Make jsonfiy encode in utf-8.
JSON_AS_ASCII = False

# Secret key.
SECRET_KEY = 'Secret Key'

# Database & sqlalchemy.
DB_USERNAME = 'feeds-api'
DB_PASSWORD = 'feeds-password'
DB_SERVER = 'feeds-password'
DB_NAME = 'feeds-api'
SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(
    DB_USERNAME, DB_PASSWORD, DB_SERVER, DB_NAME)
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

# The md5 for default avatar.
DEFAULT_AVATAR_MD5 = '587c36119c43e7383b739e6093c23150'

# Data/Time format we use.
DATE_FORMAT = '%Y-%m-%d'
TIME_FORMAT = '%H:%M:%S'
DATETIME_FORMAT = ' '.join([DATE_FORMAT, TIME_FORMAT])

# The maximum content size when uploading.
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
# The maximun block size we read every time when processing file.
BLOCKSIZE = 65536
# The directory to store uploaded files.
UPLOAD_DIR = 'uploads'
UPLOAD_URL = UPLOAD_DIR
UPLOAD_FOLDER = os.path.realpath(os.path.join(
    os.path.dirname(__file__),
    UPLOAD_DIR,
))
UPLOAD_AVATAR_DIR = 'avatars'
UPLOAD_AVATAR_URL = os.path.join(UPLOAD_URL, UPLOAD_AVATAR_DIR)
UPLOAD_AVATAR_FOLDER = os.path.realpath(os.path.join(
    UPLOAD_FOLDER,
    UPLOAD_AVATAR_DIR,
))
