#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common.output import Model
from ..account import Account

# testcase1 联盟状态下拉框数据
test_agency_business_cooperation_case1 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    alliance_status_list=set([u'请选择...',u'已绑定',u'已解绑']))


# testcase2 验证正确的联盟企业搜索
test_agency_business_cooperation_case2 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    company=u'七匹狼')


# testcase3 验证错误的联盟企业搜索
test_agency_business_cooperation_case3 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,
    company=u'错误的搜索')