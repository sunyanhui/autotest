#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common.output import Model
from ..account import Account

#testcase1 验证联盟店基本信息
test_shop_basic_information_case1 = Model(username = Account.shop, password = '888888')