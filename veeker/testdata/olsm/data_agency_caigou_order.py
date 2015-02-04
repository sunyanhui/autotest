#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common.output import Model
from ..account import Account

# testcase1 分销商正确提交采购订单
test_agency_caigou_order_case1 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password)

# testcase2 分销商撤销采购采购订单
test_agency_caigou_order_case2 = Model(
    username=Account.agency_city,
    password=Account.agency_city_password)