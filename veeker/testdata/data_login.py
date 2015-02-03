#!/usr/bin/python2.7  
# -*- coding: utf-8 -*-
from common.output import Model
from .account import Account

#企业正常登录
test_login_case1 = Model(
    username=Account.enterprise,
    password=Account.enterprise_password,
    title=u"七匹狼男装|管理平台")

#个人正常登录
test_login_case2 = Model(
    username=Account.person1,
    password=Account.person1_password,
    title=u"会员服务中心首页")

#市级分销商正常登录
test_login_case3 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    title=u"分销商平台首页")

#分销商操作员正常登录
test_login_case4 = Model(
    username=Account.agency_city_manager,
    password=Account.agency_city_manager_password,
    title=u"分销商平台首页")

#企业操作员正常登录
test_login_case5 = Model(
    username=Account.enterprise_manager_for_login,
    password=Account.enterprise_manager_for_login_password,
    title=u"七匹狼男装|管理平台")

#超市正常登录
test_login_case6 = Model(
    username=Account.supermarket,
    password=Account.supermarket_password,
    title=u"亚超超市|管理平台")

#联盟店正常登录
test_login_case7 = Model(
    username=Account.shop,
    password=Account.shop_password,
    title=u"联盟店平台首页")

#联盟店操作员正常登录
test_login_case8 = Model(
    username=Account.shop_manager_for_login,
    password=Account.shop_manager_for_login_password,
    title=u"联盟店平台首页")

#超市操作员正常登录
test_login_case9 = Model(
    username=Account.supermarket_manager_for_login,
    password=Account.supermarket_manager_for_login_password,
    title=u"亚超超市|管理平台")