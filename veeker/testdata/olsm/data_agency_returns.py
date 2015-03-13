#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common.output import Model
from ..account import Account

#testcase1 验证正常退货流程
test_returns_case1_person = Model(
    username = Account.person_for_agency_sales_return,
    password = Account.person_for_agency_sales_return_password,
    goods_name = u"测试专用-正常商品-企"
)

test_returns_case1_agency = Model(
    username = Account.agency_city,
    password = Account.agency_city_password,
)
