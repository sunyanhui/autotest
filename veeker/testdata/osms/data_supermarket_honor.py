#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
from ..account import Account
from common.output import Model

#testcase1 验证添加荣誉、删除荣誉
test_honor_case1 = Model(
    username = Account.supermarket,
    password = Account.supermarket_password)
