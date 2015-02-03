#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
from ..account import Account
from common.output import Model

#testcase1 验证正常修改超市密码
test_modify_password_case1 = Model(
    username    = Account.supermarket,
    password    = Account.supermarket_password,
    oldPassword = Account.supermarket_password,
    newPassword = '111111',
)

#testcase2 把密码修改回来
test_modify_password_case2 = Model(
    username    = Account.supermarket,
    password    = '111111',
    oldPassword = '111111',
    newPassword = Account.supermarket_password,
)