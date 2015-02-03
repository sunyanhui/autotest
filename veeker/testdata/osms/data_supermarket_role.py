#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
from ..account import Account
from common.output import Model

#testcase1 验证正常添加角色
test_modify_role_case1 = Model(
    username = Account.supermarket,
    password = Account.supermarket_password,
    role_name = 'tester',
)

#testcase1 验证删除角色
test_modify_role_case2 = Model(
    username = Account.supermarket,
    password = Account.supermarket_password,
    role_name = 'tester',
)