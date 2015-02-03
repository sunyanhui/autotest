#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
from common.config import IMGPATH
from ..account import Account
from common.output import Model

#testcase1 验证正常添加操作员
test_modify_manager_case1 = Model(
    username = Account.supermarket,
    password = Account.supermarket_password,
    manager_account = Account.supermarket_manager_for_test,
)

#testcase1 验证删除操作员
test_modify_manager_case2 = dict(
    username = Account.supermarket,
    password = Account.supermarket_password,
    manager_account = Account.supermarket_manager_for_test,
)