#!/usr/bin/python2.7  
# -*- coding: utf-8 -*-
from common.output import Model

#企业正常登录
test_login_case1 = Model(tag='yes',
    username='XYHD3100028', password='888888', if_remember_username='yes', title=u"卡曼妮|管理平台")

#个人正常登录
test_login_case2 = Model(tag='yes',
    username='41000000001', password='888888', if_remember_username='yes', title=u"个人中心首页")

#市级分销商正常登录
test_login_case3 = Model(tag='yes',
    username='41000000002', password='888888', if_remember_username='yes', title=u"分销商平台首页")

#分销商操作员正常登录
test_login_case4 = Model(tag='yes',
    username='41000000003', password='888888', if_remember_username='yes', title=u"分销商平台首页")

#企业操作员正常登录
test_login_case5 = Model(tag='yes',
    username='13000000001', password='888888', if_remember_username='yes', title=u"卡曼妮|管理平台")

#超市正常登录
test_login_case6 = Model(tag='yes',
    username='XYHD3100030', password='888888', if_remember_username='yes', title=u"喜羊羊|管理平台")

#联盟店正常登录
test_login_case7 = Model(tag='yes',
    username='31000000001', password='888888', if_remember_username='yes', title=u"联盟店平台首页")

#联盟店操作员正常登录
test_login_case8 = Model(tag='yes',
    username='50000000002', password='888888', if_remember_username='yes', title=u"联盟店平台首页")

#超市操作员正常登录
test_login_case9 = Model(tag='yes',
    username='11000000001', password='888888', if_remember_username='yes', title=u"喜羊羊|管理平台")