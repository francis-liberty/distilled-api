#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Script to drop all tables
"""

print 'Please input "yes" to confirm you know what you are doing'
confirm = raw_input()

if confirm == 'yes':
    from app import db
    db.drop_all()
