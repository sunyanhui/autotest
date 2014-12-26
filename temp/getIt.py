#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from sex import *

for i in open('.\\sex\\element_person_login.py'):
    if 'By' in i:
        print i.strip()