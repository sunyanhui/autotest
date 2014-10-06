#!/usr/bin/python2.7  
# -*- coding: utf-8 -*-

#个人正常登录
test_login_case1 = dict(tag='yes',
    username='15000000237', password='888888', verifycode='11',ifrememberusername='yes')

#分销商正常登录
test_login_case2 = dict(tag='yes',
    username='15000000245', password='888888', verifycode='11',ifrememberusername='yes')

#企业正常登录
test_login_case3 = dict(tag='yes',
    username='XYHD3100085', password='888888', verifycode='11',ifrememberusername='yes')

#用户名输入为空
test_login_case4 = dict(tag='yes',
    username='', password='888888', verifycode='11',ifrememberusername='yes')

#用户名输入错误
test_login_case5 = dict(tag='yes',
    username='a5000000491', password='888888', verifycode='11',ifrememberusername='yes')

#用户名输入在正确的基础上多1位
test_login_case6 = dict(tag='yes',
    username='150000002371', password='888888', verifycode='11',ifrememberusername='yes')

#密码输入错误
test_login_case7 = dict(tag='yes',
    username='15000000237', password='111111', verifycode='11',ifrememberusername='yes')

#密码输入为空
test_login_case8 = dict(tag='yes',
    username='15000000237', password='', verifycode='11',ifrememberusername='yes')

#验证码输入为空
test_login_case9 = dict(tag='yes',
    username='15000000237', password='888888', verifycode='',ifrememberusername='yes')