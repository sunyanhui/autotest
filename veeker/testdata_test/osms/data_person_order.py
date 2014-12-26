#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common.output import Model

#test_order_case1
# 正常商品-超下订单数据
test_order_case1_person = Model(
    username='23000000001',password='888888',goodname=u'测试专用-正常商品-超',goodsnumber='1',goodsprice=999.9)


test_order_case1_supermarket = Model(
    username='XYHD3100030',password='888888',)

#test_order_case2
# 团购商品-超下订单数据
test_order_case2_person = Model(
    username='23000000001',password='888888',goodname=u'测试专用-团购商品-超',goodsnumber='1',goodsprice=999.9)


test_order_case2_supermarket = Model(
    username='XYHD3100030',password='888888')

#test_order_case3
# 打折商品-超下订单数据
test_order_case3_person = Model(
    username='23000000001',password='888888',goodname=u'测试专用-打折商品-超',goodsnumber='1',goodsprice=999.9)


test_order_case3_supermarket = Model(
    username='XYHD3100030',password='888888',)

#test_order_case4
# 打折商品-超下订单数据
test_order_case4 = Model(
    username='23000000001',password='888888',goodname=u'测试专用-正常商品-超',goodsnumber='1',goodsprice=999.9)


#test_order_case5
# 打折商品-超下订单数据(有联盟店)
test_order_case5_person = Model(
    username='41000000019',password='888888',goodname=u'测试专用-正常商品-超',goodsnumber='1',goodsprice=999.9)


test_order_case5_shop = Model(
    username='31000000001',password='888888')