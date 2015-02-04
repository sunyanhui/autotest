#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common.output import Model
from ..account import Account

# testcase1 联盟店正确提交采购订单
test_shop_caigou_order_case1 = Model(
    username=Account.shop,
    password=Account.shop_password)

# testcase2 联盟店撤销采购采购订单
test_shop_caigou_order_case2 = Model(
    username=Account.shop,
    password=Account.shop_password)

# testcase2 联盟店发布采购采购订单
test_shop_caigou_order_case3 = Model(
    username=Account.shop,
    password=Account.shop_password)