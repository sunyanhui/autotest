#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

#正常商品下订单数据
test_order_case1_person = dict(
    username='21000000001',password='ww5013358195',ifrememberusername='no',
    goodname=u'测试专用-正常商品-企',startprice='',endprice='',selectindustry='',goodsnumber='1',
    invoice='no',payondelivery='no',remark='only a test',
    goodsprice=999.9)


test_order_case1_enterprise = dict(
    username='XYHD3100000',password='6666666',ifrememberusername='no',)

#团购商品下订单数据
test_order_case2_person = dict(
    username='21000000001',password='ww5013358195',ifrememberusername='no',
    goodname=u'测试专用-团购商品-企',startprice='',endprice='',selectindustry='',goodsnumber='1',
    invoice='no',payondelivery='no',remark='only a test',
    goodsprice=999.9)


test_order_case2_enterprise = dict(
    username='XYHD3100000',password='6666666',ifrememberusername='no',)

#打折商品下订单数据
test_order_case3_person = dict(
    username='21000000001',password='ww5013358195',ifrememberusername='no',
    goodname=u'测试专用-打折商品-企',startprice='',endprice='',selectindustry='',goodsnumber='1',
    invoice='no',payondelivery='no',remark='only a test',
    goodsprice=999.9)


test_order_case3_enterprise = dict(
    username='XYHD3100000',password='6666666',ifrememberusername='no',)

#打折商品下订单数据
test_order_case4 = dict(
    username='21000000001',password='ww5013358195',ifrememberusername='no',
    goodname=u'测试专用-正常商品-企',startprice='',endprice='',selectindustry='',goodsnumber='1',
    invoice='no',payondelivery='no',remark='only a test',
    goodsprice=999.9)

#test_order_case6
# 打折商品-超下订单数据(有县级分销商)
test_order_case6_person = dict(
    username='50000000004',password='111111',ifrememberusername='no',
    goodname=u'测试专用-打折商品-企',startprice='',endprice='',selectindustry='',goodsnumber='1',
    invoice='no',payondelivery='no',remark='only a test',
    goodsprice=999.9)


test_order_case6_agency = dict(
    username='41000000124',password='111111',ifrememberusername='no',)

#test_order_case7
# 打折商品-超下订单数据(有市级分销商)
test_order_case7_person = dict(
    username='13000000019',password='111111',ifrememberusername='no',
    goodname=u'测试专用-团购商品-企',startprice='',endprice='',selectindustry='',goodsnumber='1',
    invoice='no',payondelivery='no',remark='only a test',
    goodsprice=999.9)


test_order_case7_agency = dict(
    username='31000000007',password='111111',ifrememberusername='no',)

#test_order_case8
# 打折商品-超下订单数据(有省级分销商)
test_order_case8_person = dict(
    username='13000000020',password='111111',ifrememberusername='no',
    goodname=u'测试专用-正常商品-企',startprice='',endprice='',selectindustry='',goodsnumber='1',
    invoice='no',payondelivery='no',remark='only a test',
    goodsprice=999.9)

test_order_case8_agency = dict(
    username='11000000008',password='111111',ifrememberusername='no',)