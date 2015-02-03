#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common.output import Model
from ..account import Account

#正常商品下订单数据
test_order_case1_person = Model(
    username=Account.person1,
    password=Account.person1_password,
    goodname=u'测试专用-正常商品-企',
    goodsnumber='1',
    goodsprice=999.9)

test_order_case1_enterprise = Model(
    username=Account.enterprise,
    password=Account.enterprise_password,)

#团购商品下订单数据
test_order_case2_person = Model(
    username=Account.person1,
    password=Account.person1_password,
    goodname=u'测试专用-团购商品-企',
    goodsnumber='1',
    goodsprice=999.9)

test_order_case2_enterprise = Model(
    username=Account.enterprise,
    password=Account.enterprise_password,)

#打折商品下订单数据
test_order_case3_person = Model(
    username=Account.person1,
    password=Account.person1_password,
    goodname=u'测试专用-打折商品-企',
    goodsnumber='1',
    goodsprice=999.9)

test_order_case3_enterprise = Model(
    username=Account.enterprise,
    password=Account.enterprise_password,)

#打折商品下订单数据
test_order_case4 = Model(
    username=Account.person1,
    password=Account.person1_password,
    goodname=u'测试专用-正常商品-企',
    goodsnumber='1',
    goodsprice=999.9)

#test_order_case6
# 打折商品-超下订单数据(有县级分销商)
test_order_case6_person = Model(
    username=Account.agency_country_person,
    password=Account.agency_country_person_password,
    goodname=u'测试专用-打折商品-企',
    goodsnumber='1',
    goodsprice=999.9)

test_order_case6_agency = Model(
    username=Account.agency_country,
    password=Account.agency_country_password)

#test_order_case7
# 打折商品-超下订单数据(有市级分销商)
test_order_case7_person = Model(
    username=Account.agency_city_person,
    password=Account.agency_city_person_password,
    goodname=u'测试专用-团购商品-企',
    goodsnumber='1',
    goodsprice=999.9)

test_order_case7_agency = Model(
    username=Account.agency_city,
    password=Account.agency_city_password,)

#test_order_case8
# 打折商品-超下订单数据(有省级分销商)
test_order_case8_person = Model(
    username=Account.agency_province_person,
    password=Account.agency_province_person_password,
    goodname=u'测试专用-正常商品-企',
    goodsnumber='1',
    goodsprice=999.9)

test_order_case8_agency = Model(
    username=Account.agency_province,
    password=Account.agency_province_password)