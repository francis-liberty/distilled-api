#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Script to create database.
"""
from app import db

db.create_all()
