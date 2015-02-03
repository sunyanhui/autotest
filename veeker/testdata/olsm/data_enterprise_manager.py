#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
from common.config import IMGPATH
from common.output import Model
from ..account import Account

#testcase1 验证正常添加操作员
test_modify_manager_case1 = Model(
    username = Account.enterprise,
    password = Account.enterprise_password,
    manager_account = Account.enterprise_manager_for_test,
)

#testcase1 验证删除操作员
test_modify_manager_case2 = Model(
    username = Account.enterprise,
    password = Account.enterprise_password,
    manager_account = Account.enterprise_manager_for_test,
)