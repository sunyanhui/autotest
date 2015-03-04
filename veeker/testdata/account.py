#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common.config import ENV

class Test:
    u"""
    账号类，方便统一修改
    """

    #企业账号
    enterprise                             = 'XYHD3100028'
    enterprise_password                    = '888888'
    enterprise_manager_for_login           = '13000000001'
    enterprise_manager_for_login_password  = '888888'
    enterprise_manager_for_test            = '14000000001'
    enterprise_manager_for_test_password   = '888888'

    #省级分销商账号
    agency_province                        = '41000000025'
    agency_province_password               = '888888'
    agency_province_person                 = '41000000026'
    agency_province_person_password        = '888888'

    #市级分销商账号
    agency_city                            = '41000000002'
    agency_city_password                   = '888888'
    agency_city_manager                    = '41000000003'
    agency_city_manager_password           = '888888'
    agency_city_manager_for_test           = '41000000027'
    agency_city_manager_for_test_password  = '888888'
    agency_city_person                     = '41000000024'   #该分销商所属地区
    agency_city_person_password            = '888888'


    #县级分销商账号
    agency_country                         = '41000000020'
    agency_country_password                = '888888'
    agency_country_person                  = '41000000022'   #该分销商所属地区
    agency_country_person_password         = '888888'


    #超市
    supermarket                            = 'XYHD3100030'
    supermarket_password                   = '888888'
    supermarket_manager_for_login          = '11000000001'
    supermarket_manager_for_login_password = '888888'
    supermarket_manager_for_test           = '21000000001'

    #联盟店
    shop                                   = '31000000001'
    shop_password                          = '888888'
    shop_manager_for_login                 = '50000000002'
    shop_manager_for_login_password        = '888888'
    shop_manager_for_test                  = '41000000028'
    shop_manager_for_test_password         = '888888'

    #个人账号1
    person1                                = '23000000001'
    person1_password                       = '888888'

    #个人账号2
    person2                                = '41000000019'
    person2_password                       = '888888'

    #个人账号 测试联盟店退货用
    person_for_shop_sales_return           = '41000000030'
    person_for_shop_sales_return_password  = '888888'

    #个人账号 测试分销商退货用
    person_for_agency_sales_return         = '41000000024'
    person_for_agency_sales_return_password= '888888'

class Online:
    u'''
    账号类，方便统一修改
    '''

    #企业账号
    enterprise                             = 'XYHD3100000'
    enterprise_password                    = '6666666'
    enterprise_manager_for_login           = '14000000003'
    enterprise_manager_for_login_password  = 'ww5013358195'
    enterprise_manager_for_test            = '41000000192'
    enterprise_manager_for_test_password   = '888888'

    #省级分销商账号
    agency_province                        = '11000000008'
    agency_province_password               = '111111'
    agency_province_person                 = '13000000020'
    agency_province_person_password        = '111111'

    #市级分销商账号
    agency_city                            = '31000000007'
    agency_city_password                   = '111111'
    agency_city_manager                    = '13000000013'
    agency_city_manager_password           = 'ww5013358195'
    agency_city_manager_for_test           = ''
    agency_city_manager_for_test_password  = ''
    agency_city_person                     = '13000000019'   #该分销商所属地区
    agency_city_person_password            = '111111'

    #县级分销商账号
    agency_country                         = '41000000124'
    agency_country_password                = '111111'
    agency_country_person                  = '50000000004'   #该分销商所属地区
    agency_country_person_password         = '111111'

    #超市
    supermarket                            = 'XYHD3100012'
    supermarket_password                   = '6666666'
    supermarket_manager_for_login          = '23000000001'
    supermarket_manager_for_login_password = 'ww5013358195'
    supermarket_manager_for_test           = '41000000193'

    #联盟店
    shop                                   = '54000000001'
    shop_password                          = '111111'
    shop_manager_for_login                 = '22000000001'
    shop_manager_for_login_password        = 'ww5013358195'
    shop_manager_for_test                 = ''
    shop_manager_for_test_password        = ''

    #个人账号1
    person1                                = '21000000001'
    person1_password                       = 'ww5013358195'

    #个人账号2
    person2                                = '41000000120'
    person2_password                       = '6666666'

    #个人账号 测试联盟店退货用
    person_for_shop_sales_return           = '41000000272'
    person_for_shop_sales_return_password  = '888888'

    #个人账号 测试分销商退货用
    person_for_agency_sales_return         = '13000000019'
    person_for_agency_sales_return_password= '111111'


if ENV == 'test':
    Account = Test
else:
    Account = Online
