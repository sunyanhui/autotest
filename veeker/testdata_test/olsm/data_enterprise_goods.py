#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common.output import Model
#testcase1 验证正常发布商品
test_goods_case1 = Model(
    username = 'XYHD3101059',
    password = '888888',
    goods_name = u'测试发布商品S',
    goods_stock = '111',
    goods_desc = 'Its only a test',
    price = '100',
    cprice = '100',
    cgprice = '100'
)

#testcase1 验证删除角色
test_modify_role_case2 = Model(
    username = 'XYHD3101059',
    password = '888888',
    role_name = 'tester',
)