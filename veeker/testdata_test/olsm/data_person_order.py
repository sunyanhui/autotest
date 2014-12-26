#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common.output import Model

#正常商品下订单数据
test_order_case1_person = Model(
    username='23000000001',password='888888',goodname=u'测试专用-正常商品-企',goodsnumber='1',goodsprice=999.9)

test_order_case1_enterprise = Model(
    username='XYHD3100028',password='888888',)

#团购商品下订单数据
test_order_case2_person = Model(
    username='23000000001',password='888888',goodname=u'测试专用-团购商品-企',goodsnumber='1',goodsprice=999.9)

test_order_case2_enterprise = Model(
    username='XYHD3100028',password='888888',)

#打折商品下订单数据
test_order_case3_person = Model(
    username='23000000001',password='888888',goodname=u'测试专用-打折商品-企',goodsnumber='1',goodsprice=999.9)

test_order_case3_enterprise = Model(
    username='XYHD3100028',password='888888',)

#打折商品下订单数据
test_order_case4 = Model(
    username='23000000001',password='888888',goodname=u'测试专用-正常商品-企',goodsnumber='1',goodsprice=999.9)

#test_order_case6
# 打折商品-超下订单数据(有县级分销商)
test_order_case6_person = Model(
    username='41000000022',password='888888',goodname=u'测试专用-打折商品-企',goodsnumber='1',goodsprice=999.9)

test_order_case6_agency = Model(
    username='41000000020',password='888888',)

#test_order_case7
# 打折商品-超下订单数据(有市级分销商)
test_order_case7_person = Model(
    username='41000000024',password='888888',goodname=u'测试专用-团购商品-企',goodsnumber='1',goodsprice=999.9)

test_order_case7_agency = Model(
    username='41000000002',password='888888',)

#test_order_case8
# 打折商品-超下订单数据(有省级分销商)
test_order_case8_person = Model(
    username='41000000026',password='888888',goodname=u'测试专用-正常商品-企',goodsnumber='1',goodsprice=999.9)

test_order_case8_agency = Model(
    username='41000000025',password='888888',)