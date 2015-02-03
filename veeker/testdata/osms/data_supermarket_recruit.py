#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
from common.output import Model
from ..account import Account

#testcase1 验证正常添加招聘信息
test_recruit_case1 = Model(
    username = Account.supermarket,
    password = Account.supermarket_password,)
