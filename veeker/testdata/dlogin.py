#!/usr/bin/python2.7  
# -*- coding: utf-8 -*-

#正常登录
test_login_case1 = dict(tag='yes',
    username='15000000049', password='888888', verifycode='11',ifrememberusername='yes')

#用户名输入为空
test_login_case2 = dict(tag='yes',
    username='', password='888888', verifycode='11',ifrememberusername='yes')

#用户名输入错误
test_login_case3 = dict(tag='yes',
    username='150000000491', password='888888', verifycode='11',ifrememberusername='yes')

#用户名输入错误
test_login_case4 = dict(tag='yes',
    username='1500000004a', password='888888', verifycode='11',ifrememberusername='yes')

#密码输入为空
test_login_case5 = dict(tag='yes',
    username='15000000049', password='', verifycode='11',ifrememberusername='yes')

#密码输入错误
test_login_case6 = dict(tag='yes',
    username='1500000004a', password='111111', verifycode='11',ifrememberusername='yes')