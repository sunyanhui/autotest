#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
from common.output import Model
from common.config import IMGPATH
from ..account import Account

#testcase1 验证正常修改企业密码
test_modify_password_case1 = Model(
    username = Account.enterprise,
    password = Account.enterprise_password,
    oldPassword = Account.enterprise_password,
    newPassword = '111111',
)

#testcase2 把密码修改回来
test_modify_password_case2 = Model(
    username = Account.enterprise,
    password = '111111',
    oldPassword = '111111',
    newPassword = Account.enterprise_password
)