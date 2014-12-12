#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from testdata.osms.data_supermarket_modify_password import *
from action.action_login import Login
from action.supermarket.action_supermarket_modify_password import SupermarketModifyPassword
from common import config
import unittest
import logging
import time

class TestSupermarketModifyPassword(unittest.TestCase):
    u'''
    测试超市修改基本信息
    '''
    def setUp(self):
        self.login = Login()
        self.supermarket_modify_password = SupermarketModifyPassword()

    def tearDown(self):
        time.sleep(1)
        self.login.quit()


    def test_modifypass_case1(self):
        u'''测试超市修改密码功能'''
        self.assertTrue(self.login.open_browser(config.OLMS_URL),u"打开首页失败")
        r = self.login.login(**test_modifypass_case1)
        self.assertTrue(r['result'], r['msg'])
        r = self.supermarket_modify_password.modify_pass(**test_modifypass_case1)
        self.assertTrue(r['result'], r['msg'])

    def test_modifypass_case2(self):
        u'''测试超市修改密码功能，把密码修改回来'''
        self.assertTrue(self.login.open_browser(config.OLMS_URL),u"打开首页失败")
        r = self.login.login(**test_modifypass_case2)
        self.assertTrue(r['result'], r['msg'])
        r = self.supermarket_modify_password.modify_pass(**test_modifypass_case2)
        self.assertTrue(r['result'], r['msg'])

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)

    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestSupermarketModifyPassword))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()