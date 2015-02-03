#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
from common.output import Model
from ..account import Account

#testcase1 验证添加荣誉、删除荣誉
test_honor_case1 = Model(
    username = Account.enterprise,
    password = Account.enterprise_password)
