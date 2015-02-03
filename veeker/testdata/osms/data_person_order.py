#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from ..account import Account
from common.output import Model

#test_order_case1
# 正常商品-超下订单数据
test_order_case1_person = Model(
    username=Account.person1,
    password=Account.person1_password,
    goodname=u'测试专用-正常商品-超',
    goodsnumber='1',
    goodsprice=999.9)

test_order_case1_supermarket = Model(
    username=Account.supermarket,
    password=Account.supermarket_password)

#test_order_case2
# 团购商品-超下订单数据
test_order_case2_person = Model(
    username=Account.person1,
    password=Account.person1_password,
    goodname=u'测试专用-团购商品-超',
    goodsnumber='1',
    goodsprice=999.9)

test_order_case2_supermarket = Model(
    username=Account.supermarket,
    password=Account.supermarket_password)

#test_order_case3
# 打折商品-超下订单数据
test_order_case3_person = Model(
    username=Account.person1,
    password=Account.person1_password,
    goodname=u'测试专用-打折商品-超',
    goodsnumber='1',
    goodsprice=999.9)

test_order_case3_supermarket = Model(
    username=Account.supermarket,
    password=Account.supermarket_password)

#test_order_case4
# 打折商品-超下订单数据
test_order_case4 = Model(
    username=Account.person1,
    password=Account.person1_password,
    goodname=u'测试专用-正常商品-超',
    goodsnumber='1',
    goodsprice=999.9)

#test_order_case5
# 打折商品-超下订单数据(有联盟店)
test_order_case5_person = Model(
    username=Account.person2,
    password=Account.person2_password,
    goodname=u'测试专用-正常商品-超',
    goodsnumber='1',
    goodsprice=999.9)

test_order_case5_shop = Model(
    username=Account.shop,
    password=Account.shop_password)