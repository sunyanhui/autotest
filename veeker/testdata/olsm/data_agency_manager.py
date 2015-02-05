#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common.output import Model
from ..account import Account

#testcase1 验证正常添加管理员
test_modify_manager_case1 = Model(
    username = Account.agency_city,
    password = Account.agency_city_password,
    manager_account = Account.agency_city_manager_for_test
)

#testcase2 验证删除管理员
test_modify_manager_case2 = Model(
    username = Account.agency_city,
    password = Account.agency_city_password,
    manager_account = Account.agency_city_manager_for_test
)