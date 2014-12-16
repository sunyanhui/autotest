#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
pwd = os.path.dirname(__file__)
pom = [i.split('.')[0] for i in os.listdir(pwd) if i.endswith('.py') and not i.startswith('__init__')]
for i in pom:
    exec("from . import %s"%i)