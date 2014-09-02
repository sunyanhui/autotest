#!/usr/bin/python2.7  
# -*- coding: utf-8 -*-

test_login_case1 = \
    dict(tag='yes', useraccount='15000000049', password='888888', vertifycode='11',rememberusername='yes',
        result=True, usernameprompt=None, passwordprompt=None, vertifycodeprompt=u'1验证码错误！！！')

test_login_case2 = \
    dict(tag='no', useraccount='', password='888888', vertifycode='11',rememberusername='no',
        result=False, usernameprompt=u'用户名不能为空1', passwordprompt=None, vertifycodeprompt=None)
