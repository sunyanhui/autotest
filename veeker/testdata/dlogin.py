#!/usr/bin/python2.7  
# -*- coding: utf-8 -*-

test_login_case1 = \
dict(tag='no', useraccount='15000000049', password='888888', vertifycode='11',rememberusername='yes',result=True)

test_login_case2 = \
dict(tag='yes', useraccount='', password='888888', vertifycode='11',rememberusername='no',result=False)
