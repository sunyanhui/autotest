#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.osms.data_shop_basic_information import *
from action.action_login import Login
from action.shop.action_shop_basic_information import ShopBasicInformation
import unittest
import time

class TestShopBasicInformation(unittest.TestCase):
    u'''
    测试超市商品品牌
    '''
    def setUp(self):
        self.login_page = Login()
        self.basic_information_page = ShopBasicInformation()

    def tearDown(self):
        pass
        #time.sleep(1)
        #self.login_page.quit()

    def test_basic_information_case1(self):
        u'''验证手机号输入10位数字'''

        case = test_shop_basic_information_case1
        self.assertTrue(self.login_page.open_browser(config.OSMS_URL),u"打开首页失败")

        #登录
        r = self.login_page.login(**case)
        self.assertTrue(r.result, r.msg)

        #验证输入情况
        r = self.basic_information_page.test_telephone(**case)
        self.assertTrue(r.result, r.msg)

        #验证提示信息
        self.assertEqual(r.error_information, case.error_information)