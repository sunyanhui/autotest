#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common.output import Model
from ..account import Account

#testcase1 验证正常发布商品
test_goods_case1 = Model(
    username = Account.supermarket,
    password = Account.supermarket_password)