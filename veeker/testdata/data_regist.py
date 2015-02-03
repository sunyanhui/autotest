#!/usr/bin/python2.7  
# -*- coding: utf-8 -*-
from common.output import Model

#测试是否可以收到验证码
test_regist_case1 = Model(tag='yes',
    province=u'河南省',city=u'许昌市',nickname='random',password='888888',confirmpassword='888888')