#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from testdata.osms.data_supermarket_modify_info import *
from action.action_login import Login
from action.supermarket.action_supermarket_modify_info import SupermarketModifyInfo
from common import config
import unittest
import logging
import time

class TestSupermarketModifyInfo(unittest.TestCase):
    u'''
    测试超市修改基本信息
    '''
    def setUp(self):
        self.login = Login()
        self.supermarketModifyInfo = SupermarketModifyInfo()

    def tearDown(self):
        time.sleep(1)
        self.login.quit()


    def test_modifyinfo_case1(self):
        u'''测试超市版注册功能，注册成功后，使用新注册的账号登录'''
        self.assertTrue(self.login.open_browser(config.OLMS_URL),u"打开首页失败")
        r = self.login.login(**test_modifyinfo_case1)
        self.assertTrue(r['result'], r['msg'])
        r = self.supermarketModifyInfo.modify_info(**test_modifyinfo_case1)
        self.assertTrue(r['result'], r['msg'])

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)

    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestSupermarketModifyInfo))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()