#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from common import config
from testdata.osms.data_supermarket_modify_password import *
from action.action_login import Login
from action.supermarket.action_supermarket_modify_password import SupermarketModifyPassword

import unittest
import logging
import time

class TestSupermarketModifyPassword(unittest.TestCase):
    u'''
    测试超市修改基本信息
    '''
    def setUp(self):
        self.login_page = Login()
        self.modify_password_page = SupermarketModifyPassword()

    def tearDown(self):
        time.sleep(1)
        self.login_page.quit()

    def test_modify_password_case1(self):
        u'''测试超市修改密码功能'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")
        r = self.login_page.login(**test_modify_password_case1)
        self.assertTrue(r.result, r.msg)
        r = self.modify_password_page.modify_pass(**test_modify_password_case1)
        self.assertTrue(r.result, r.msg)

    def test_modify_password_case2(self):
        u'''测试超市修改密码功能，把密码修改回来'''
        self.assertTrue(self.login_page.open_browser(config.BASE_URL),u"打开首页失败")
        r = self.login_page.login(**test_modify_password_case2)
        self.assertTrue(r.result, r.msg)
        r = self.modify_password_page.modify_pass(**test_modify_password_case2)
        self.assertTrue(r.result, r.msg)

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)

    a = unittest.TestSuite()
    a.addTests(unittest.makeSuite(TestSupermarketModifyPassword))
    b = unittest.TextTestRunner()
    b.run(a)
    #unittest.main()