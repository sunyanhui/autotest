#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
from common.output import Model
from ..account import Account

#testcase1 验证正常添加公告
test_notice_case1 = Model(
    username = Account.enterprise,
    password = Account.enterprise_password)
